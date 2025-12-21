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
        Compile(self.brute_lang, self.sol_lang)
        if not os.path.exists(f"src/data/{self.sessionID}"):
            os.mkdir(f"src/data/{self.sessionID}")
    
    def RunTest(self, test):
        TCase = TestCase(test, self.brute_lang, self.sol_lang, self.sessionID)
        TCase.Run()
        
        return TCase.accepted()
        
    def Run(self):
        for test in range(1, self.NTEST + 1):
            print(f"Running test #{test}:")
            
            if(not self.RunTest(test)):
                print("WRONG ANSWER!")
                return False
            
            print("CORRECT")
        
        return True

if __name__ == "__main__":
    config = load_config("src/config.json")
    
    ins = Instance(NTEST=69)
    ins.init()
    
    print(ins.Run())
    
    ins2 = Instance(NTEST=5)
    ins2.init()
    
    print(ins2.Run())