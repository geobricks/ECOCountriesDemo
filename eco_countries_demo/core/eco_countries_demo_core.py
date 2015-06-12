from geobricks_modis.core import modis_core as c
from geobricks_processing.core import processing_core
from geobricks_downloader.core.downloader_core import Downloader
from eco_countries_demo.config.processing_config import processing


class ECOCountriesDownloader:

    products = ['MYD11C1']
    years = ['2015', '2014']
    countries = 'af,az,ir,kz,kg,pk,tj,tr,tm,uz'

    def __init__(self):
        for p in self.products:
            for y in self.years:
                days = c.list_days(p, y)
                for d in days:
                    layers = c.list_layers_countries_subset(p, y, d['code'], self.countries)
                    my_downloader = Downloader('modis',
                                               '/home/kalimaha/Desktop',
                                               {'product': p, 'year': y, 'day': d['code']},
                                               layers,
                                               True)
                    downloaded_layers = my_downloader.download()['downloaded_files']
                    processing[0]['source_path'] = ['/home/kalimaha/Desktop/' + p + '/' + y + '/' + d['code'] + '/' + layers[0]['file_name']]
                    processing[0]['output_path'] = '/home/kalimaha/Desktop/' + p + '/' + y + '/' + d['code'] + '/PROCESSED/'
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
                    print processed_files
                    print 'Processing done.'



dwld = ECOCountriesDownloader()