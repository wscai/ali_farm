import pygame
from helper_functions import reader, emo_loader
from selenium import webdriver

pygame.init()

# 基本信息
caption_name = '直播'
between_frame_sleep_time = 0.04
url = 'https://live.bilibili.com/22471888?hotRank=0&session_id=a4521cdf4635faf8160e1a294cd63213_9936858E-DA9F-4E65' \
      '-ADAE-993F0299BD5C&visit_id=99dh06lbve80 '
mysterious_word = '1'
# browser_driver = webdriver.Safari()
browser_driver = webdriver.Chrome()
screen_size = (pygame.display.Info().current_w, pygame.display.Info().current_h)
screen = pygame.display.set_mode(screen_size, pygame.RESIZABLE)
max_character = 150
speaking_enabled = True
emo_enabled = True
eat_enabled = True
clock_remaining_enabled = True

switch_mode = False
time_wake = 7  # 24小时整数
time_sleep = 22  # 24小时整数

# 图片
background_dir = 'asset/image/bg.jpeg'
# 脸朝左是True
emo_dict = {
    '流泪': True,
    '流汗': True,
    'doge': True,
    'cheems': True,
    '企鹅': True,
    '滑稽': True,
    '疑问': False,
    '熊猫头': False,
}
emo = emo_loader(emo_dict)
emo_size = [35, 35]
character, character_is_animation = reader(name='sheep_grey', face_right=False)
character_eating, character_eating_is_animation = reader(name='王境泽', face_right=False)
# weather_effect, _ = reader(name='rain',face_right=False)
weather_effect = None

# 音频
clock_voice = pygame.mixer.Sound('asset/audio/打卡.mp3')

# 字体
id_font = pygame.font.Font('asset/font/general.ttf', 20)
clock_font = pygame.font.Font('asset/font/general.ttf', int(screen_size[1] * 0.1))
clock_remain_font = pygame.font.Font('asset/font/general.ttf', int(screen_size[1] * 0.05))

# 时钟
clock_cycle = [(25, (0, 0, 0)), (5, (255, 255, 255))]  # [(minutes, (color RGB)), ...]
