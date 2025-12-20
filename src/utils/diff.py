import filecmp

def compare():
    return filecmp.cmp("src/data/solution.out", "src/data/brute_force.out", shallow=False)

if __name__ == "__main__":
    print(compare())