import os
import copy
import shutil
import os.path
from geobricks_modis.core import modis_core as c
from geobricks_processing.core import processing_core
from geobricks_common.core.date import day_of_the_year_to_date
from geobricks_downloader.core.downloader_core import Downloader
from eco_countries_demo.config.processing_config import processing


class ECOCountriesDownloader:

    years = None
    products = None
    countries = None
    root = '/home/vortex/Desktop/nena/'

    def __init__(self):
        pass

    def download_ndvi(self):
        self.products = ['MOD13A1']
        self.years = ['2015']
        self.countries = 'za'
        self.__download()

    def process_ndvi(self):
        self.products = ['MOD13A1']
        self.years = ['2015']
        self.countries = 'za'
        self.__process('mod13a1')

    def prepare_output_ndvi(self):
        self.prepare_output('mod13a1')

    def download_mydc13(self):
        self.products = ['MYD11C3']
        self.years = ['2014', '2013', '2012',
                      '2011', '2010', '2009', '2008', '2007', '2006',
                      '2005', '2004', '2003', '2002', '2001', '2000']
        self.countries = 'eco'
        self.__download()

    def process_mydc13(self):
        self.products = ['MYD11C3']
        self.years = ['2014', '2013', '2012',
                      '2011', '2010', '2009', '2008', '2007', '2006',
                      '2005', '2004', '2003', '2002', '2001', '2000']
        self.countries = 'eco'
        self.__process('myd11c3')

    def prepare_output_mydc13(self):
        self.prepare_output('myd11c3')

    def process_mod16(self):
        self.products = ['MOD16']
        self.years = ['2014', '2013', '2012',
                      '2011', '2010', '2009', '2008', '2007', '2006',
                      '2005', '2004', '2003', '2002', '2001', '2000']
        self.countries = 'eco'
        self.__process('mod16')

    def __download(self):
        if self.products is not None and self.years is not None and self.countries is not None:
            for p in self.products:
                for y in self.years:
                    days = c.list_days(p, y)
                    for d in days:
                        print 'DOWNLOADING ' + p + ' FOR ' + y + ', DAY: ' + d['code']
                        layers = c.list_layers_countries_subset(p, y, d['code'], self.countries)
                        my_downloader = Downloader('modis',
                                                   self.root,
                                                   {'product': p, 'year': y, 'day': d['code']},
                                                   layers)
                        my_downloader.download()
                        download_in_progress = True
                        while download_in_progress:
                            try:
                                current = my_downloader.progress(layers[0]['file_name'])['download_size']
                                total = my_downloader.progress(layers[0]['file_name'])['total_size']
                                download_in_progress = current != total
                            except TypeError:
                                pass
                            except KeyError:
                                pass
                        print 'Layer downloaded.'
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
                                my_processing[product_code][0]['source_path'].append(self.root +
                                                                                     p + '/' +
                                                                                     y + '/' +
                                                                                     d['code'] + '/' +
                                                                                     l['file_name'])
                            except AttributeError:
                                my_processing[product_code][0]['source_path'] = []
                                my_processing[product_code][0]['source_path'].append(self.root +
                                                                                     p + '/' +
                                                                                     y + '/' +
                                                                                     d['code'] + '/' +
                                                                                     l['file_name'])
                        for tmp_out in my_processing[product_code]:
                            tmp_out['output_path'] = self.root + p + '/' + y + '/' + d['code'] + '/PROCESSED/'
                        try:
                            for proc in my_processing[product_code]:
                                proc["source_path"] = proc["source_path"] if "source_path" in proc else result
                                result = processing_core.process_obj(proc)
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

    def prepare_output(self, product_code):
        for path, subdirs, files in os.walk(self.root + product_code.upper()):
            for name in files:
                if 'final.tif' in os.path.join(path, name):
                    day = self.get_parent_folder(self.get_parent(os.path.join(path, name)))
                    year = self.get_parent_folder(self.get_parent(self.get_parent(os.path.join(path, name))))
                    d = day_of_the_year_to_date(day, year)
                    date = str(d.year) + '0' + str(d.month)  if d.month < 10 else str(d.year) + str(d.month)
                    prj = '3857'
                    new_name = product_code.upper() + '_' + date + '_' + prj + '.tif'
                    print 'COPYING: ' + os.path.join(path, name) + '...'
                    shutil.copyfile(os.path.join(path, name), os.path.join(self.root, product_code.upper(), new_name))

    def get_parent(self, file_path):
        return os.path.abspath(os.path.join(file_path, os.pardir))

    def get_parent_folder(self, file_path):
        parent_path = self.get_parent(file_path)
        return parent_path[1 + parent_path.rfind('/'):]



dwld = ECOCountriesDownloader()

dwld.download_ndvi()
# dwld.process_ndvi()
#dwld.prepare_output_ndvi()

# dwld.download_mydc13()
# dwld.process_mydc13()
# dwld.prepare_output_mydc13()
