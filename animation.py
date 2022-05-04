from settings import character, character_is_animation, character_eating, character_eating_is_animation



# 人物的动画
class animation:
    # name是asset名，frequency是动画快慢，face_right标明动画人物左右朝向
    def __init__(self, frequency: float = 1, face_right: bool = True,
                 eat_face_right: bool = False):
        self.face_right = face_right
        self.eat_face_right = eat_face_right
        self.moving = 0
        self.frequency = frequency if frequency >= 0 else -frequency

        # 读取动画
        self.image_head = character
        self.is_animation = character_is_animation
        self.is_eating = False
        self.eating_head = character_eating
        self.eating_is_animation = character_eating_is_animation
        self.eating_current = self.eating_head
        self.eating_remain = 0

    # 转头
    def turn(self):
        self.face_right = not self.face_right
        self.eat_face_right = not self.eat_face_right

    def eat(self, time=50):
        self.is_eating = True
        self.eating_remain = time

    def shit(self):
        pass

    # 更新动画
    def image_update(self):
        self.moving += self.frequency
        if self.is_eating:
            if not self.eating_is_animation:
                self.eating_remain -= 1
                if self.eating_remain <= 0:
                    self.is_eating = False
                    self.eating_remain = 0
                return self.eating_head.value[self.eat_face_right]
            while self.moving >= 1:
                self.moving -= 1
                self.eating_current = self.eating_current.next
                if self.eating_current == self.eating_head:
                    self.is_eating = False
                break
            return self.eating_current.value[self.eat_face_right]

        if not self.is_animation:
            return self.image_head.value[self.face_right]
        while self.moving >= 1:
            self.moving -= 1
            self.image_head = self.image_head.next
        return self.image_head.value[self.face_right]
