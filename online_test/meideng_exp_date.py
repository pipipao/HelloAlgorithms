def getExpirationDate(year, month, day,orderSpan):
    bigMonth = {1, 3, 5, 7, 8, 10, 12}
    smallMonth = {4, 6, 9, 11}
    # orderSpan = 1
    expMonth = month + orderSpan
    # 计算出不考虑情况的失效日期
    if expMonth > 12:
        year += 1
        expMonth %= 12
    # 如果是28号之前的天数或者在大月里失效那么一定合理直接返回
    if day <= 28 or expMonth in bigMonth:
        return [year, expMonth, day]
    # 如果失效日期在小月，只需要考虑31号的情况
    if expMonth in smallMonth:
        if day == 31:
            return [year, expMonth, 30]
        # 小月的29、30号直接返回
        return [year, expMonth, day]
    # 失效日期不是大月也不是小月，只可能是最小的2月
    # 此时日期>=29，那么闰年返回29，普通年份返回28
    if isLeapYear(year):
        return [year, expMonth, 29]
    return [year, expMonth, 28]


def isLeapYear(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    return False

if __name__ == '__main__':
    print(getExpirationDate(2020,3,31))
    print(getExpirationDate(2020,1,31))
    print(getExpirationDate(2019,1,31))
    print(getExpirationDate(2019,12,31))
    print(getExpirationDate(2020,2,5))
    print('\n')
    print(getExpirationDate(2018,11,10))
    print(getExpirationDate(2018,12,10))
    print(getExpirationDate(2019,1,30))
    print(getExpirationDate(2019,4,30))
