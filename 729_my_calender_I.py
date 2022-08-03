# https://leetcode.com/problems/my-calendar-i/


class MyCalendar:

    def __init__(self):
        self.calender = []

    def book(self, start: int, end: int) -> bool:
        i = 0
        while i < len(self.calender):
            if start > self.calender[i][1]:
                i += 1
                continue
            if start <= self.calender[i][0] < end or start < self.calender[i][1] <= end or \
                    self.calender[i][0] <= start < self.calender[i][1] or \
                    self.calender[i][0] < end <= self.calender[i][1]:
                return False
            if self.calender[i][0] >= end:
                self.calender.insert(i, (start, end))
                break
            i += 1
        else:
            self.calender.append((start, end))
        return True


if __name__ == '__main__':
    c = MyCalendar()
    for i, j in [[23, 32], [26, 31]]:
        print(c.book(i, j))
        print(c.calender)
