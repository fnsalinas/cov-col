# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 08:53:46 2020

@author: fsalinas
"""

import pandas as pd
from datetime import datetime as dt
from sodapy import Socrata
import os

principal_path = r'H:\github\cov-col'
os.chdir(principal_path)

def getCovidData(limit = 3000000):
    api_token = r'2i1q8riwhl18w3bdeogeph7a0'
    api_secretkey = r'54cvecvip76jrrpox1g9m4xcj2zqk0zw57vkf1cf2fixhnlqb8'
    
    app_token = r'OpRCtKHXAFQJANoSy1aRfevWv'
    app_token_secret = r'jsbkBmq1ybXiRWxQLfA1aVk8YFt8v3CuZV08'
    
    client = Socrata('www.datos.gov.co',
                     app_token,
                     username="fabio.salinas@sbseguros.co",
                     password="Aadd4455+")
    
    print('{} Loading Data...'.format(str(dt.now()).split('.')[0]))
    results = client.get("gt2j-8ykr", limit = limit)
    
    print('{} building Pandas Data Frame...'.format(str(dt.now()).split('.')[0]))
    df = pd.DataFrame.from_records(results)
    del(results)
    
    tstamp = str(dt.now()).replace('-','').replace(':','').\
        replace(' ','_').split('.')[0]
    f = r'data/{}_datos_abiertos.csv'.format(tstamp)
    
    print('{} Exporting Data to {}...'.format(tstamp, f))
    df.to_csv(f, sep='~', encoding='latin1')
    
    print('{} Process Finished...'.format(str(dt.now()).split('.')[0]))
    
    return(df)