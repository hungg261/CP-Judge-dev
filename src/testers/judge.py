import subprocess
from pathlib import Path
import os
import argparse

script_dir = Path(__file__).resolve().parent
os.chdir(script_dir)

def Generate(test):
    subprocess.run(["generator.exe", str(test)], check=True)

def RunSolution(test):
    return

