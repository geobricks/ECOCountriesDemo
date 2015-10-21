import glob
import os
import subprocess
from geobricks_common.core.filesystem import get_filename




def process_tifs_warp(input_path, output_path):
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    files = glob.glob(input_path + "/*.tiff")
    print files
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

        add_gdaladdo(output_file_path)

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


def process_mod11c3():
    # input_path = "/media/vortex/LaCie/LaCie/ECO_COUNTRIES/MYD11C3_4326/"
    # output_path = "/media/vortex/LaCie/LaCie/ECO_COUNTRIES/MYD11C3/"
    # process_tifs_warp(input_path, output_path)
    #
    # input_path = "/media/vortex/LaCie/LaCie/ECO_COUNTRIES/MYD11C3_4326/MYD11C3_ANOMALY"
    # output_path = "/media/vortex/LaCie/LaCie/ECO_COUNTRIES/MYD11C3/MYD11C3_ANOMALY"
    # process_tifs_warp(input_path, output_path)
    #
    # input_path = "/media/vortex/LaCie/LaCie/ECO_COUNTRIES/MYD11C3_4326/MYD11C3_AVG"
    # output_path = "/media/vortex/LaCie/LaCie/ECO_COUNTRIES/MYD11C3/MYD11C3_AVG"
    # process_tifs_warp(input_path, output_path)
    #
    # input_path = "/media/vortex/LaCie/LaCie/ECO_COUNTRIES/MYD11C3_4326/MYD11C3_ZSCORE"
    # output_path = "/media/vortex/LaCie/LaCie/ECO_COUNTRIES/MYD11C3/MYD11C3_ZSCORE"
    # process_tifs_warp(input_path, output_path)
    #
    # input_path = "/media/vortex/LaCie/LaCie/ECO_COUNTRIES/MYD11C3_4326/MYD11C3_SD"
    # output_path = "/media/vortex/LaCie/LaCie/ECO_COUNTRIES/MYD11C3/MYD11C3_SD"
    # process_tifs_warp(input_path, output_path)

    print "here"
    input_path = "/media/vortex/LaCie/LaCie/ECO_COUNTRIES/CHIRPS/MONTHLY/data/"
    output_path = "/media/vortex/LaCie/LaCie/ECO_COUNTRIES/CHIRPS/MONTHLY/data/output/"
    process_tifs_warp(input_path, output_path)



def process_mod16():
    input_path = "/media/vortex/LaCie/LaCie/ECO_COUNTRIES/MOD16_bk/ET/ET/"
    output_path = "/media/vortex/LaCie/LaCie/ECO_COUNTRIES/MOD16/ET/ET/"
    process_tifs_translate(input_path, output_path)

    input_path = "/media/vortex/LaCie/LaCie/ECO_COUNTRIES/MOD16_bk/ET/ET/ET_ANOMALY"
    output_path = "/media/vortex/LaCie/LaCie/ECO_COUNTRIES/MOD16/ET/ET/ET_ANOMALY"
    process_tifs_translate(input_path, output_path)

    input_path = "/media/vortex/LaCie/LaCie/ECO_COUNTRIES/MOD16_bk/ET/ET/ET_AVG"
    output_path = "/media/vortex/LaCie/LaCie/ECO_COUNTRIES/MOD16/ET/ET/ET_AVG"
    process_tifs_translate(input_path, output_path)

    input_path = "/media/vortex/LaCie/LaCie/ECO_COUNTRIES/MOD16_bk/ET/ET/ET_ZSCORE"
    output_path = "/media/vortex/LaCie/LaCie/ECO_COUNTRIES/MOD16/ET/ET/ET_ZSCORE"
    process_tifs_translate(input_path, output_path)



def process_MOD13A3():
    input_path = "/media/vortex/LaCie/LaCie/ECO_COUNTRIES/MOD13A3/MOD13A3_ZSCORE/original//"
    output_path = "/media/vortex/LaCie/LaCie/ECO_COUNTRIES/MOD13A3/MOD13A3_ZSCORE/"
    process_tifs_translate(input_path, output_path)

    input_path = "/media/vortex/LaCie/LaCie/ECO_COUNTRIES/MOD13A3_bk/MOD13A3_ANOMALY"
    output_path = "/media/vortex/LaCie/LaCie/ECO_COUNTRIES/MOD13A3/MOD13A3_ANOMALY"
    process_tifs_translate(input_path, output_path)

    input_path = "/media/vortex/LaCie/LaCie/ECO_COUNTRIES/MOD13A3_bk/MOD13A3_AVG"
    output_path = "/media/vortex/LaCie/LaCie/ECO_COUNTRIES/MOD13A3/MOD13A3_AVG"
    process_tifs_translate(input_path, output_path)


def process_wheat_hs():
    input_path = "/media/vortex/LaCie/LaCie/ECO_COUNTRIES/HOT_SPOT_ANALYSIS/WHEAT_AREA_AFG/original/"
    output_path = "/media/vortex/LaCie/LaCie/ECO_COUNTRIES/HOT_SPOT_ANALYSIS/WHEAT_AREA_AFG/"
    process_tifs_translate(input_path, output_path)

    input_path = "/media/vortex/LaCie/LaCie/ECO_COUNTRIES/HOT_SPOT_ANALYSIS/DROUGHT_HOTPOST_AFG/original/"
    output_path = "/media/vortex/LaCie/LaCie/ECO_COUNTRIES/HOT_SPOT_ANALYSIS/DROUGHT_HOTPOST_AFG/"
    process_tifs_translate(input_path, output_path)



process_mod11c3()
# process_MOD13A3()
# process_mod16()
#process_wheat_hs()
