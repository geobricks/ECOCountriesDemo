import os
import fnmatch

def get_files(path, match):
    files = []
    for root, dirnames, filenames in os.walk(path):
        for filename in fnmatch.filter(filenames, match):
            files.append(os.path.join(root, filename))
    return files

