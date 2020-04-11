from sickle import Sickle
from datetime import date, datetime
import pickle

URL = 'http://export.arxiv.org/oai2'
sickle = Sickle(URL)
records = records = sickle.ListRecords(
             **{'metadataPrefix': 'oai_dc',
             'from': '2015-01-01',
             'ignore_deleted':True
            })

date_list, record_list = [], []
for record in records:
    year, month, day = record.header.datestamp.split('-')
    year, month, day = int(year), int(month), int(day)
    d = date(year, month, day)
    date_list.append(d)
    record_list.append(record)

with open('date_list.pkl', "wb") as f:
    pickle.dump(date_list, f)

with open('record_list.pkl', "wb") as f:
    pickle.dump(record_list, f)

from collections import Counter
import numpy as np 
import datetime
import pickle

with open("date_list.pkl", "rb") as f:
    date_list = pickle.load(f)

datetime_list = [datetime.datetime.combine(dt, datetime.time.min) for dt in date_list]
dcounts = Counter(d for d in datetime_list)
date_list, count_list = [], []
for d, count in dcounts.items():
    date_list.append(d)
    count_list.append(count)

date_list, count_list = zip(*sorted(zip(date_list, count_list), key=lambda x: x[0]))