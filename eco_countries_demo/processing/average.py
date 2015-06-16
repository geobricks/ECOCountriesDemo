from geobricks_gdal_calc.core.gdal_calc import calc_layers
from eco_countries_demo.processing.utils import get_files


basepath = "/home/vortex/Desktop/LAYERS/ECO_COUNTRIES/MOD13A3/"
outputfile = "/home/vortex/Desktop/LAYERS/ECO_COUNTRIES/MOD13A3/avg.tif"
files_path = get_files(basepath, 'final.tif')

# calculation
result = calc_layers(files_path, outputfile, "avg", ['--NoDataValue=-3000'])

