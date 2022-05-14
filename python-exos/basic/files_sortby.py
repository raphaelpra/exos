#!/usr/bin/env python3

from pathlib import Path

def dir_path(root, course):
    return Path(root) / course / "logs"

def scan_course(root, course, deep=False):
    dir = dir_path(root, course)
    glob_pattern = "**/*" if deep else "*"
    return (f for f in dir.glob(glob_pattern) if f.is_file())

def sort_files(root: Path, course: str,
               deep=False, criteria='name'):
    """
    sort files under the folder 'root'

    only the subfolder named 'course' is considered,
    and under that only the 'logs' folder is taken into account

    Parameters:
      root: a Path to the main folder
      course: a str that gives the name of the first subfolder
      deep: a boolean that says if a recursive search is needed
      criteria: a str among 'name', 'namelen', or 'size'

    """
    files = scan_course(root, course, deep)
    dir = dir_path(root, course)

    if criteria == 'name':
        sort_function = lambda p: p.name
    elif criteria == 'namelen':
        sort_function = lambda p: len(p.name)
    elif criteria == 'size':
        sort_function = lambda p: p.stat().st_size
    # not too interesting - not advertized
    elif criteria == 'path':
        sort_function = lambda p: len(str(p.relative_to(dir)))
    return sorted(files, key = sort_function)

####################
def init():
    """
    a utility function only for populating the 'pathlib-foo' subfolder
    """
    scale = 10
    logs = Path("pathlib-foo") / "logs"
    logs.mkdir(parents=True, exist_ok = True)
    for i, log, key in ( (1, 0, 'b'), (10, 1, 'a'), (100, 2, 'c')):
        d = logs / f"dir{i}"
        d.mkdir(exist_ok = True)
        for j in range(1, 4):
            pad = (6-2*log) * 'x'
            f = d / f"file{j*key}{pad}"
            with f.open('w') as output:
                content = (i*scale+j) * '*'
                output.write(content + "\n")
            size = f.stat().st_size
            print(f"Wrote file {f} - size {size}")


if __name__ == '__main__':
    init()


