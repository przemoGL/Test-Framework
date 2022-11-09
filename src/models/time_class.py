import time


class Time:
    def __init__(self):
        self.time = time

    def hour(self):
        return self.time.strftime("%H:%M:%S")

    def data(self):
        return self.time.strftime("%D")
