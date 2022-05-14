import sys
import time

import pygame

from clock import clock, pattern_clock
from player import player
from settings import url, background_dir, clock_voice, between_frame_sleep_time, caption_name, emo, \
    clock_cycle, screen_size, screen, clock_remaining_enabled, time_wake, time_sleep, switch_mode, \
    eat_enabled, emo_enabled, speaking_enabled
from user_management import usr_management, parsing

pygame.init()
sleep_time = between_frame_sleep_time
pattern = pattern_clock(time_wake=time_wake, time_sleep=time_sleep)


def update(USERS, Screen, bg):
    def blit(s=True):
        Screen.blit(bg, (0, 0))
        id_list = list(sorted([(USERS.users[k][0].rect.centery, k) for k in USERS.users.keys()]))
        for k in id_list:
            USERS.users[k[1]][0].update(Screen)
        t, play, left = time_clock.update(switch_mode and not pattern.is_wake())
        if play and clock_remaining_enabled:
            clock_voice.play()
        t_rect = t.get_rect()
        t_rect.bottomright = screen_size
        if switch_mode:
            if clock_remaining_enabled and pattern.is_wake():
                l_rect = left.get_rect()
                l_rect.bottomright = t_rect.topright
                Screen.blit(left, l_rect)
        else:
            if clock_remaining_enabled:
                l_rect = left.get_rect()
                l_rect.bottomright = t_rect.topright
                Screen.blit(left, l_rect)
        Screen.blit(t, t_rect)
        pygame.display.flip()
        if s:
            time.sleep(sleep_time)

    th = parsing(USERS.browser.page_source)
    blit(False)
    th.start()
    for _ in range(10):
        blit()
    blit(False)
    th.join()
    danmu_list = th.get_result()
    speak_list = set()
    for i in danmu_list:
        if i.user_id in USERS.users:
            if i.time > USERS.users[i.user_id][1].time:
                USERS.users[i.user_id][1] = i
                speak_list.add(i.user_id)
        else:
            USERS.users[i.user_id] = [player(i.user_name, frequency=0.5, scale=(80, 60)), i]
            speak_list.add(i.user_id)
            USERS.time_list.append(i.user_id)
    USERS.delete_character()

    for i in list(speak_list):
        if eat_enabled and '吃草' == USERS.users[i][1].content:
            USERS.users[i][0].eat()
        if switch_mode:
            if pattern.is_wake() and USERS.users[i][1].content in emo.keys():
                USERS.users[i][0].emo(USERS.users[i][1].content)
                # for j in emo.keys():
                #     if j in USERS.users[i][1].content:
                #         USERS.users[i][0].emo(j)
            if pattern.is_wake():
                USERS.users[i][0].speak(USERS.users[i][1].content)
        else:
            if emo_enabled and USERS.users[i][1].content in emo.keys():
                USERS.users[i][0].emo(USERS.users[i][1].content)
                # for j in emo.keys():
                #     if j in USERS.users[i][1].content:
                #         USERS.users[i][0].emo(j)
            if speaking_enabled:
                USERS.users[i][0].speak(USERS.users[i][1].content)

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
