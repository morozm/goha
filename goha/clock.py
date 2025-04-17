import pygame
from .constants import FPS
from .utils import resource_path

class Clock:
    def __init__(self, time):
        self.time = time
        self._init()

    def _init(self):
        self.time_font = pygame.font.Font(resource_path("assets/Shojumaru-Regular.ttf"), 25)
        self.paused = True
        self.new_miliseconds = [0, 0]

        if (self.time == 0):
            self.miliseconds = False
            self.added_time = 0
        elif (self.time == 1):
            self.miliseconds = 10*60*1000 # // 600
            self.added_time = 0*1000
        elif (self.time == 2):
            self.miliseconds = 20*60*1000
            self.added_time = 5*1000

    def time_format(self, miliseconds):
        if (self.time != 0):
            seconds = miliseconds // 1000
            self.mins, self.secs = divmod(seconds, 60)
            return '{:02d}:{:02d}'.format(self.mins, self.secs)

    def draw(self, screen, x, y, width, height, color1, color2):
        self.update()
        if self.time != 0:
            time_rect1 = pygame.Rect(0, 0, width+8, height+8)
            time_rect2 = pygame.Rect(0, 0, width, height)
            time_rect1.center = (x, y)
            time_rect2.center = (x, y)
            pygame.draw.rect(screen, color1, time_rect1, border_radius=10)
            pygame.draw.rect(screen, color2, time_rect2, border_radius=10)
            text = self.time_font.render(self.time_format(self.miliseconds - self.new_miliseconds[1]), True, color1)
            screen.blit(text, (x - text.get_width()//2, y - text.get_height()//2))

    def update(self):
        if self.paused == False:
            self.new_miliseconds[1] = pygame.time.get_ticks() - self.new_miliseconds[0]
            if (self.miliseconds - self.new_miliseconds[1] <= 0):
                self.paused = True
                self.miliseconds = 0
                self.new_miliseconds[1] = 0

    def pause(self):
        self.paused = True
        self.miliseconds -= self.new_miliseconds[1]
        self.new_miliseconds[1] = 0

    def resume(self):
        self.paused = False
        self.new_miliseconds[0] = pygame.time.get_ticks()

    def add_time(self):
        self.miliseconds += self.added_time