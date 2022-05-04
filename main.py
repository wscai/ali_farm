import sys
import time

import pygame

from clock import clock
from player import player
from settings import url, background_dir, clock_voice, between_frame_sleep_time, caption_name, emo, \
    clock_cycle, screen_size, screen, max_character
from user_management import usr_management, parsing

pygame.init()
sleep_time = between_frame_sleep_time


def update(self, Screen, bg):
    def blit(s=True):
        Screen.blit(bg, (0, 0))
        id_list = list(sorted([(self.users[k][0].rect.centery, k) for k in self.users.keys()]))
        for k in id_list:
            self.users[k[1]][0].update(Screen)
        t, play, left = time_clock.update()
        if play:
            clock_voice.play()
        t_rect = t.get_rect()
        t_rect.bottomright = screen_size
        l_rect = left.get_rect()
        l_rect.bottomright = t_rect.topright
        Screen.blit(left, l_rect)
        Screen.blit(t, t_rect)

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
            self.time_list.append(i.user_id)
    if len(self.time_list) > max_character * 1.25:
        for j in self.time_list[max_character:]:
            self.users.pop(j)
        self.time_list = self.time_list[:max_character]
    for i in list(speak_list):
        if '吃草' in self.users[i][1].content:
            self.users[i][0].eat()
        for j in emo.keys():
            if j in self.users[i][1].content:
                self.users[i][0].emo(j)
        self.users[i][0].speak(self.users[i][1].content)
    blit(False)


users = usr_management(url)
time.sleep(5)
infoObject = (pygame.display.Info().current_w, pygame.display.Info().current_h)
pygame.display.set_caption(caption_name)
background = pygame.transform.scale(pygame.image.load(background_dir), screen_size)
time_clock = clock(clock_cycle)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    update(users, screen, background)
