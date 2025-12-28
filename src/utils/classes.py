from .run import RunSolvers, GenerateTest
from .prepare import CompileGenerator, CompileSolvers
from .diff import compare
import os

def Compile(brute_lang, sol_lang, sessionID):
    if not os.path.exists(f"src/scripts/{sessionID}"):
        os.makedirs(f"src/scripts/{sessionID}", exist_ok=True)
    
    CompileGenerator(sessionID)
    CompileSolvers(brute_lang, sol_lang, sessionID)

class TestCase:
    def __init__(self, id, brute_lang, sol_lang, sessionID, time_limit = 1000):
        self.id = id
        self.brute_lang = brute_lang
        self.sol_lang = sol_lang
        
        self.sessionID = sessionID
        self.time_limit = time_limit
        
    def Preprocess(self):
        Compile(self.brute_lang, self.sol_lang, self.sessionID)
        
    def Run(self):
        GenerateTest(self.id, self.sessionID)
        
        runStat = RunSolvers(self.brute_lang, self.sol_lang, self.sessionID, self.time_limit / 1000)
        return runStat
    
    def accepted(self):
        return compare(self.sessionID)
        

if __name__ == "__main__":
    test = TestCase(12, "python", "python")
    test.Compile()
    
    test.Run()
    
    print(test.accepted())