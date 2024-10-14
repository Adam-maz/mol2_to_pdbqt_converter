import os
import subprocess
from pathlib import Path

path = os.getcwd()
dir_list = os.listdir(path)
for molecule in dir_list:
    if molecule.endswith(".mol2"):
        full_element_path = Path(path, molecule)
        converted_name = molecule.replace("mol2", "pdbqt")
        full_converted_name = Path(path, converted_name)

        command = subprocess.run(
            ["obabel", str(full_element_path), "-O", str(full_converted_name)],
            text=True,
        )
    else:
        pass
