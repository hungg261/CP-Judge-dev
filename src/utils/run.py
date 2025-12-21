import subprocess
import sys
import os

# script_dir = Path(__file__).resolve().parent
# os.chdir(script_dir)

def GenerateTest(test, sessionID):
    with open(f"src/data/{sessionID}/test_case.inp", "wb") as finp:
        subprocess.run(["src/scripts/generator.exe", str(test)], stdout=finp, check=True)

class Python:
    @staticmethod
    def BruteForce(sessionID):
        with open(f"src/data/{sessionID}/test_case.inp", "rb") as input, open(f"src/data/{sessionID}/brute_force.out", "wb") as output:
            subprocess.run([sys.executable, "src/scripts/brute_force.py"], stdin=input, stdout=output, check=True)
          
    @staticmethod  
    def Solution(sessionID):
        with open(f"src/data/{sessionID}/test_case.inp", "rb") as input, open(f"src/data/{sessionID}/solution.out", "wb") as output:
            subprocess.run([sys.executable, "src/scripts/solution.py"], stdin=input, stdout=output, check=True)

class CPP:
    @staticmethod
    def BruteForce(sessionID):
        with open(f"src/data/{sessionID}/test_case.inp", "rb") as input, open(f"src/data/{sessionID}/brute_force.out", "wb") as output:
            subprocess.run(["src/scripts/brute_force.exe"], stdin=input, stdout=output, check=True)
            
    @staticmethod
    def Solution(sessionID):
        with open(f"src/data/{sessionID}/test_case.inp", "rb") as input, open(f"src/data/{sessionID}/solution.out", "wb") as output:
            subprocess.run(["src/scripts/solution.exe"], stdin=input, stdout=output, check=True)


def Run_BruteForce(lang, sessionID):
    if lang == "python":
        Python.BruteForce(sessionID)
    else:
        CPP.BruteForce(sessionID)

def Run_Solution(lang, sessionID):
    if lang == "python":
        Python.Solution(sessionID)
    else:
        CPP.Solution(sessionID)
        
def RunSolvers(brute_lang, sol_lang, sessionID):
    Run_BruteForce(brute_lang, sessionID)
    Run_Solution(sol_lang, sessionID)

if __name__ == "__main__":
    if not os.path.exists(f"src/data/{1}"):
        os.mkdir(f"src/data/{1}")
    
    GenerateTest(36, 1)
    
    RunSolvers("python", "c++", 1)