# -*- coding: utf-8 -*-
"""
Created on Fri May 22 10:52:53 2015

@author: ibuder
"""

import pandas as pd

sat_schools = pd.io.json.read_json('sat_schools.json', orient='records')
zillow_demographics = pd.io.json.read_json('zillow_demographics.json',
                                           orient='records')
sat_schools_zillow = pd.merge(sat_schools, zillow_demographics, how='left',
                              left_on='Zip5', right_on='zip')
del sat_schools_zillow['zip']
sat_schools_zillow.to_json('sat_schools_zillow.json', orient='records')
