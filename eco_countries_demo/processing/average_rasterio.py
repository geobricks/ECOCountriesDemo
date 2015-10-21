import rasterio
import os
from eco_countries_demo.processing.utils_rasterio import initialize_rasterio_raster
from eco_countries_demo.processing.utils import get_monthly_layers


def calc_monthly_average(basepath, filename, layers_by_month, epsg="3857"):
    print "-----Averages"

    if not os.path.exists(basepath):
        os.makedirs(basepath)

    for month in layers_by_month:
        output_path = basepath + "/" + filename + "_" + month + "_" + epsg + ".tif"

        data = None
        kwargs = None

        print "Processing: ", str(month)
        for f in layers_by_month[month]:
            print "Reading: ",  f
            r = rasterio.open(f)

            if data is None:
                data, kwargs = initialize_rasterio_raster(r, rasterio.float32)

            data = data + r.read_band(1).astype(float)


        data = data / len(layers_by_month[month])

        # writing
        print "Writing: ", output_path
        with rasterio.open(output_path, 'w', **kwargs) as dst:
            dst.write_band(1, data.astype(rasterio.float32))


def process_all():
    basepath = "/media/vortex/LaCie/LaCie/ECO_COUNTRIES/CHIRPS/"
    layers_by_month = get_monthly_layers(basepath + "/*.tif")
    calc_monthly_average(basepath + "/avg", "CHIRPS", layers_by_month)


# process_all()