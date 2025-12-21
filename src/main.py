from utils.classes import TestCase, Compile
import json
import os

def load_config(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"{path} not found")
    except json.JSONDecodeError:
        print(f"{path} is not valid JSON")
    return None

WORKSPACE_COUNTER = 0
CONFIG = load_config("src/config.json")

class Instance:
    def __init__(self, NTEST = None, brute_lang = None, sol_lang = None, sessionID = None):
        self.NTEST = CONFIG["config"]["tests-count"] if NTEST is None else NTEST
        
        self.brute_lang = CONFIG["config"]["languages"]["brute_force"] if brute_lang is None else brute_lang
        self.sol_lang = CONFIG["config"]["languages"]["solution"] if sol_lang is None else sol_lang
        
        if sessionID is None:
            global WORKSPACE_COUNTER
            
            self.sessionID = "workspace-" + str(WORKSPACE_COUNTER).zfill(2)
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

if __name__ == "__main__":
    
    import threading
    
    def test_run(id, ntest):
        ins = Instance(NTEST=ntest)
        ins.init()
        
        ins.SampleRun(output=False)
        print(f"[!] #{id} - Finished")

    t1 = threading.Thread(target=test_run, args=(1, 100,))
    t2 = threading.Thread(target=test_run, args=(2, 69,))
    t3 = threading.Thread(target=test_run, args=(3, 58,))
    t4 = threading.Thread(target=test_run, args=(4, 14,))
    t5 = threading.Thread(target=test_run, args=(5, 5,))
    t6 = threading.Thread(target=test_run, args=(6, 57,))
    
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()
    
    from utils.clean import cleanup_workspaces
    cleanup_workspaces()