import os
from pathlib import Path

def rename_files(folder_path, prefix):
    folder = Path(folder_path)
    if not folder.exists():
        print(f"❌ Folder '{folder}' does not exist!")
        return

    for i, file in enumerate(folder.iterdir(), start=1):
        if file.is_file():
            new_name = f"{prefix}{i}{file.suffix}"
            file.rename(folder / new_name)
    print(f"✅ Renamed files in '{folder}' with prefix '{prefix}'")
