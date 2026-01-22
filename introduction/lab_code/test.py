#test change
import subprocess
import yaml
from pathlib import Path

def run_command():
    # Safe subprocess call (no shell=True)
    result = subprocess.run(
        ["pwd"],
        capture_output=True,
        text=True,
        check=True
    )

    result2 = subprocess.run(
        ["ls"],
        capture_output=True,
        text=True,
        check=True
    )

    print(result.stdout)
    print(result2.stdout)


def load_yaml(path: Path):
    if not path.exists():
        raise FileNotFoundError(f"{path} does not exist")

    with path.open("r") as f:
        data = yaml.safe_load(f)

    print(data)


if __name__ == "__main__":
    run_command()
    load_yaml(Path("test.yaml"))

