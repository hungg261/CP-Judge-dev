import subprocess
import shutil


class Python:
    @staticmethod
    def Compile_BruteForce():
        shutil.copyfile("src/solvers/Python/brute_force.py", "src/scripts/brute_force.py")

        
    @staticmethod
    def Compile_Solution():
        shutil.copyfile("src/solvers/Python/solution.py", "src/scripts/solution.py")
    

class CPP:
    @staticmethod
    def Compile_BruteForce():
        subprocess.run(["g++", "src/solvers/CPP/brute_force.cpp", 
                    "-o", "src/scripts/brute_force"],
                    check=True)
        
    @staticmethod
    def Compile_Solution():
        subprocess.run(["g++", f"src/solvers/CPP/solution.cpp",
                    "-o", f"src/scripts/solution"],
                    check=True)


def CompileGenerator():
    subprocess.run(["g++", "src/generator/generator.cpp", "-o", "src/scripts/generator.exe"])

def Compile_BruteForce(lang):
    match lang:
        case "python":
            Python.Compile_BruteForce()
        case "c++":
            CPP.Compile_BruteForce()
        case _:
            pass

def Compile_Solution(lang):
    match lang:
        case "python":
            Python.Compile_Solution()
        case "c++":
            CPP.Compile_Solution()
        case _:
            pass
        
def CompileSolvers(brute_lang, sol_lang):
    Compile_BruteForce(brute_lang)
    Compile_Solution(sol_lang)

if __name__ == "__main__":    
    CompileGenerator()
    CompileSolvers("c++", "c++")
    