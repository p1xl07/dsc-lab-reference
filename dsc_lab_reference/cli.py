import argparse
import shutil
from importlib.resources import files
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description="Install the Data Science Lab reference notebooks into a folder.")
    parser.add_argument("--output", default="dsc-lab-notebooks", help="Destination folder")
    args = parser.parse_args()

    source = files("dsc_lab_reference").joinpath("notebooks")
    destination = Path(args.output).expanduser().resolve()
    destination.mkdir(parents=True, exist_ok=True)

    for item in source.iterdir():
        if item.name.endswith(".ipynb"):
            shutil.copyfile(item, destination / item.name)

    print(f"Copied notebooks to: {destination}")
    print("Open a notebook with: jupyter notebook")

if __name__ == "__main__":
    main()
