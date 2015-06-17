import glob
import os
import rasterio
from eco_countries_demo.processing.utils_rasterio import initialize_rasterio_raster
from eco_countries_demo.processing.utils import get_monthly_layers


def calc_variance(basepath, filename, layers_by_month, epsg="3857"):
    print "-----Variance"

    for month in layers_by_month:
        print month
        output_path = basepath + "/" + filename + "_" + month + "_" + epsg + ".tif"

        data = None
        kwargs = None

        if month == '07':
            print "Processing: ", str(month)
            for f in layers_by_month[month]:
                print "Reading: ",  f
                r = rasterio.open(f)

                if data is None:
                    data, kwargs = initialize_rasterio_raster(r, rasterio.float32)

                band_data = r.read_band(1).astype(float)

                sq = (band_data * band_data)

                # sum of squares
                data = data + sq

            # divide by n-1
            data = data / (len(layers_by_month[month]) - 1)

            # writing
            print "Writing: ", output_path
            with rasterio.open(output_path, 'w', **kwargs) as dst:
                dst.write_band(1, data.astype(rasterio.float32))


def process_all():
    basepath = "/home/vortex/Desktop/LAYERS/ECO_COUNTRIES/MOD13A3"
    layers_by_month = get_monthly_layers(basepath + "/anomalies/*.tif")
    calc_variance(basepath + "/variance", "MOD13A3", layers_by_month)

