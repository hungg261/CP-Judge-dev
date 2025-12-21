import subprocess
import shutil


class Python:
    @staticmethod
    def Compile_BruteForce(sessionID):
        shutil.copyfile("src/solvers/Python/brute_force.py", f"src/scripts/{sessionID}/brute_force.py")

        
    @staticmethod
    def Compile_Solution(sessionID):
        shutil.copyfile("src/solvers/Python/solution.py", f"src/scripts/{sessionID}/solution.py")
    

class CPP:
    @staticmethod
    def Compile_BruteForce(sessionID):
        subprocess.run(["g++", "src/solvers/CPP/brute_force.cpp", 
                    "-o", f"src/scripts/{sessionID}/brute_force"],
                    check=True)
        
    @staticmethod
    def Compile_Solution(sessionID):
        subprocess.run(["g++", f"src/solvers/CPP/solution.cpp",
                    "-o", f"src/scripts/{sessionID}/solution"],
                    check=True)


def CompileGenerator(sessionID):
    subprocess.run(["g++", "src/generator/generator.cpp", "-o", f"src/scripts/{sessionID}/generator.exe"])

def Compile_BruteForce(lang, sessionID):
    match lang:
        case "python":
            Python.Compile_BruteForce(sessionID)
        case "c++":
            CPP.Compile_BruteForce(sessionID)
        case _:
            pass

def Compile_Solution(lang, sessionID):
    match lang:
        case "python":
            Python.Compile_Solution(sessionID)
        case "c++":
            CPP.Compile_Solution(sessionID)
        case _:
            pass
        
def CompileSolvers(brute_lang, sol_lang, sessionID):
    Compile_BruteForce(brute_lang, sessionID)
    Compile_Solution(sol_lang, sessionID)

if __name__ == "__main__":    
    CompileGenerator()
    CompileSolvers("python", "c++")
    