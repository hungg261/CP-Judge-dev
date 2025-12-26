from utils.run import RunSolvers, GenerateTest
from utils.prepare import CompileGenerator, CompileSolvers
from utils.diff import compare, fc_compare
import os

def Compile(brute_lang, sol_lang, sessionID):
    if not os.path.exists(f"src/scripts/{sessionID}"):
        os.makedirs(f"src/scripts/{sessionID}", exist_ok=True)
    
    CompileGenerator(sessionID)
    CompileSolvers(brute_lang, sol_lang, sessionID)

class TestCase:
    def __init__(self, id, brute_lang, sol_lang, sessionID):
        self.id = id
        self.brute_lang = brute_lang
        self.sol_lang = sol_lang
        
        self.sessionID = sessionID
        
    def Preprocess(self):
        Compile(self.brute_lang, self.sol_lang, self.sessionID)
        
    def Run(self):
        GenerateTest(self.id, self.sessionID)
        RunSolvers(self.brute_lang, self.sol_lang, self.sessionID)
    
    def accepted(self):
        return compare(self.sessionID)
        

if __name__ == "__main__":
    test = TestCase(12, "python", "python")
    test.Compile()
    
    test.Run()
    
    print(test.accepted())