from online_test.date_class import Date
datea=Date(2020,1,1)
dateb=Date(2020,1,1)
print(datea.day)
for _ in range(1):
    datea.nextDay()
# print('\n')
# datea.nextDay()
dateb.nextNDays(1)
print(datea.year,datea.month,datea.day)
print(dateb.year,dateb.month,dateb.day)