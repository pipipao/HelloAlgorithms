from online_test.date_class import Date
from online_test.meideng_exp_date import getExpirationDate

check = dict()
date = Date(2015, 1, 1)
while date.year < 2022:
    for timeSpan in [1, 3, 6, 12]:
        expDate = getExpirationDate(date.year, date.month, date.day, timeSpan)
        t = (expDate[0], expDate[1], expDate[2])
        if t not in check.keys():
            check[t] = 1
        else:
            check[t] += 1

    date.nextDay()

max_v = max(check.values())
for key, value in check.items():
    if max_v == value or value == max_v - 1:
        print(key, value)

print('**************')
for key, value in check.items():
    if 12 > value > 4:
        print(key, value)
