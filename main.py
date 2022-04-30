import sys
import pygame
import time
from user_management import usr_management, parsing
from player import player

pygame.init()
sleep_time = 0.05
url = 'https://live.bilibili.com/451?hotRank=0&session_id=2990e7d1587c6892c5781cdd9c15e5fa_6032ECCC-4B30-40C3-BEF6-7935C0BCE57F&visit_id=43526qphei80'
background_dir = 'asset/image/bg.jpeg'


def update(self, screen, bg):
    def blit(s=True):
        screen.blit(bg, (0, 0))
        id_list = list(sorted([(self.users[i][0].rect.centery, i) for i in self.users.keys()]))
        for i in id_list:
            self.users[i[1]][0].update(screen)
        pygame.display.flip()
        if s:
            time.sleep(sleep_time)
    th = parsing(self.browser.page_source)
    blit(False)
    th.start()
    for _ in range(10):
        blit()
    blit(False)
    th.join()
    danmu_list = th.get_result()
    speak_list = set()
    for i in danmu_list:
        if i.user_id in self.users:
            if i.time > self.users[i.user_id][1].time:
                self.users[i.user_id][1] = i
                speak_list.add(i.user_id)
        else:
            self.users[i.user_id] = [player(i.user_name,frequency=0.5,scale=(80,60)), i]
            speak_list.add(i.user_id)
    for i in list(speak_list):
        if '的' in self.users[i][1].content:
            self.users[i][0].eat()
        self.users[i][0].speak(self.users[i][1].content)
    blit()


users = usr_management(url)
time.sleep(5)
infoObject = pygame.display.Info()
screen = pygame.display.set_mode((infoObject.current_w, infoObject.current_h), pygame.RESIZABLE)
pygame.display.set_caption('直播')
bg = pygame.transform.scale(pygame.image.load(background_dir), (infoObject.current_w, infoObject.current_h))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    update(users,screen,bg)


