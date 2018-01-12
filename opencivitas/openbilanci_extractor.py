#!/bin/python

import urllib.request, json
import numpy as np
import pandas as pd
import logging

from random import randint
from time import sleep


def init_logger():
    # create logger
    logger = logging.getLogger('openbilanci-extractor')
    logger.setLevel(logging.DEBUG)

    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    # create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # add formatter to ch
    ch.setFormatter(formatter)

    # add ch to logger
    logger.addHandler(ch)
    return logger


def extract_data(df, logger, start_point=0):
    d_types = ['entrate', 'spese']
    base_url = 'https://www.openbilanci.it/armonizzati/bilanci/%s-comune-%s/%s/dettaglio.json?year=2016&type=preventivo'

    missed_urls = []

    i = 0
    logger.info('extracting %d from opencivitas dataset' % df.shape[0])
    for r in df.iloc[start_point:, :].values:
        cod, city, year, province = r
        try:
            if type(city) == str and type(province) == str:
                city = city.lower().replace(' ', '-')
                province = province.lower()
                city_url = base_url % (city, province, d_types[0])

                filename = './data/bilanci/%s_%s.json' % (cod, city)

                try:
                    sleep(randint(1, 10))
                    i += 1
                    logger.info('processing url %s', city_url)
                    with urllib.request.urlopen(city_url) as url:
                        data = json.loads(url.read().decode())

                        with open(filename, 'w') as o:
                            json.dump(data, o)

                            logger.info('saved data into %s' % filename)

                except Exception as ex:
                    logger.error('error %s for url %s' % (ex, city_url))
                    missed_urls.append(city_url)
            else:
                logger.error('error processing record cod=%s, city=%s, province=%s' % (cod, city, province))
        except Exception as ex:
            logger.error('error %s processing record cod=%s, city=%s, province=%s' % (ex, cod, city, province))
            logger.error('finished at line %d' % i)

    logger.info("finished extraction for %d urls" % i)
    with open("./data/bilanci/error_url.txt") as o:
        o.write(','.join(missed_urls))


logger = init_logger()

df_sose = pd.read_csv('./data/opencivitas_spesa_storica_dati_irpef.csv')
columns = ['COMUNE_CAT_COD', 'Denominazione Comune', 'ANNO', 'Sigla Provincia_y']
df = df_sose[columns]
df = df[df['ANNO'] == 2010]

extract_data(df, logger, 720)
