import sys
import pygame
import time
from user_management import usr_management, parsing
from player import player,emo

pygame.init()
sleep_time = 0.05
url = 'https://live.bilibili.com/8308544?hotRank=0&session_id=11f56503093dfb9366d9771a730ae7f6_22D97473-63A1-4D89-9F8A-9E8224795A9E&visit_id=aoxj10z4m040'
background_dir = 'asset/image/bg.jpeg'
mysterious_word = '1'


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
        if mysterious_word in self.users[i][1].content:
            self.users[i][0].eat()
        if '你好' in self.users[i][1].content:
            self.users[i][0].emo('cat')
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


