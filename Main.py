"""Start the JPZ desktop application."""
from pathlib import Path
import sys

def start():
    program_dir = Path(__file__).resolve().parent / "JPZ_DESKTOP"
    sys.path.insert(0, str(program_dir))
    from main import run
    run()

if __name__ == "__main__":
    start()
