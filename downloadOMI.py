# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 20:22:45 2020
version 1.1.0
@author: punpun Thanyarat Munkong
"""
import requests
import time
from datetime import timedelta, date
# =============================================================================
#change this
year = 2019
start_date = date(2019, 3, 2)
end_date = date(2019, 3, 3) 
# =============================================================================

delta = timedelta(days=1)
urlDaylist = []
while start_date <= end_date:
    urlDaylist.append('http://temis.nl/airpollution/no2col/data/omi/data_v2/%04d/omi_no2_he5_%s.tar' % (year, start_date.strftime("%Y%m%d")))
    start_date += delta
# =============================================================================
for url in urlDaylist:
    local_filename = url.split('/')[-1]
    with requests.get(url, stream=True) as r:
        with open(local_filename, 'wb') as f:
            print("Downloading %s" % local_filename)
            f.write(r.content)
            print("%s done" % local_filename)
    time.sleep(3)
print("All done!")
