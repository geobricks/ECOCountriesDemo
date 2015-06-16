import os
from geobricks_gdal_calc.core.gdal_calc import calc_layers
from eco_countries_demo.processing.utils import get_files


basepath = "/home/vortex/Desktop/LAYERS/ECO_COUNTRIES/MOD13A3/"
files_path = get_files(basepath, 'final.tif')
avg_file_path = os.path.join(basepath, "avg.tif")

# for each file calc the anomalies
for f in files_path:

    # create anomaly file in the folder
    outputfile = os.path.join(os.path.dirname(os.path.realpath(f)), "anomaly.tif")

    # calculation
    result = calc_layers([f, avg_file_path], outputfile, "diff", ['--NoDataValue=-3000'])