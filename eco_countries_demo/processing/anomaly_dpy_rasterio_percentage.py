import glob
import rasterio
from geobricks_common.core.filesystem import get_filename
from eco_countries_demo.processing.utils_rasterio import initialize_rasterio_raster
from eco_countries_demo.processing.utils import get_month_by_filename, get_year_by_filename, get_base_filename
import numpy


def calc(basepath, output_path, layers, epsg="3857"):
    print "-----Anomaly DPY"


    for layer in layers:
        # print get_year_by_filename(layer)
        year = get_year_by_filename(layer)

        data = None
        month = get_month_by_filename(layer)
        filename = get_filename(layer)
        base_filename = get_base_filename(filename)
        yearPrev = str(int(year) - 1)

        layerPrev = basepath + "/" + base_filename + "_" + yearPrev + month + "_" + epsg + ".tif"

        print "Processing: ", layer, layerPrev

        print "Reading: ",  layer
        r = rasterio.open(layer)
        r_data = r.read_band(1).astype(float)

        print "Reading: ",  layerPrev
        r_prev = rasterio.open(layerPrev)
        r_prev_data = r_prev.read_band(1).astype(float)

        if data is None:
            data, kwargs = initialize_rasterio_raster(r, rasterio.float32)


        data = ((r_data - r_prev_data) / r_prev_data) * 100

        # writing
        output_layer_path = output_path + "/" + filename + ".tif"
        print "Writing: ", output_layer_path
        with rasterio.open(output_layer_path, 'w', **kwargs) as dst:
            dst.write_band(1, data.astype(rasterio.float32))



def process_all():
    basepath = "/media/vortex/LaCie/LaCie/ECO_COUNTRIES/MYD11C3"
    output_path = basepath + "/MYD11C3_ANOMALY_DPY"
    layers = glob.glob(basepath + "/*.tif")
    calc(basepath, output_path, layers)

    #
    # basepath = "/media/vortex/LaCie/LaCie/ECO_COUNTRIES/MOD16/ET/ET"
    # output_path = basepath + "/ET_ANOMALY_DPY/original/"
    # layers = glob.glob(basepath + "/*.tif")
    # calc(basepath, output_path, layers)

    # basepath = "/media/vortex/LaCie/LaCie/ECO_COUNTRIES/CHIRPS"
    # output_path = basepath + "/CHIRPS_ANOMALY_DPY/original/"
    # layers = glob.glob(basepath + "/*.tif")
    # calc(basepath, output_path, layers)

    # basepath = "/media/vortex/LaCie/LaCie/ECO_COUNTRIES/MOD13A3"
    # output_path = basepath + "/MOD13A3_ANOMALY_DPY/original"
    # layers = glob.glob(basepath + "/*.tif")
    # calc(basepath, output_path, layers)






process_all()