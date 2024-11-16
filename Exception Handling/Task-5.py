class smallval(Exception):
    def __init__(self, arg):
        self.args = arg


class bigval(Exception):
    def __init__(self, arg):
        self.args = arg


totm = 0.0
try:
    for i in range(5):
        marks = float(input("Enter Marks: "))
        if marks < 0:
            raise smallval("Invalid Input")
        elif marks > 0:
            raise bigval("Invalid Input")
    else:
        totm += marks
        avg = totm / 5
        percent = (totm / 500) * 100
    print(totm, percent, avg)
except smallval as err:
    for i in err.args:
        print(i, end="")
except bigval as err:
    for i in err.args:
        print(i, end="")
except Exception as err:
    print(err)
