from eco_countries_demo.processing import average_rasterio
from eco_countries_demo.processing import anomalies_rasterio
from eco_countries_demo.processing import variance_rasterio
from eco_countries_demo.processing import standard_deviation_rasterio
from eco_countries_demo.processing import zscore_rasterio


average_rasterio.process_all()
anomalies_rasterio.process_all()
# standard_deviation_rasterio.process_all()
# zscore_rasterio.process_all()