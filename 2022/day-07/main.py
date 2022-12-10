from pathlib import Path

class Directory:
    def __init__(self, name: str, path: Path):
        self.name = name
        self.path = path
        self.subdirs = []
        self.filesize = 0

    def __str__(self):
        return f"Name: {self.name} - Filesize: {self.filesize}"

def parse_directories(lines: list) -> dict():
    dirs = dict()
    current_dir = Directory(name='/', path=Path('/'))
    for line in lines[1:]: 
        if line.startswith('$ cd'):
            # store previous dir
            if current_dir.path not in dirs.keys():
                dirs[current_dir.path] = current_dir 
                       
            # change to new dir 
            target_name = line.split()[2]
            if target_name == '..':
                target_path = current_dir.path.parent
            else:
                target_path = current_dir.path / target_name
            current_dir = Directory(name=target_path.name, path=target_path)
            
        elif line.startswith('$ ls'):
            continue 
        elif line.startswith('dir'):
            current_dir.subdirs.append(line.split()[1])
        elif line[:1].isdigit():
            current_dir.filesize += int(line.split()[0])
    
    dirs[current_dir.path] = current_dir
    return dirs
        
def get_total_filesize(dir_: Path, dirs: dict) -> int:
    filesize = dirs[dir_].filesize
    for subdir in dirs[dir_].subdirs:
        subpath = dir_ / subdir
        filesize += get_total_filesize(subpath, dirs)
    return filesize
    

def sum_filesize(dirs: dict, threshold: int) -> int:
    results = dict()
    total_size = 0
    for dir_ in dirs.keys():
        results[dir_] = get_total_filesize(dir_, dirs)
        if results[dir_] < threshold:
            total_size += results[dir_]
    return results, total_size    
    
if __name__ == "__main__":
    filename = 'input.txt'
    lines = [line.strip() for line in open(filename) if line.strip()]
    dirs = parse_directories(lines)
    results, total_size = sum_filesize(dirs, threshold=100_000)
    
    print('--- results ---')
    print(f'{total_size=}')

    total_disc = 70000000
    needed_unused = 30000000
    currently_unused = total_disc - results[Path('/')]
    space_to_remove = needed_unused - currently_unused
    large_dirs = [(key, value) for key, value in results.items() if value > space_to_remove]
    dir_to_remove = sorted(large_dirs, key=lambda x: x[1])[0]
    print(f"{dir_to_remove=}")


    