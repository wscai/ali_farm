import os
import pygame


# Linked list
class Node:
    def __init__(self, val):
        self.value = val
        self.next = None


# 创建looped linked list 以播放动画
def build_loop(img_list) -> Node:
    head = Node(img_list[0])
    cur = head
    for i in img_list[1:]:
        cur.next = Node(i)
        cur = cur.next
    cur.next = head
    return head


def reader(name, face_right):
    image = []
    if name in os.listdir('asset/image'):
        is_animation = True
        for i in range(len(os.listdir(f'asset/image/{name}'))):
            image.append({
                face_right: pygame.image.load(f'asset/image/{name}/{i}.png'),
                not face_right: pygame.transform.flip(pygame.image.load(f'asset/image/{name}/{i}.png'), True,
                                                      False)})

        image_head = build_loop(image)
    else:
        is_animation = False
        if name + '.png' not in [i for i in os.listdir('asset/image')]:
            raise Exception('Not in asset or not a png file')
        image_head = build_loop([{
            face_right: pygame.image.load(f'asset/image/{name}.png'),
            not face_right: pygame.transform.flip(pygame.image.load(f'asset/image/{name}.png'), True,
                                                  False)}])
    return image_head, is_animation
