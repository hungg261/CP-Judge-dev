from run import Run_BruteForce, Run_Solution
from prepare import CompileGenerator, CompileSolution

class TestCase:
    def __init__(self, id, brute_lang, sol_lang):
        self.id = id
        self.brute_lang = brute_lang
        self.sol_lang = sol_lang
        
    def Compile():
        CompileGenerator()
        CompileSolution()
        
    def Run(self):
        Run_BruteForce(self.brute_lang)
        Run_Solution(self.sol_lang)
        

if __name__ == "__main__":
    test = TestCase(12, "c++", "c++")
    test.Run()