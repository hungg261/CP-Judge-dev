import subprocess
import shutil

def CompileGenerator():
    subprocess.run(["g++", "src/generator/generator.cpp", "-o", "src/scripts/generator.exe"])


class Python:
    @staticmethod
    def Compile_BruteForce():
        shutil.copyfile("src/solutions/Python/brute_force.py", "src/scripts/brute_force.py")

        
    @staticmethod
    def Compile_Solution():
        shutil.copyfile("src/solutions/Python/solution.py", "src/scripts/solution.py")
    

class CPP:
    @staticmethod
    def Compile_BruteForce():
        subprocess.run(["g++", "src/solutions/CPP/brute_force.cpp", 
                    "-o", "src/scripts/brute_force"],
                    check=True)
        
    @staticmethod
    def Compile_Solution():
        subprocess.run(["g++", f"src/solutions/CPP/solution.cpp",
                    "-o", f"src/scripts/solution"],
                    check=True)


if __name__ == "__main__":    
    CompileGenerator()
    
    CPP.Compile_Solution()
    Python.Compile_BruteForce()
    