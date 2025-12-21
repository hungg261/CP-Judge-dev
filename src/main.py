from utils.classes import TestCase, Compile
import json

def load_config(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"{path} not found")
    except json.JSONDecodeError:
        print(f"{path} is not valid JSON")
    return None

class Instance:
    def __init__(self):
        self.config = load_config("src/config.json")
        self.NTEST = self.config["config"]["tests-count"]
        
        self.brute_lang = self.config["config"]["languages"]["brute_force"]
        self.sol_lang = self.config["config"]["languages"]["solution"]
    
    def init(self):
        Compile(self.brute_lang, self.sol_lang)
    
    def RunTest(self, test):
        TCase = TestCase(test, self.brute_lang, self.sol_lang)
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
    
    ins = Instance()
    ins.init()
    
    print(ins.Run())