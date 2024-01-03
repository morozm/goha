import pygame
import random
from .constants import WIDTH, HEIGHT, WHITECOLOR

class Circle:
    def __init__(self):
        self.radius = random.randint(5, 30)
        self.x = random.randint(0, WIDTH - self.radius)
        self.y = random.randint(0, HEIGHT - self.radius)
        self.color_value = random.randint(0, 255)
        self.color = (self.color_value, self.color_value, self.color_value)
        self.speed_x = random.choice([-2, -1, 1, 2])
        self.speed_y = random.choice([-2, -1, 1, 2])
    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y
        if self.x > WIDTH - self.radius or self.x < 0:
            self.speed_x = -self.speed_x
        if self.y > HEIGHT - self.radius or self.y < 0:
            self.speed_y = -self.speed_y

class Background:
    def __init__(self, win):
        self.win = win
        self.circles = [Circle() for _ in range(20)]

    def draw_background(self):
        self.win.fill(WHITECOLOR)
        for circle in self.circles:
            pygame.draw.circle(self.win, circle.color, (circle.x, circle.y), circle.radius)
            circle.move()