import glob
import os
import subprocess
from geobricks_common.core.filesystem import get_filename




def process_tifs_warp(input_path, output_path, input_ext='*.tif'):
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    files = glob.glob(input_path + "/"+ input_ext)
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


def process(input_path, output_path_warp, output_path_trasnslate, input_ext='*.tif'):
    print input_ext

    # WARP
    if not os.path.exists(output_path_warp):
        os.makedirs(output_path_warp)
    process_tifs_warp(input_path, output_path_warp, input_ext)

    # translate + gdaladdo
    if not os.path.exists(output_path_trasnslate):
        os.makedirs(output_path_trasnslate)
    process_tifs_translate(output_path_warp, output_path_trasnslate)


#Rainfed
# process(
#     '/media/vortex/LaCie/LaCie/ECO_COUNTRIES/original/basic/Rainfed/lrlcofaocrf00_package/',
#     '/media/vortex/LaCie/LaCie/ECO_COUNTRIES/original/3857/basic/Rainfed/',
#     '/media/vortex/LaCie/LaCie/ECO_COUNTRIES/RAINFED/'
#     )

# Population
# process(
#     '/media/vortex/LaCie/LaCie/ECO_COUNTRIES/original/basic/Pop/',
#     '/media/vortex/LaCie/LaCie/ECO_COUNTRIES/original/3857/basic/Pop/',
#     '/media/vortex/LaCie/LaCie/ECO_COUNTRIES/POPULATION/'
# )


# Cultivated Land
# process(
#     '/media/vortex/LaCie/LaCie/ECO_COUNTRIES/original/basic/Cultivated_land/lrlcofaocrp00_package/',
#     '/media/vortex/LaCie/LaCie/ECO_COUNTRIES/original/3857/basic/cultivated_land/',
#     '/media/vortex/LaCie/LaCie/ECO_COUNTRIES/CULTIVATED_LAND/',
# )


# IRRIGATION (ESRI GRID)
# process(
#     '/media/vortex/LaCie/LaCie/ECO_COUNTRIES/original/basic/Irrigation/AREA_EQUIPPED_FOR_IRRIGATION/1_6_AEI_rf/aei_rf/',
#     '/media/vortex/LaCie/LaCie/ECO_COUNTRIES/original/3857/basic/AREA_EQUIPPED_FOR_IRRIGATION/',
#     '/media/vortex/LaCie/LaCie/ECO_COUNTRIES/AREA_EQUIPPED_FOR_IRRIGATION/',
#     'hdr*'
# )