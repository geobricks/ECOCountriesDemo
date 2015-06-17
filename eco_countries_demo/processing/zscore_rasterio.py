import glob
import os
import rasterio
from geobricks_common.core.filesystem import get_filename
from eco_countries_demo.processing.utils_rasterio import initialize_rasterio_raster
from eco_countries_demo.processing.utils import get_date_by_filename

# the calc is of the zscore is = avg / variance

def calc(basepath, filename, epsg="3857"):
    print "-----ZSCORE"

    layers_avg = glob.glob(basepath + "/avg/*.tif")
    #layers_variance = glob.glob(basepath + "/variance/*.tif")
    layers_variance = glob.glob(basepath + "/sd/*.tif")

    for layer_avg in layers_avg:

        month_avg = get_date_by_filename(layer_avg)
        layer_variance = get_layer_variance_by_month(layers_variance, month_avg)

        if month_avg == '07':
            print "Processing: ", str(month_avg)
            print "Reading: ",  layer_avg
            r_avg = rasterio.open(layer_avg)
            print "Reading: ",  layer_variance
            r_variance = rasterio.open(layer_variance)

            data, kwargs = initialize_rasterio_raster(r_avg, rasterio.float32)

            r_avg_band_data = r_avg.read_band(1).astype(float)
            r_variance_band_data = r_variance.read_band(1).astype(float)

            data = r_avg_band_data / r_variance_band_data

            # writing
            filename = get_filename(layer_avg)
            output_path = basepath + "/zscore/" + filename + ".tif"
            print "Writing: ", output_path
            with rasterio.open(output_path, 'w', **kwargs) as dst:
                dst.write_band(1, data.astype(rasterio.float32))


def get_layer_variance_by_month(layers, month):
    for l in layers:
        if month == get_date_by_filename(l):
            return l

def process_all():
    basepath = "/home/vortex/Desktop/LAYERS/ECO_COUNTRIES/MOD13A3"
    calc(basepath, "MOD13A3")

#process_all()
