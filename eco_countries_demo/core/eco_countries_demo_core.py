from geobricks_modis.core import modis_core as c
from geobricks_processing.core import processing_core
from geobricks_downloader.core.downloader_core import Downloader


processing = [
    {
        "band": 1,
        "process": [
            {
                "extract_bands": ""
            }
        ]
    },
    {
        "band": 1,
        "output_file_name": "merge",
        "process": [
            {
                "gdal_merge": {
                    "prefix": "gdal_merge_",
                    "extension": "tif"
                }
            }
        ]
    },
    {
        "band": 1,
        "output_file_name": "final",
        "process": [
            {
                "get_pixel_size" : "{{PIXEL_SIZE}}"
            },
            {
                "gdalwarp": {
                    "opt": {
                        "-multi": "",
                        "-overwrite": "",
                        "-of": "GTiff",
                        "-s_srs": "'+proj=sinu +R=6371007.181 +nadgrids=@null +wktext'",
                        "-co": "'TILED=YES'",
                        "-t_srs": "EPSG:3857",
                        "-srcnodata": -3000,
                        "-dstnodata": -3000
                    },
                    "prefix": "gdalwarp_",
                    "extension": "tif"
                }
            }
        ]
    },
    {
        "band": 1,
        "process": [
            {
                "gdaladdo": {
                    "parameters": {
                        "-r": "average"
                    },
                    "overviews_levels": "2 4 8 16"
                }
            }
        ]
    }
]

layers = c.list_layers_countries_subset('MYD11C1', '2015', '001', 'af')
my_downloader = Downloader('modis',
                           '/home/kalimaha/Desktop',
                           {'product': 'MYD11C1', 'year': '2015', 'day': '001'},
                           layers,
                           True)
downloaded_layers = my_downloader.download()['downloaded_files']
print downloaded_layers
print type(downloaded_layers)
print '/home/kalimaha/Desktop/MYD11C1/2015/001/' + layers[0]['file_name']
processing[0]['source_path'] = ['/home/kalimaha/Desktop/MYD11C1/2015/001/' + layers[0]['file_name']]
processing[0]['output_path'] = '/home/kalimaha/Desktop/MYD11C1/2015/001/PROCESSED/'
print processing
download_in_progress = True
while download_in_progress:
    try:
        current = my_downloader.progress(layers[0]['file_name'])['download_size']
        total = my_downloader.progress(layers[0]['file_name'])['total_size']
        print str(current) + ' VS ' + str(total)
        download_in_progress = current != total
    except TypeError, e:
        print 'TypeError'
        print e
        pass
    except KeyError:
        print 'KeyError'
        pass
print 'Layer downloaded.'
print 'Start processing...'
processed_files = processing_core.process_data(processing)
print 'Processing done.'