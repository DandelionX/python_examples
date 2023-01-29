

import os
import datetime
import pandas as pd
import code

year = 2019
# ---------------------------------------------
dt_start = datetime.datetime(year, 4, 27)
dt_end = datetime.datetime(year, 5, 5)
period = pd.date_range(start=dt_start, end=dt_end, freq='D', closed='left')  # 这里pandas的版本是1.3.5
# period = pd.date_range(start=dt_start, end=dt_end, freq='D', inclusive='left')  # 版本问题1.4.0以上用inclusive
# -------------OBS----------------------------
for p in period:
    YY = str(p.year)
    MM = str(p.month).zfill(2)
    DD = str(p.day).zfill(2)
    os.makedirs('./FileMakeDir/' + str(year) + '/' + YY + MM + DD)

code.interact(local=locals())
# period = pd.date_range(start=dt_start, end=dt_end, freq='H', closed='both')
# period = pd.date_range(start=dt_start, end=dt_end, freq='5H', closed='both')


'''
pd.date_range
https://pandas.pydata.org/docs/reference/api/pandas.date_range.html
'''




















