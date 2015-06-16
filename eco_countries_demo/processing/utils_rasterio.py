import rasterio
import numpy


def initialize_rasterio_raster(r, nodata=None, parameters=None):
    data = numpy.zeros(r.shape, dtype=rasterio.uint16)
    kwargs = r.meta
    kwargs.update(
        dtype=rasterio.uint16,
        count=1,
        #nodata=-3000
    )
    return data, kwargs