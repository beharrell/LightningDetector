import time

class ElapseTimer:
    def __init__(self, interval,autoReset):
        self.refTime = time.time()
        self.interval = interval
        self.autoReset = autoReset

    def Reset(self):
        self.refTime = time.time()

    def Update(self):
        diff = time.time() - self.refTime
        expired = diff >= self.interval
        if (expired and self.autoReset):
             self.Reset()
        return expired