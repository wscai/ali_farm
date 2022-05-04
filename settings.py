import pygame
from helper_functions import reader
from selenium import webdriver
pygame.init()

# 基本信息
caption_name = '直播'
between_frame_sleep_time = 0.05
url = 'https://live.bilibili.com/4938691?hotRank=0&session_id=3b441be0f116a7eba5fe5543959daf79_53D67E5C-0762-438A-8726-4CD10026F505&visit_id=8pb02hnbhe00'
mysterious_word = '1'
# browser_driver = webdriver.Safari()
browser_driver = webdriver.Chrome()
screen_size = (pygame.display.Info().current_w,pygame.display.Info().current_h)
screen = pygame.display.set_mode(screen_size, pygame.RESIZABLE)
# 图片

background_dir = 'asset/image/bg.jpeg'
emo_list = ['流泪', '流汗', 'doge', 'cheems'] # 脸要朝左，png格式
emo = {
    i: pygame.transform.scale(pygame.image.load(f'asset/image/emo/{i}.png'), (100,100)) for i in emo_list
}
emo_size = [35, 35]
character, character_is_animation = reader(name='sheep_grey', face_right=False)
character_eating, character_eating_is_animation = reader(name='王境泽', face_right=False)


# 音频
clock_voice = pygame.mixer.Sound('asset/audio/laugh.mp3')

# 字体
id_font = pygame.font.Font('asset/font/general.ttf', 20)
clock_font = pygame.font.Font('asset/font/general.ttf', 200)
clock_remain_font = pygame.font.Font('asset/font/general.ttf', 100)

# 时钟
clock_cycle = [(25, (0, 0, 0)), (5, (255, 255, 255))] # [(minutes, (color RGB)), ...]

