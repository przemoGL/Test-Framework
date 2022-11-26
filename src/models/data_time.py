import time


class DataTime:
    def __init__(self):
        self.time = time

    def get_date(self):
        return self.time.strftime("%D")

    def get_time(self):
        return self.time.strftime("%H:%M:%S")
