import filecmp

def compare(sessionID):
    return filecmp.cmp(f"src/data/{sessionID}/solution.out", f"src/data/{sessionID}/brute_force.out", shallow=False)

if __name__ == "__main__":
    print(compare())