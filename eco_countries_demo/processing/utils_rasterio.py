import rasterio
import numpy


def initialize_rasterio_raster(r, dtype, nodata=None, parameters=None):
    data = numpy.zeros(r.shape, dtype=rasterio.uint16)
    kwargs = r.meta
    kwargs.update(
        dtype=dtype,
        count=1,
        compress='lzw'
        #nodata=-3000
    )
    return data, kwargs