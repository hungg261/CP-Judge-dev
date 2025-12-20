import subprocess
import sys

# script_dir = Path(__file__).resolve().parent
# os.chdir(script_dir)

def GenerateTest(test):
    with open("src/data/test_case.inp", "wb") as finp:
        subprocess.run(["src/scripts/generator.exe", str(test)], stdout=finp, check=True)

class Python:
    @staticmethod
    def BruteForce():
        with open("src/data/test_case.inp", "rb") as input, open("src/data/brute_force.out", "wb") as output:
            subprocess.run([sys.executable, "src/scripts/brute_force.py"], stdin=input, stdout=output, check=True)
          
    @staticmethod  
    def Solution():
        with open("src/data/test_case.inp", "rb") as input, open("src/data/solution.out", "wb") as output:
            subprocess.run([sys.executable, "src/scripts/solution.py"], stdin=input, stdout=output, check=True)

class CPP:
    @staticmethod
    def BruteForce():
        with open("src/data/test_case.inp", "rb") as input, open("src/data/brute_force.out", "wb") as output:
            subprocess.run(["src/scripts/brute_force.exe"], stdin=input, stdout=output, check=True)
            
    @staticmethod
    def Solution():
        with open("src/data/test_case.inp", "rb") as input, open("src/data/solution.out", "wb") as output:
            subprocess.run(["src/scripts/solution.exe"], stdin=input, stdout=output, check=True)


def Run_BruteForce(lang):
    if lang == "python":
        Python.BruteForce()
    else:
        CPP.BruteForce()

def Run_Solution(lang):
    if lang == "python":
        Python.Solution()
    else:
        CPP.Solution()
        
def RunSolvers(brute_lang, sol_lang):
    Run_BruteForce(brute_lang)
    Run_Solution(sol_lang)

if __name__ == "__main__":
    GenerateTest(36)
    
    RunSolvers("c++", "python")