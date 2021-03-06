import time
import threading
import re
from danmaku import danmaku
from settings import browser_driver, max_character

pattern_danmus = re.compile('<div class="chat-item danmaku-item .*?"(.*?)>')


class user:
    def __init__(self, ):
        self.character = None
        self.danmaku = None

    def last(self):
        return time.time() - self.danmaku.time


class usr_management:
    def __init__(self, link):
        self.browser = browser_driver
        self.browser.get(link)
        self.browser.implicitly_wait(10)
        self.link = link
        self.users = {}  # {uid: [player, danmaku]}
        self.html = ''
        self.update_frequency = 10
        self.now = 1
        self.time_list = []

    def sorted_place(self):
        return sorted([(self.users[i][0].rect.centery, i) for i in self.users.keys()])

    def __len__(self):
        return len(self.users.keys())

    def __index__(self, index):
        if index in self.users.keys():
            return self.users[index]
        else:
            return None

    def delete_character(self):
        if len(self) > max_character * 1.3:
            for j in self.time_list[max_character:]:
                self.users.pop(j)
            self.time_list = self.time_list[:max_character]



class parsing(threading.Thread):
    def __init__(self, html):
        threading.Thread.__init__(self)
        self.html = html
        self.pattern_danmus = re.compile('<div class="chat-item danmaku-item .*?"(.*?)>')
        self.dml = []

    def run(self):
        danmu_list = self.pattern_danmus.findall(self.html)
        self.dml = [danmaku(i) for i in danmu_list]

    def get_result(self):
        threading.Thread.join(self)  # 等待线程执行完毕
        try:
            return self.dml
        except Exception:
            return []
