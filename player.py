import pygame
import random
from animation import animation

pygame.init()
infoObject = pygame.display.Info()
font = pygame.font.Font('asset/font/general.ttf', 20)
a_name = 'sheep_grey'


class player(pygame.sprite.Sprite):
    # 定义构造函数
    # name是asset/image中的无后缀文件名，move_range是可运动的一个方块，font是导入字体，scale是初始大小，frequency是动画快慢，factor是近大远小乘数，screen_height是屏幕高度
    # move_range = [left,right,top,down]
    def __init__(self, name, scale=(40, 40), move_range=(0, infoObject.current_w, 300, infoObject.current_h),
                 frequency: float = 1, face_right: bool = False, factor: float = 1.1,
                 screen_height: int = 1080, speaking_time: int = 100, eat_face_right: bool = False):
        # 调父类来初始化子类
        pygame.sprite.Sprite.__init__(self)
        # 加载图片
        self.name = font.render(name, True, (0, 0, 0))
        self.id_rect = self.name.get_rect()
        self.animation = animation(a_name, frequency, face_right, eat_face_right=eat_face_right)
        self.scale = scale
        self.factor = factor
        self.screen_height = screen_height
        self.is_speaking = False
        self.words = None
        self.words_rect = None
        self.speaking_time = speaking_time
        self.speaking_remain = speaking_time
        # self.image = pygame.transform.scale(pygame.image.load(filename),(40,40))
        self.move_range = move_range
        # 获取图片rect区域
        self.rect = pygame.Rect(0, 0, scale[0], scale[1])
        # 初始位置和初始目的地
        self.rect.midtop = (
            random.randint(self.move_range[0], self.move_range[1]),
            random.randint(self.move_range[2], self.move_range[3]))
        self.to_location = (
            random.randint(self.move_range[0], self.move_range[1]),
            random.randint(self.move_range[2], self.move_range[3]))
        # 初始面向
        if self.to_location[0] > self.rect.midtop[0] and not self.animation.face_right:
            self.animation.turn()
        elif self.to_location[0] < self.rect.midtop[0] and self.animation.face_right:
            self.animation.turn()

    # 说话
    def speak(self, text: str):
        self.words = font.render(str(text), True, (0, 0, 0), (255, 255, 255))
        self.is_speaking = True

    def eat(self):
        self.animation.eat()

    # 每帧更新
    def update(self, screen):
        # Update图片的位置
        # 到达位置自动随机新位置，并自动转向
        if self.animation.is_eating:
            scale_factor = self.rect.midtop[1] * self.factor / self.screen_height + 1
            screen.blit(pygame.transform.scale(self.animation.image_update(),
                                               (int(self.scale[0] * scale_factor), int(self.scale[1] * scale_factor))),
                        self.rect)
        else:
            if self.rect.midtop[0] == self.to_location[0] and self.rect.midtop[1] == self.to_location[1]:
                new_location = (random.randint(self.move_range[0], self.move_range[1]),
                                random.randint(self.move_range[2], self.move_range[3]))
                if self.to_location[0] > new_location[0] and self.animation.face_right:
                    self.animation.turn()
                elif self.to_location[0] < new_location[0] and not self.animation.face_right:
                    self.animation.turn()
                self.to_location = new_location
            # 行走，先斜着，再直线走
            if self.rect.midtop[0] > self.to_location[0]:
                self.rect.midtop = (self.rect.midtop[0] - 1, self.rect.midtop[1])
            elif self.rect.midtop[0] < self.to_location[0]:
                self.rect.midtop = (self.rect.midtop[0] + 1, self.rect.midtop[1])
            if self.rect.midtop[1] > self.to_location[1]:
                self.rect.midtop = (self.rect.midtop[0], self.rect.midtop[1] - 1)
            elif self.rect.midtop[1] < self.to_location[1]:
                self.rect.midtop = (self.rect.midtop[0], self.rect.midtop[1] + 1)

            # 近大远小，决定人物大小
            scale_factor = self.rect.midtop[1] * self.factor / self.screen_height + 1
            self.rect.height = int(self.scale[1] * scale_factor)
            self.rect.width = int(self.scale[0] * scale_factor)

            # update动画图片
            screen.blit(pygame.transform.scale(self.animation.image_update(),
                                               (int(self.scale[0] * scale_factor), int(self.scale[1] * scale_factor))),
                        self.rect)
        # 决定ID位置
        self.id_rect.midbottom = (self.rect.centerx, self.rect.midtop[1])
        # 说话
        if self.is_speaking:
            self.speaking_remain -= 1
            if self.words is not None:
                self.words_rect = self.words.get_rect()
                self.words_rect.midbottom = (self.rect.centerx, self.id_rect.midtop[1])

        # Update文字ID的位置
        screen.blit(self.name, self.id_rect)
        if self.is_speaking:
            screen.blit(self.words, self.words_rect)
            if self.speaking_remain <= 0:
                self.speaking_remain = self.speaking_time
                self.is_speaking = False
