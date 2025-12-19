import subprocess
from pathlib import Path
import os

# script_dir = Path(__file__).resolve().parent
# os.chdir(script_dir)

def CompileGenerator():
    subprocess.run(["g++", "src/generator/generator.cpp", "-o", "src/generator/generator.exe"])

if __name__ == "__main__":
    CompileGenerator()