import sys
import pygame
import time
from user_management import usr_management, parsing
from player import player
from clock import clock
from settings import url, background_dir, mysterious_word, clock_voice, between_frame_sleep_time, caption_name, emo

pygame.init()
sleep_time = between_frame_sleep_time

def update(self, screen, bg):
    def blit(s=True):
        screen.blit(bg, (0, 0))
        id_list = list(sorted([(self.users[i][0].rect.centery, i) for i in self.users.keys()]))
        for i in id_list:
            self.users[i[1]][0].update(screen)
        t, play, left = time_clock.update()
        if play:
            clock_voice.play()

        t_rect = t.get_rect()
        t_rect.bottomright = (infoObject.current_w, infoObject.current_h)
        l_rect = left.get_rect()
        l_rect.bottomright = t_rect.topright
        screen.blit(left, l_rect)
        screen.blit(t, t_rect)
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
            self.users[i.user_id] = [player(i.user_name, frequency=0.5, scale=(80, 60)), i]
            speak_list.add(i.user_id)
    for i in list(speak_list):
        if '吃草' in self.users[i][1].content:
            self.users[i][0].eat()
        for j in emo.keys():
            if j in self.users[i][1].content:
                self.users[i][0].emo(j)
        self.users[i][0].speak(self.users[i][1].content)
    blit()


users = usr_management(url)
time.sleep(5)
infoObject = pygame.display.Info()
screen = pygame.display.set_mode((infoObject.current_w, infoObject.current_h), pygame.RESIZABLE)
pygame.display.set_caption(caption_name)
bg = pygame.transform.scale(pygame.image.load(background_dir), (infoObject.current_w, infoObject.current_h))
time_clock = clock([(25, (0, 0, 0)), (5, (255, 255, 255))])
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    update(users, screen, bg)
