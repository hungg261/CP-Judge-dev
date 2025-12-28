import subprocess
import sys
import os

from .verdicts import *

def GenerateTest(test, sessionID):
    with open(f"src/data/{sessionID}/test_case.inp", "wb") as finp:
        subprocess.run([f"src/scripts/{sessionID}/generator.exe", str(test)], stdout=finp, check=True)


class Python:
    @staticmethod
    def BruteForce(sessionID):
        try:
            with open(f"src/data/{sessionID}/test_case.inp", "rb") as inp, \
                 open(f"src/data/{sessionID}/brute_force.out", "wb") as out:
                
                subprocess.run(
                    [sys.executable, f"src/scripts/{sessionID}/brute_force.py"],
                    stdin=inp,
                    stdout=out,
                    stderr=subprocess.DEVNULL,
                    check=True
                )
            return JU
        except subprocess.CalledProcessError:
            return RE

    @staticmethod
    def Solution(sessionID, time_limit):
        try:
            with open(f"src/data/{sessionID}/test_case.inp", "rb") as inp, \
                 open(f"src/data/{sessionID}/solution.out", "wb") as out:
                
                subprocess.run(
                    [sys.executable, f"src/scripts/{sessionID}/solution.py"],
                    stdin=inp,
                    stdout=out,
                    stderr=subprocess.PIPE,
                    timeout=time_limit
                )
            return JU

        except subprocess.TimeoutExpired:
            return TLE

        except subprocess.CalledProcessError:
            return RE


class CPP:
    @staticmethod
    def BruteForce(sessionID):
        try:
            with open(f"src/data/{sessionID}/test_case.inp", "rb") as inp, \
                 open(f"src/data/{sessionID}/brute_force.out", "wb") as out:
                
                subprocess.run(
                    [f"src/scripts/{sessionID}/brute_force.exe"],
                    stdin=inp,
                    stdout=out,
                    stderr=subprocess.DEVNULL,
                    check=True
                )
            return JU
        except subprocess.CalledProcessError:
            return RE

    @staticmethod
    def Solution(sessionID, time_limit):
        try:
            with open(f"src/data/{sessionID}/test_case.inp", "rb") as inp, \
                 open(f"src/data/{sessionID}/solution.out", "wb") as out:
                
                subprocess.run(
                    [f"src/scripts/{sessionID}/solution.exe"],
                    stdin=inp,
                    stdout=out,
                    stderr=subprocess.PIPE,
                    timeout=time_limit
                )
            return JU

        except subprocess.TimeoutExpired:
            return TLE

        except subprocess.CalledProcessError:
            return RE


def Run_BruteForce(lang, sessionID):
    if lang == "python":
        Python.BruteForce(sessionID)
    else:
        CPP.BruteForce(sessionID)

def Run_Solution(lang, sessionID, time_limit):
    if lang == "python":
        return Python.Solution(sessionID, time_limit)
    else:
        return CPP.Solution(sessionID, time_limit)
        
def RunSolvers(brute_lang, sol_lang, sessionID, time_limit):
    Run_BruteForce(brute_lang, sessionID)
    
    runStat = Run_Solution(sol_lang, sessionID, time_limit)
    return runStat

if __name__ == "__main__":
    if not os.path.exists(f"src/data/{1}"):
        os.makedirs(f"src/data/{1}")
    if not os.path.exists(f"src/scripts/1"):
        os.makedirs(f"src/scripts/{1}")
    
    GenerateTest(36, 1)
    
    RunSolvers("python", "c++", 1)