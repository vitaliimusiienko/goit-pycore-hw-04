from pathlib import Path
from colorama import Fore

def vizualize_directory_path(path: str, indent: int = 0):
    directory = Path(path)
    
    for path in directory.iterdir():
        prefix = " " * indent
        if path.is_dir():
            print(Fore.BLUE + f"{prefix}{path.name}/")
            vizualize_directory_path(path, indent + 1)
        else:
            print(Fore.GREEN + f"{prefix}{path.name}")
            
vizualize_directory_path("./")