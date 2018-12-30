#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pylab as plt

base = pd.read_csv('AirPassengers.csv')
dateFormat = '%Y-%m'
dateparse = lambda dates: pd.datetime.strptime(dates, dateFormat)
base = pd.read_csv('AirPassengers.csv', parse_dates = ['Month'],
                   index_col = 'Month', date_parser = dateparse)
time_series = base['#Passengers']
                   
plt.plot(time_series)

