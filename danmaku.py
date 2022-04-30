import re
import time

pattern_danmus_2 = re.compile(
    r'data-uname="(.*?)" .*?data-type="(\d.*?)" .*?data-uid="(\d*?)" .*?data-ts="(\d*?)" .*?data-danmaku="(.*?)"')


class danmaku:
    def __init__(self, danmu_block):
        danmu_list = pattern_danmus_2.findall(danmu_block)[0]
        self.user_name = danmu_list[0]
        self.user_type = int(danmu_list[1])
        self.user_id = int(danmu_list[2])
        self.time = int(danmu_list[3])
        self.content = danmu_list[4]

    def from_now(self):
        return time.time() - self.time
