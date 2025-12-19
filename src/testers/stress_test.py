import subprocess
from pathlib import Path
import os

script_dir = Path(__file__).resolve().parent
os.chdir(script_dir)

subprocess.run(["g++", "../generator/generator.cpp", "-o", "generator.exe"])