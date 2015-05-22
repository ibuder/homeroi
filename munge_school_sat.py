# -*- coding: utf-8 -*-
"""
Created on Tue May 19 12:22:07 2015

@author: ibuder
"""

import numpy as np
import pandas as pd


def zip5(zip):
    return zip[0:5]


def make_float(d):
    try:
        return np.float(d)
    except ValueError:
        return np.NaN

#  sat1314.xls has data on the second sheet (first is a title page)
#  first column is the school code (CDS)
sat = pd.io.excel.read_excel('sat1314.xls', sheetname=1, index_col=0)
sat = sat[sat.RTYPE == u'S']  # only use schools (not districts/counties)
sat['AVGSCR'] = (sat.AVGSCRMATH.map(make_float) +
                    sat.AVGSCRREAD.map(make_float) +
                    sat.AVGSCRWRIT.map(make_float))

#  pubschls.xls first column is the school code (CDS)
schools = pd.io.excel.read_excel('pubschls.xls', index_col=0)

sat_schools = pd.merge(sat[['NUMTSTTAKR', 'AVGSCR']],
                            schools[['School', 'Street', 'City',
                            'Zip', 'State', 'Latitude', 'Longitude']],
                            how='inner',
                            left_index=True, right_index=True)

sat_schools['Zip5'] = sat_schools.Zip.map(zip5)

#FIXME some schools do not have Lat/Long.
sat_schools.to_json('sat_schools.json', orient='records')
