import filecmp
import subprocess
import os

def compare(sessionID):
    return filecmp.cmp(f"src/data/{sessionID}/solution.out", f"src/data/{sessionID}/brute_force.out", shallow=False)

def fc_compare(sessionID):
    return subprocess.run(["fc", fr"src\data\{sessionID}\solution.out", fr"src\data\{sessionID}\brute_force.out"]).returncode == 0;


if __name__ == "__main__":
    print(os.getcwd())
    print(compare("workspace-9d8b5b6ade9a4c8b9b3d2e91b78653aa"))