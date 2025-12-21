import shutil
from pathlib import Path

def cleanup_subworkspaces(root_folder):
    root = Path(root_folder)
    for path in root.rglob("workspace-*"):
        if path.is_dir():
            shutil.rmtree(path)

def cleanup_workspaces():
    cleanup_subworkspaces("src/data")
    cleanup_subworkspaces("src/scripts")
    
if __name__ == "__main__":
    cleanup_workspaces()