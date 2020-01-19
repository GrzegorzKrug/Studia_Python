import time


class TimeServer:
    def time(self):
        time_now = time.time() * 1000
        return int(time_now)

    def time_str(self):
        t = str(self.time())
        # print
        return t
