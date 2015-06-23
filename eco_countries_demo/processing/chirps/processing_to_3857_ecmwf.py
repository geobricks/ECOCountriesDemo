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
        cmd = "gdalwarp -s_srs EPSG:4326 -t_srs EPSG:3857 -overwrite '" + f + "' '" + output_file_path + "'"
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


def process_chirps():

    input_path = "/media/vortex/LaCie/LaCie/ECO_COUNTRIES/original/chirps/"
    output_path = "/media/vortex/LaCie/LaCie/ECO_COUNTRIES/CHIRPS_3857/"

    # WARP
    process_tifs_warp(input_path, output_path)
    process_tifs_warp(input_path + "/MEAN", output_path + "/CHIRPS_AVG")
    process_tifs_warp(input_path + "/ANOMALY", output_path + "/CHIRPS_ANOMALY")
    process_tifs_warp(input_path + "/ZSCORES", output_path + "/CHIRPS_ZSCORE")

    # translate + gdaladdo
    input_path = "/media/vortex/LaCie/LaCie/ECO_COUNTRIES/CHIRPS_3857"
    output_path = "/media/vortex/LaCie/LaCie/ECO_COUNTRIES/CHIRPS/"
    process_tifs_translate(input_path, output_path)
    process_tifs_translate(input_path + "/CHIRPS_AVG", output_path + "/CHIRPS_AVG")
    process_tifs_translate(input_path + "/CHIRPS_ANOMALY", output_path + "/CHIRPS_ANOMALY")
    process_tifs_translate(input_path + "/CHIRPS_ZSCORE", output_path + "/CHIRPS_ZSCORE")

process_chirps()
