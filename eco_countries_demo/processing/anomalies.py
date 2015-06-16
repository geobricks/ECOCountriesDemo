import os
from geobricks_common.core.filesystem import get_filename
from geobricks_gdal_calc.core.gdal_calc import calc_layers
from eco_countries_demo.processing.utils import get_files


basepath = "/home/vortex/Desktop/LAYERS/ECO_COUNTRIES/MOD13A3"
files_path = get_files(basepath + "/*.tif")
avg_file_path = basepath + "/avg/MOD13A3_avg.tif"

# for each file calc the anomalies
for f in files_path:

    filename = get_filename(f)
    s = filename.split("_")
    date = s[len(s)-2]

    # create anomaly file in the folder
    output_path = os.path.join(os.path.dirname(os.path.realpath(f)), "anomalies", "MOD13A3_anomalies_" + date + "_3857.tif")

    # calculation
    result = calc_layers([f, avg_file_path], output_path, "diff", ['--NoDataValue=-3000'])