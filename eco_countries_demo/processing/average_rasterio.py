import glob
import os
import rasterio
import numpy
from eco_countries_demo.processing.utils_rasterio import initialize_rasterio_raster
from geobricks_common.core.filesystem import get_filename
from eco_countries_demo.processing.utils import get_monthly_layers
from geobricks_gdal_calc.core.gdal_calc import calc_layers
from eco_countries_demo.processing.utils import get_files


basepath = "/home/vortex/Desktop/LAYERS/ECO_COUNTRIES/MOD13A3"

def calc_monthly_average(basepath, filename, layers_by_month, epsg="3857"):
    print layers_by_month

    for month in layers_by_month:
        output_path = basepath + "/" + filename + "_" + month + "_" + epsg + "_rasterio.tif"

        data = None
        kwargs = None

        print "Processing: ", str(month)
        for f in layers_by_month[month]:
            print "Reading: ",  f
            r = rasterio.open(f)

            if data is None:
                data, kwargs = initialize_rasterio_raster(r)

            data += r.read_band(1)

        data / len(layers_by_month[month])

        # writing
        print "Writing: ", output_path
        with rasterio.open(output_path, 'w', **kwargs) as dst:
            dst.write_band(1, data.astype(rasterio.uint16))






layers_by_month = get_monthly_layers(basepath + "/*.tif")
calc_monthly_average(basepath + "/avg", "MOD13A3", layers_by_month)






# calculation
# result = calc_layers(files_path, outputfile, "avg", ['--NoDataValue=-3000'])



