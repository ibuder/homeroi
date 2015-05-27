# -*- coding: utf-8 -*-
"""
Created on Thu May 21 15:48:04 2015

@author: ibuder
"""

import requests
import xml.etree.ElementTree as ET
import pandas as pd
import numpy as np

import settings_local


def get_zillow_demographics_one(zip_):
    params = {'zip': zip_, 'zws-id': settings_local.zws_id}
    page = requests.get(
        'http://www.zillow.com/webservice/GetDemographics.htm',
        params=params)
    
    root = ET.fromstring(page.text)
    results = {'zip': zip_}
    results['forSale'] = root.findtext('.//forSale')
    results['medianListPricePerSqFt'] = root.findtext(
        ".//*[name='Median List Price Per Sq Ft']/values/zip/value")
    results['homeValueIndex'] = root.findtext(
        ".//*[name='Zillow Home Value Index']/values/zip/value")
    results['medianSingleFamilyHomeValue'] = root.findtext(
        ".//*[name='Median Single Family Home Value']/values/zip/value")
    return results

sat_schools = pd.io.json.read_json('sat_schools.json', orient='records')
# Zillow has API request limit, so try to minimize calls
zipcodes = np.unique(sat_schools.Zip5)

#FIXME make line below into unit test
#zipcodes = list(zipcodes[0:3]) + [95057]  # testing

zillow_demographics = [get_zillow_demographics_one(zip_) for zip_ in zipcodes]
zillow_demographics = pd.DataFrame(zillow_demographics)
zillow_demographics.to_json('zillow_demographics.json', orient='records')
