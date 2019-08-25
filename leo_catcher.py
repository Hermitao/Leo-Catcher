import sys, pygame
from pygame.locals import *
import random as rd
pygame.init()

score = 0

size = width, height = 800, 600

screen_offset = 60

spoon_x = width/2
spoon_y = height - 180
leo_starting_y = -200
game_over = False

seconds_elapsed = 0

frames_per_second = 60

class Leo:
        x = 0
        y = 0
        dy = 0
        
        def __init__(self):
                self.x = rd.randint(60, width)
                self.y = leo_starting_y
                self.dy = rd.randint(1, 3)

        def update(self):
                self.y += self.dy
                if self.y > height:
                        global game_over
                        game_over = True
                        self.y = 0 - 200
                        self.x = rd.randint(screen_offset, width - screen_offset)
                        r.dy = rd.randint(1, 3) * int(round(seconds_elapsed * 0.1))
                self.x+= rd.randint(-5, 5)
                if self.x < 10:
                        self.x = 10
                if self.x > width - screen_offset:
                        self.x = width - screen_offset
                screen.blit(cabeca_do_leo, (self.x, self.y))

        def is_caught(self):
                return self.y >= spoon_y - 100 and self.y <= spoon_y + 20 and\
                       self.x >= spoon_x - 20 and self.x < spoon_x + 120
                
clock = pygame.time.Clock()
leos = [Leo(), Leo(), Leo()]

pygame.init()

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('LÉO CATCHER')
spoon = pygame.image.load('resources/spoon.gif')
cabeca_do_leo = pygame.image.load('resources/leo.gif')

def update_spoon():
        global spoon_x
        global spoon_y
        spoon_x, ignore = pygame.mouse.get_pos()
        screen.blit(spoon, (spoon_x, spoon_y))

def check_for_catch():
        global score
        for r in leos:
                if r.is_caught():
                        score += 1
                        r.y = leo_starting_y
                        r.x = rd.randint(screen_offset, width - screen_offset)
                        r.dy = rd.randint(1, 3) * int(round(seconds_elapsed * 0.15))
                

def display(message, pos):
        font = pygame.font.Font(None, 36)
        text = font.render(message, 1, (10, 10, 10))
        screen.blit(text, pos)

while True:
        seconds_elapsed = pygame.time.get_ticks() / 1000
        if game_over:
                break
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        sys.exit()
        screen.fill((255, 255, 255))
        for r in leos:
                r.update()
        update_spoon()
        check_for_catch()
        display('Score: ' + str(score), (0, 0))
        display('Time: ' + str(round(seconds_elapsed, 2)), (0, 20))
        pygame.display.update()
        clock.tick(60)
