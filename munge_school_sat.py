# -*- coding: utf-8 -*-
"""
Created on Tue May 19 12:22:07 2015

@author: ibuder
"""

import pandas as pd


#  sat1314.xls has data on the second sheet (first is a title page)
#  first column is the school code (CDS)
sat = pd.io.excel.read_excel('sat1314.xls', sheetname=1, index_col=0)

#  pubschls.xls first column is the school code (CDS)
schools = pd.io.excel.read_excel('pubschls.xls', index_col=0)

sat_schools = pd.merge(sat[['RTYPE', 'NUMTSTTAKR', 'AVGSCRREAD',
                            'AVGSCRMATH', 'AVGSCRWRIT']],
                            schools[['School', 'Street', 'City',
                            'Zip', 'State', 'Latitude', 'Longitude']],
                            how='inner',
                            left_index=True, right_index=True)

#FIXME some schools do not have Lat/Long.
sat_schools.to_json('sat_schools.json', orient='records')