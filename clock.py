import datetime
from helper_functions import build_loop
from settings import clock_font, clock_remain_font


class clock:
    def __init__(self, clock_cycle: list):
        self.cycle = build_loop(clock_cycle)
        self.last_cycle_time = datetime.datetime.now()

    def update(self,night_color):
        msg = False
        minute = '0' + str(datetime.datetime.now().minute) if datetime.datetime.now().minute < 10 else str(
            datetime.datetime.now().minute)
        hour = '0' + str(datetime.datetime.now().hour) if datetime.datetime.now().hour < 10 else str(
            datetime.datetime.now().hour)
        dif = (datetime.datetime.now() - self.last_cycle_time).seconds // 60
        if dif >= self.cycle.value[0]:
            self.cycle = self.cycle.next
            self.last_cycle_time = datetime.datetime.now()
            msg = True
        if night_color:
            color = (0,0,0)
        else:
            color = self.cycle.value[1]
        return clock_font.render(hour + ':' + minute, True, color), msg, clock_remain_font.render(
            str(self.cycle.value[0] - dif) + '分钟剩余', True, color)


class pattern_clock:
    def __init__(self, time_wake: int, time_sleep: int):
        self.time_wake = time_wake
        self.time_sleep = time_sleep
        if self.time_sleep > self.time_wake:
            self.wake_range = set(range(self.time_wake, self.time_sleep))
        else:
            self.wake_range = set([range(0, self.time_sleep)] + [range(self.time_wake, 24)])

    def is_wake(self):
        if datetime.datetime.now().hour in self.wake_range:
            return True
        else:
            return False
