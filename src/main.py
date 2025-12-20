from utils.prepare import CompileGenerator, CompileSolution
from utils.run import RunSolution
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