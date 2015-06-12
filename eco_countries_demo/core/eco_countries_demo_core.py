from geobricks_modis.core import modis_core as c
from geobricks_processing.core import processing_core
from geobricks_downloader.core.downloader_core import Downloader
from eco_countries_demo.config.processing_config import processing


layers = c.list_layers_countries_subset('MYD11C1', '2015', '001', 'af')
my_downloader = Downloader('modis',
                           '/home/kalimaha/Desktop',
                           {'product': 'MYD11C1', 'year': '2015', 'day': '001'},
                           layers,
                           True)
downloaded_layers = my_downloader.download()['downloaded_files']
processing[0]['source_path'] = ['/home/kalimaha/Desktop/MYD11C1/2015/001/' + layers[0]['file_name']]
processing[0]['output_path'] = '/home/kalimaha/Desktop/MYD11C1/2015/001/PROCESSED/'
download_in_progress = True
while download_in_progress:
    try:
        current = my_downloader.progress(layers[0]['file_name'])['download_size']
        total = my_downloader.progress(layers[0]['file_name'])['total_size']
        download_in_progress = current != total
    except TypeError, e:
        pass
    except KeyError:
        pass
print 'Layer downloaded.'
print 'Start processing...'
processed_files = processing_core.process_data(processing)
print 'Processing done.'