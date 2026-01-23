import subprocess
import yaml
from pathlib import Path

def run_command():
    # SAFE: no shell=True, args as list
    cmd = ["pwd"]
    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        check=True
    )
    print("Command output:")
    print(result.stdout)


def load_yaml():
    yaml_path = Path("/home/fox/test.yaml")

    if not yaml_path.exists():
        print("YAML file not found:", yaml_path)
        return

    with open(yaml_path, "r") as f:
        data = yaml.safe_load(f)

    print("YAML content:")
    print(data)


if __name__ == "__main__":
    run_command()
    load_yaml()
