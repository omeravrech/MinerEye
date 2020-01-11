
class AvgCalculate(object):
    def __init__(self):
        self.avg = 0
        self.amount = 0

    def update(self, input):
        if isinstance(input, (float, int)):
            _number = input
        elif isinstance(input, str):
            try:
                _number = float(input)
            except:
                return
        else:
            return

        self.avg = ((self.avg * self.amount) + _number) / (self.amount + 1)
        self.amount += 1

    def getAvg(self):
        return self.avg


if __name__ == "__main__":
    a = AvgCalculate()
    a.update(1)
    a.update(2)
    print("Average is:", a.getAvg())