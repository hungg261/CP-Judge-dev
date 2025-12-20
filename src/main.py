from utils.classes import TestCase
import json

def load_config(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"{path} not found")
    except json.JSONDecodeError:
        print(f"{path} is not valid JSON")
    return None

if __name__ == "__main__":
    test = TestCase(36, "python", "c++")
    test.Compile()
    
    test.Run()
    
    print(test.accepted())