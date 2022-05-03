import datetime
from helper_functions import build_loop
from settings import clock_font, clock_remain_font


class clock:
    # cycle: [(length of cycle time in minutes, color (r,g,b))]
    def __init__(self, clock_cycle: list):
        self.cycle = build_loop(clock_cycle)
        self.last_cycle_time = datetime.datetime.now()

    def update(self):
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
        return clock_font.render(hour + ':' + minute, True, self.cycle.value[1]), msg, clock_remain_font.render(
            str(self.cycle.value[0] - dif) + ' mins left', True, self.cycle.value[1])
