import os
import fnmatch
import glob
import shutil
from geobricks_common.core.filesystem import get_filename



def get_files_match(path, match):
    files = []
    for root, dirnames, filenames in os.walk(path):
        for filename in fnmatch.filter(filenames, match):
            files.append(os.path.join(root, filename))
    return files

def get_folders_match(path, match):
    files = []
    for root, dirnames, filenames in os.walk(path):
        for filename in fnmatch.filter(dirnames, match):
            files.append(os.path.join(root, filename))
    return files


def get_files(path):
    files = glob.glob(path)
    files_path = []
    for f in files:
        if os.path.isfile(f):
            files_path.append(f)
    return files_path


def get_month_by_filename(f):
    filename = get_filename(f)
    s = filename.split("_")
    date = s[len(s)-2]
    return date[4:6]


# get all layers of the same month
def get_monthly_layers(path):
    layers_by_month = {}
    files = get_files(path)

    for f in files:
        # cache layers by month
        month = get_month_by_filename(f)
        if month not in layers_by_month:
            layers_by_month[month] = []

        layers_by_month[month].append(f)

    return layers_by_month


def delete_folders(basepath, folder):
    folders = get_folders_match(basepath, folder)
    for f in folders:
        print f
        # shutil.rmtree(f)

# folders = get_folders_match('/media/vortex/LACIE SHARE/ECO_COUNTRIES/MOD13A3', 'PROCESSED')
# for f in folders:
#     print f
#     shutil.rmtree(f)
