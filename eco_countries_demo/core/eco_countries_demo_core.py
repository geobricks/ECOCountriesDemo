import os
import shutil
import copy
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
        self.products = ['MOD13A3']
        self.years = ['2015']
        self.countries = 'eco'
        self.__download('mod13a3')

    def process_ndvi(self):
        self.products = ['MOD13A3']
        self.years = ['2015']
        self.countries = 'eco'
        self.__process('mod13a3')

    def download_mydc11(self):
        self.products = ['MYD11C3']
        self.years = ['2015']
        self.countries = 'eco'
        self.__download('myd11c3')

    def __download(self, product_code):
        if self.products is not None and self.years is not None and self.countries is not None:
            for p in self.products:
                for y in self.years:
                    days = c.list_days(p, y)
                    for d in days:
                        print 'DOWNLOADING ' + p + ' FOR ' + y + ', DAY: ' + d['code']
                        # my_processing = copy.deepcopy(processing)
                        # my_processing[product_code][0]['source_path'] = None
                        # for tmp_out in my_processing[product_code]:
                        #     tmp_out['output_path'] = None
                        # if os.path.isdir(self.root + p + '/' + y + '/' + d['code'] + '/PROCESSED/'):
                        #     shutil.rmtree(self.root + p + '/' + y + '/' + d['code'] + '/PROCESSED/')
                        layers = c.list_layers_countries_subset(p, y, d['code'], self.countries)
                        # for l in layers:
                        #     try:
                        #         my_processing[product_code][0]['source_path'].append(self.root + p + '/' + y + '/' + d['code'] + '/' + l['file_name'])
                        #     except Exception:
                        #         my_processing[product_code][0]['source_path'] = []
                        #         my_processing[product_code][0]['source_path'].append(self.root + p + '/' + y + '/' + d['code'] + '/' + l['file_name'])
                        # for tmp_out in my_processing[product_code]:
                        #     print '!!! OUTPUT PATH: ' + self.root + p + '/' + y + '/' + d['code'] + '/PROCESSED/'
                        #     tmp_out['output_path'] = self.root + p + '/' + y + '/' + d['code'] + '/PROCESSED/'
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
                        # print 'Start my_processing...'
                        # try:
                        #     print '##################################################'
                        #     print '#                                                #'
                        #     print '#                                                #'
                        #     print '#                                                #'
                        #     for s in my_processing[product_code][0]['source_path']:
                        #         print '\t' + s
                        #     print '#                                                #'
                        #     print '#                                                #'
                        #     print '#                                                #'
                        #     print '##################################################'
                        #     for proc in my_processing[product_code]:
                        #         # processed_files = my_processing.process_data(my_processing[product_code])
                        #         print proc
                        #         proc["source_path"] = proc["source_path"] if "source_path" in proc else result
                        #         result = processing_core.process_obj(proc)
                        #         print result
                        #     # processed_files = my_processing.process_data(processing[product_code])
                        # except Exception, e:
                        #     print '##################################################'
                        #     print e
                        #     print '##################################################'
                        # print 'Processing done.'
        else:
            if self.products is None:
                raise Exception('Please provide a valid "products" array.')
            if self.years is None:
                raise Exception('Please provide a valid "years" array.')
            if self.countries is None:
                raise Exception('Please provide a valid "countries" comma separated string.')

    def __process(self, product_code):
        if self.products is not None and self.years is not None and self.countries is not None:
            for p in self.products:
                for y in self.years:
                    days = c.list_days(p, y)
                    for d in days:
                        my_processing = copy.deepcopy(processing)
                        my_processing[product_code][0]['source_path'] = None
                        for tmp_out in my_processing[product_code]:
                            tmp_out['output_path'] = None
                        if os.path.isdir(self.root + p + '/' + y + '/' + d['code'] + '/PROCESSED/'):
                            shutil.rmtree(self.root + p + '/' + y + '/' + d['code'] + '/PROCESSED/')
                        layers = c.list_layers_countries_subset(p, y, d['code'], self.countries)
                        for l in layers:
                            try:
                                my_processing[product_code][0]['source_path'].append(self.root + p + '/' + y + '/' + d['code'] + '/' + l['file_name'])
                            except Exception:
                                my_processing[product_code][0]['source_path'] = []
                                my_processing[product_code][0]['source_path'].append(self.root + p + '/' + y + '/' + d['code'] + '/' + l['file_name'])
                        for tmp_out in my_processing[product_code]:
                            print '!!! OUTPUT PATH: ' + self.root + p + '/' + y + '/' + d['code'] + '/PROCESSED/'
                            tmp_out['output_path'] = self.root + p + '/' + y + '/' + d['code'] + '/PROCESSED/'
                        try:
                            for proc in my_processing[product_code]:
                                proc["source_path"] = proc["source_path"] if "source_path" in proc else result
                                result = processing_core.process_obj(proc)
                                print result
                        except Exception, e:
                            print '##################################################'
                            print e
                            print '##################################################'
                        print 'Processing done.'
        else:
            if self.products is None:
                raise Exception('Please provide a valid "products" array.')
            if self.years is None:
                raise Exception('Please provide a valid "years" array.')
            if self.countries is None:
                raise Exception('Please provide a valid "countries" comma separated string.')



dwld = ECOCountriesDownloader()
# dwld.download_ndvi()
dwld.process_ndvi()
# dwld.download_mydc11()