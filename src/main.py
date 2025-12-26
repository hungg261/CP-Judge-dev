from utils.classes import TestCase, Compile
from utils.file import load_config
import os
import uuid
import multiprocessing

WORKSPACE_COUNTER = 0
CONFIG = load_config("src/config.json")

class Instance:
    def __init__(self, NTEST = None, brute_lang = None, sol_lang = None, sessionID = None):
        self.NTEST = CONFIG["config"]["tests-count"] if NTEST is None else NTEST
        
        self.brute_lang = CONFIG["config"]["languages"]["brute_force"] if brute_lang is None else brute_lang
        self.sol_lang = CONFIG["config"]["languages"]["solution"] if sol_lang is None else sol_lang
        
        if sessionID is None:
            global WORKSPACE_COUNTER
            
            self.sessionID = "workspace-" + uuid.uuid4().hex
            WORKSPACE_COUNTER += 1
    
    def init(self):
        Compile(self.brute_lang, self.sol_lang, self.sessionID)
        if not os.path.exists(f"src/data/{self.sessionID}"):
            os.mkdir(f"src/data/{self.sessionID}")
    
    def RunTest(self, test):
        TCase = TestCase(test, self.brute_lang, self.sol_lang, self.sessionID)
        TCase.Run()
        
        return TCase.accepted()
        
    def SampleRun(self, output=True):
        for test in range(1, self.NTEST + 1):
            if output:
                print(f"Running test #{test}:")
            
            if(not self.RunTest(test)):
                if output:
                    print("WRONG ANSWER!")
                return False
            
            if output:
                print("CORRECT")
        
        return True

import random
def test_run(id, ntest):
    ins = Instance(NTEST=ntest)
    ins.init()
    
    ins.SampleRun(output=False)
    print(f"[!] #{id} - Finished")
    
if __name__ == "__main__":
    # ins = Instance(NTEST=50)
    # ins.init()
    
    # ins.SampleRun()

    lthread = []
    for i in range(10):
        nt = random.randint(1, 100)
        print(f"#{i}: ", nt)
        
        thread = multiprocessing.Process(target=test_run, args=(i, nt))
        thread.start()
        
        lthread.append(thread)
    
    for t in lthread:
        t.join()
    
    from utils.clean import cleanup_workspaces
    cleanup_workspaces("workspace-*")