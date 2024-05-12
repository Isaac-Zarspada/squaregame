import pygame as pg

class Player:
    COLOR_RED = (255,0,0)
    COLOR_BLUE = (0,0,255)
    def __init__(self, x, y, width, height):
        self.rect = pg.Rect(x,y,width,height)
        self.velx = 0
        self.vely = 0
        
    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    def move_left(self, vel):
        self.velx = -vel

    def move_right(self, vel):
        self.velx = vel

    def move_up(self, vel):
        self.velx = -vel

    def move_down(self, vel):
        self.velx = vel

    def display(self, screen):
        screen.blit(self.surf,self.rect)
    
    def loop(self, fps):
        self.move(self.velx, self.vely)

    def draw(self, screen):
        pg.draw.rect(screen, self.COLOR_BLUE, self.rect)
