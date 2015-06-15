import os
import shutil
import glob
from geobricks_modis.core import modis_core as c
from geobricks_processing.core import processing_core
from geobricks_downloader.core.downloader_core import Downloader
from eco_countries_demo.config.processing_config import processing


class ECOCountriesDownloader:

    years = None
    products = None
    countries = None
    root = '/home/kalimaha/Desktop/'

    def __init__(self):
        pass

    def download_ndvi(self):
        self.products = ['MOD13A2']
        self.years = ['2015']
        self.countries = 'eco'
        self.__download('mod13a2')

    def download_mydc11(self):
        self.products = ['MYD11C1']
        self.years = ['2015', '2014']
        self.countries = 'af,az,ir,kz,kg,pk,tj,tr,tm,uz'
        self.__download('myd11c1')

    def __download(self, product_code):
        if self.products is not None and self.years is not None and self.countries is not None:
            for p in self.products:
                for y in self.years:
                    days = c.list_days(p, y)

                    for d in days:

                        processing[product_code][0]['source_path'] = None
                        if os.path.isdir(self.root + p + '/' + y + '/' + d['code'] + '/PROCESSED/'):
                            shutil.rmtree(self.root + p + '/' + y + '/' + d['code'] + '/PROCESSED/')

                        layers = c.list_layers_countries_subset(p, y, d['code'], self.countries)

                        for l in layers:
                            try:
                                processing[product_code][0]['source_path'].append(self.root + p + '/' + y + '/' + d['code'] + '/' + l['file_name'])
                            except Exception:
                                processing[product_code][0]['source_path'] = []
                                processing[product_code][0]['source_path'].append(self.root + p + '/' + y + '/' + d['code'] + '/' + l['file_name'])
                        for tmp_out in processing[product_code]:
                            tmp_out['output_path'] = self.root + p + '/' + y + '/' + d['code'] + '/PROCESSED/'

                        my_downloader = Downloader('modis',
                                                   self.root,
                                                   {'product': p, 'year': y, 'day': d['code']},
                                                   layers,
                                                   True)
                        my_downloader.download()
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
                        processed_files = processing_core.process_data(processing[product_code])
                        print processed_files
                        print processed_files
                        for f in glob.glob(self.root + p + '/' + y + '/' + d['code'] + '/PROCESSED/*'):
                            if 'final.tif' not in f:
                                os.remove(f)
                        print 'Processing done.'

            # for p in self.products:
            #     for y in self.years:
            #         days = [{'code': '001'}]
            #         for d in days:
            #             layers = c.list_layers_countries_subset(p, y, d['code'], self.countries)
            #             for l in layers:
            #                 try:
            #                     processing['mod13a2'][0]['source_path'].append('/home/kalimaha/Desktop/' + p + '/' + y + '/' + d['code'] + '/' + l['file_name'])
            #                 except Exception:
            #                     processing['mod13a2'][0]['source_path'] = []
            #                     processing['mod13a2'][0]['source_path'].append('/home/kalimaha/Desktop/' + p + '/' + y + '/' + d['code'] + '/' + l['file_name'])
            #             for tmp_out in processing['mod13a2']:
            #                 tmp_out['output_path'] = '/home/kalimaha/Desktop/' + p + '/' + y + '/' + d['code'] + '/PROCESSED/'
            #         print processing['mod13a2'][0]['source_path']
            #         print 'Start processing...'
            #         processed_files = processing_core.process_data(processing['mod13a2'])
            #         print processed_files
            #         print 'Processing done.'
        else:
            if self.products is None:
                raise Exception('Please provide a valid "products" array.')
            if self.years is None:
                raise Exception('Please provide a valid "years" array.')
            if self.countries is None:
                raise Exception('Please provide a valid "countries" comma separated string.')



dwld = ECOCountriesDownloader()
dwld.download_ndvi()