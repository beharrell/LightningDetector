from ElapseTimer import ElapseTimer

class FrameRate:
    def __init__(self):
        self.timer = ElapseTimer(1, True)
        self.count = 0
        self.rate = 0


    def Update(self):
        newRateValue = self.timer.Update()
        self.count += 1
        if (newRateValue):
            self.rate = self.count
            self.count = 0
        return newRateValue


