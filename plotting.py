import matplotlib.pyplot as plt
import numpy as np
import pickle
from collections import Counter
import datetime

with open("date_list.pkl", "rb") as f:
    date_list = pickle.load(f)
datetime_list = [datetime.datetime.combine(d, datetime.time.min) for d in date_list]
datetime_list = sorted(datetime_list)

dcounts = Counter(d for d in datetime_list)
date_list, count_list = [], []
for d, count in dcounts.items():
    date_list.append(d)
    count_list.append(count)
plt.plot(date_list, count_list)
plt.show()
plt.close()

#Monday is 0 and Sunday is 6
day_of_week_list = [d.weekday() for d in date_list]

#Grouping by day of the week
slice_indx_lst = []
old_day_indx = -1 #Throwaway big number
for i, day_indx in enumerate(day_of_week_list):
    if old_day_indx >= day_indx:
        slice_indx_lst.append(i)
    old_day_indx = day_indx

slice_indx_lst.insert(0, 0)
sliced_days, sliced_dates, sliced_counts = [], [], []
for i, j in zip(slice_indx_lst[:-1], slice_indx_lst[1:]):
    sliced_days.append(day_of_week_list[i:j])
    sliced_dates.append(date_list[i:j])
    sliced_counts.append(count_list[i:j])
fig, ax = plt.subplots()
for days, counts in zip(sliced_days, sliced_counts):
    
    #Inserting zeros anytime there is a blank entry and changing blank entry to contain consecutive day
    ax.plot(days, counts, c=np.random.rand(3,))

ax.set_xticklabels([' ', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
plt.show()