import filecmp

def compare():
    return filecmp.cmp("src/data/solve.ans", "src/data/solve.out", shallow=False)

if __name__ == "__main__":
    print(compare())