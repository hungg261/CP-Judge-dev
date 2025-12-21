from utils.run import RunSolvers, GenerateTest
from utils.prepare import CompileGenerator, CompileSolvers
from utils.diff import compare

def Compile(brute_lang, sol_lang):
    CompileGenerator()
    CompileSolvers(brute_lang, sol_lang)

class TestCase:
    def __init__(self, id, brute_lang, sol_lang):
        self.id = id
        self.brute_lang = brute_lang
        self.sol_lang = sol_lang
        
    def Preprocess(self):
        Compile(self.brute_lang, self.sol_lang)
        
    def Run(self):
        GenerateTest(self.id)
        RunSolvers(self.brute_lang, self.sol_lang)
    
    @staticmethod
    def accepted():
        return compare()
        

if __name__ == "__main__":
    test = TestCase(12, "python", "python")
    test.Compile()
    
    test.Run()
    
    print(test.accepted())