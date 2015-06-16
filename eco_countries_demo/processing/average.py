import glob
import os
from geobricks_common.core.filesystem import get_filename
from eco_countries_demo.processing.utils import get_monthly_layers
from geobricks_gdal_calc.core.gdal_calc import calc_layers
from eco_countries_demo.processing.utils import get_files


basepath = "/home/vortex/Desktop/LAYERS/ECO_COUNTRIES/MOD13A3"



def calc_monthly_average(basepath, filename, layers_by_month, epsg="3857"):
    print layers_by_month

    for month in layers_by_month:
        output_path = basepath + "/" + filename + "_" + month + "_" + epsg + ".tif"
        result = calc_layers(layers_by_month[month], output_path, "avg", ['--NoDataValue=-3000'])
        print result





layers_by_month = get_monthly_layers(basepath + "/*.tif")
calc_monthly_average(basepath + "/avg", "MOD13A3", layers_by_month)






# calculation
# result = calc_layers(files_path, outputfile, "avg", ['--NoDataValue=-3000'])



