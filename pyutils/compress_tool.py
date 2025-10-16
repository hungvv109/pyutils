import shutil
from pathlib import Path

def compress_folder(input_folder, output_zip, logger):
    folder = Path(input_folder)
    if not folder.exists():
        logger.error(f"Folder '{folder}' not found.")
        return

    shutil.make_archive(output_zip.replace('.zip', ''), 'zip', folder)
    logger.info(f"Compressed '{folder}' → '{output_zip}'")
