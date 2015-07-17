import glob
import os
import subprocess
from geobricks_common.core.filesystem import get_filename




def process_tifs_warp(input_path, output_path):
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    files = glob.glob(input_path + "/*.tif")
    for f in files:
        filename = get_filename(f)
        output_file_path = output_path + "/" + filename + ".tif"
        print output_file_path
        cmd = "gdalwarp -s_srs EPSG:4326 -t_srs EPSG:3857 -overwrite -co TILED=YES -co COMPRESS=DEFLATE '" + f + "' '" + output_file_path + "'"
        print cmd
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = process.communicate()
        print output
        print error

        # add_gdaladdo(output_file_path)

def process_tifs_translate(input_path, output_path):
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    files = glob.glob(input_path + "/*.tif")
    for f in files:
        filename = get_filename(f)
        output_file_path = output_path + "/" + filename + ".tif"
        print output_file_path
        cmd = "gdal_translate -co TILED=YES -co COMPRESS=DEFLATE '" + f + "' '" + output_file_path + "'"
        print cmd
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = process.communicate()
        print output
        print error
        add_gdaladdo(output_file_path)

def add_gdaladdo(output_file_path):
    cmd = "gdaladdo " + output_file_path + " 2 4 8 16 "
    print cmd
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    print output
    print error


def process_ECMWF():

    input_path = "/media/vortex/LaCie/LaCie/ECO_COUNTRIES/original/ecmwf/RAIN/MONTHLY/"
    output_path = "/media/vortex/LaCie/LaCie/ECO_COUNTRIES/original/3857/ECMWF/"

    # WARP
    process_tifs_warp(input_path, output_path)
    # process_tifs_warp(input_path + "/MEAN", output_path + "/ECMWF_AVG")
    # process_tifs_warp(input_path + "/ANOMALY", output_path + "/ECMWF_ANOMALY")
    # process_tifs_warp(input_path + "/ZSCORES", output_path + "/ECMWF_ZSCORE")

    # translate + gdaladdo
    input_path = "/media/vortex/LaCie/LaCie/ECO_COUNTRIES/original/3857/ECMWF/"
    output_path = "/media/vortex/LaCie/LaCie/ECO_COUNTRIES/ECMWF/"
    process_tifs_translate(input_path, output_path)
    # process_tifs_translate(input_path + "/ECMWF_AVG", output_path + "/ECMWF_AVG")
    # process_tifs_translate(input_path + "/ECMWF_ANOMALY", output_path + "/ECMWF_ANOMALY")
    # process_tifs_translate(input_path + "/ECMWF_ZSCORE", output_path + "/ECMWF_ZSCORE")

process_ECMWF()
