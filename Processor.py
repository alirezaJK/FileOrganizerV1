from pathlib import Path
from collections import deque
import shutil
import Reporter
#a
def Process(input_path:Path , output_path:Path, SubFolders:bool=False):
    Reporter.logger.info("Process Started.")
    try:
        if SubFolders :
            files_filter = input_path.rglob("*")
        else:
            files_filter = input_path.iterdir()
    except Exception as e:
        Reporter.logger.error(f"{e}")
        return False
    buffers = deque()
    Reporter.logger.info(f"Searching Path : {input_path.name}")
    try:
        for p in files_filter:
            if p.is_file(): 
                buffers.append({"name": p.name, "path": p, "suffix": p.suffix})


        suffixes = list(set(f["suffix"] for f in buffers))


        folders = {}
        for suf in suffixes:
            clean_suf = suf.replace(".", "") if suf else "no_suffix"
            folder_path = output_path / clean_suf
            folder_path.mkdir(exist_ok=True)
            folders[suf] = folder_path  


        for f in buffers:
            target_folder = folders[f["suffix"]]
            shutil.move(str(f["path"]), str(target_folder / f["name"]))
    except Exception as e:
        Reporter.logger.error(f"{e}")
        return False
    return True