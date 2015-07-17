import glob
from geobricks_common.core.filesystem import get_filename
import subprocess

def process_tifs(base_path, output_path):
    files = glob.glob(base_path + "/*.tif")
    for f in files:
        filename = get_filename(f)
        output_file_path = output_path + "/" + filename + ".tif"
        print output_file_path

        # "-multi": "",
        # "-overwrite": "",
        # "-of": "GTiff",
        # "-s_srs": "'+proj=sinu +R=6371007.181 +nadgrids=@null +wktext'",
        # "-t_srs": "EPSG:3857"
        #
        # "a_nodata": "-3000",
        # "-co": "'TILED=YES'",
        # "-co": "'COMPRESS=DEFLATE'"
        #
        cmd = "gdal_translate -a_nodata -3000 -co TILED=YES -co COMPRESS=DEFLATE '" + f + "' '" + output_file_path + "'"
        print cmd
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = process.communicate()




base_path = "/home/vortex/Desktop/LAYERS/ECO_COUNTRIES/MOD13A3/bk"
output_path = "/home/vortex/Desktop/LAYERS/ECO_COUNTRIES/MOD13A3"

process_tifs(base_path, output_path)