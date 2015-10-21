import glob
import os
import subprocess
from geobricks_common.core.filesystem import get_filename



def process_tifs_translate(input_path, output_path, base_str, replace_str):
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    files = glob.glob(input_path + "/*.tif")
    for f in files:
        filename = get_filename(f)
        output_file_path = output_path + "/" + filename.replace(base_str, replace_str) + ".tif"
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


def process():


    # input_path = "/media/vortex/LaCie/LaCie/ECO_COUNTRIES/MYD11C3/MYD11C3_ANOMALY_DPY/original"
    # output_path = "/media/vortex/LaCie/LaCie/ECO_COUNTRIES/MYD11C3/MYD11C3_ANOMALY_DPY"
    # process_tifs_translate(input_path, output_path, 'LST_', 'LST_Anomaly_DPY_')
    #
    # input_path = "/media/vortex/LaCie/LaCie/ECO_COUNTRIES/MOD16/ET/ET/ET_ANOMALY_DPY/original"
    # output_path = "/media/vortex/LaCie/LaCie/ECO_COUNTRIES/MOD16/ET/ET/ET_ANOMALY_DPY"
    # process_tifs_translate(input_path, output_path, 'ET_', 'ET_Anomaly_DPY_')

    input_path = "/media/vortex/LaCie/LaCie/ECO_COUNTRIES/CHIRPS/CHIRPS_ANOMALY_DPY/original"
    output_path = "/media/vortex/LaCie/LaCie/ECO_COUNTRIES/CHIRPS/CHIRPS_ANOMALY_DPY"
    process_tifs_translate(input_path, output_path, 'Rainfall_', 'Rainfall_Anomaly_DPY_')

    # input_path = "/media/vortex/LaCie/LaCie/ECO_COUNTRIES/MOD13A3/MOD13A3_ANOMALY_DPY/original"
    # output_path = "/media/vortex/LaCie/LaCie/ECO_COUNTRIES/MOD13A3/MOD13A3_ANOMALY_DPY"
    # process_tifs_translate(input_path, output_path, 'NDVI_', 'NDVI_Anomaly_DPY_')


process()