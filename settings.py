import pygame
from helper_functions import reader
from selenium import webdriver
pygame.init()

# 基本信息
caption_name = '直播'
between_frame_sleep_time = 0.05
url = 'https://live.bilibili.com/292891?hotRank=0&session_id=0c28084f2e4b8b05ee833fb75ea6dc27_8D5A5EC9-B88D-40EA-935E-899C97178C77&visit_id=bvsik0r3fwg0'
mysterious_word = '1'
# browser_driver = webdriver.Safari()
browser_driver = webdriver.Chrome()

# 图片
background_dir = 'asset/image/bg.jpeg'
emo_list = ['流泪', '流汗', 'doge', 'cheems'] # 脸要朝左，png格式
emo = {
    i: pygame.transform.scale(pygame.image.load(f'asset/image/emo/{i}.png'), (45, 45)) for i in emo_list
}
character, character_is_animation = reader(name='sheep_grey', face_right=False)
character_eating, character_eating_is_animation = reader(name='王境泽', face_right=False)


# 音频
clock_voice = pygame.mixer.Sound('asset/audio/laugh.mp3')

# 字体
id_font = pygame.font.Font('asset/font/general.ttf', 20)
clock_font = pygame.font.Font('asset/font/general.ttf', 200)
clock_remain_font = pygame.font.Font('asset/font/general.ttf', 100)



