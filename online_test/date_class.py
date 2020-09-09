class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def nextDay(self):
        monthDays = {1: 31, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        if self.isLeapYear():
            monthDays[2] = 29
        else:
            monthDays[2] = 28
        day = self.day + 1
        if day > monthDays[self.month]:
            self.day = 1
            self.month += 1
            if self.month > 12:
                self.month = 1
                self.year += 1
        else:
            self.day = day

    def nextNDays(self, n):
        for _ in range(n):
            self.nextDay()

    def isLeapYear(self):
        if (self.year % 4 == 0 and self.year % 100 != 0) or self.year % 400 == 0:
            return True
        return False
