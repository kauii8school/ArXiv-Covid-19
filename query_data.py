from sickle import Sickle
from datetime import date, datetime
import pickle
import os
import time

cwd = os.getcwd()

URL = 'http://export.arxiv.org/oai2'
subject_list = ['physics', 'cs', 'math', 'q-bio', 'q-fin', 'stat']
for subject in subject_list:
    sickle = Sickle(URL)
    fr = '2015-04-04'
    year, month, day = fr.split('-')
    year, month, day = int(year), int(month), int(day)
    fr_dt = date(year, month, day)
    un = '2020-04-30'
    year, month, day = un.split('-')
    year, month, day = int(year), int(month), int(day)
    un_dt = date(year, month, day)

    print(f"Downloading ArXiV metadata from {fr} to {un} for subject:{subject}")

    date_list, author_length_list = [], []
    while True:
        records = sickle.ListRecords(
                    **{'metadataPrefix': 'oai_dc',
                    'from': f'{fr}',
                    'until': f'{un}',
                    'ignore_deleted':False,
                    'set': f'{subject}'
                    })


        for i, record in enumerate(records):
            year, month, day = record.metadata['date'][0].split('-')
            year, month, day = int(year), int(month), int(day)
            d = date(year, month, day)
            if d > fr_dt and d < un_dt:
                date_list.append(d)
                author_length_list.append(len(record.metadata['creator']))

        time.sleep(50)
        try:
            records.next()
        except:
            break

    print(len(date_list))
    if not os.path.exists(f"{cwd}/data/{subject}"):
        os.mkdir(f"{cwd}/data/{subject}")

    with open(f'data/{subject}/date_list.pkl', "rb") as rf:
        read_date_list = pickle.load(rf)
    write_date_list = read_date_list.extend(date_list)
    with open(f'data/{subject}/date_list.pkl', "wb") as wf:
        pickle.dump(date_list, wf)


    with open(f'data/{subject}/author_length_list.pkl', "rb") as rf:
        read_author_length_list = pickle.load(rf)
    write_author_length_list = read_author_length_list.extend(author_length_list)
    with open(f'data/{subject}/author_length_list.pkl', "wb") as wf:
        pickle.dump(author_length_list, wf)

# subject_list = ['physics', 'cs', 'math', 'q-bio', 'q-fin', 'stat']
# date_list, author_length_list = [], []
# for subject in subject_list:
#     with open(f'data/{subject}/date_list.pkl', "rb") as f:
#         dt_lst = pickle.load(f)
#     date_list.extend(dt_lst)

#     with open(f'data/{subject}/author_length_list.pkl', "rb") as f:
#         at_lst = pickle.load(f)
#     author_length_list.extend(at_lst)

# print(len(date_list))
# with open(f'data/all/date_list.pkl', "wb") as f:
#     pickle.dump(date_list, f)

# with open(f'data/all/author_length_list.pkl', "wb") as f:
#     pickle.dump(author_length_list, f)
