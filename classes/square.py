import pygame as pg
HEIGHT = 640
class Player:

    def init(self, positionx, positiony, xspeed, yspeed, color, width, height):
        self.color = color
        self.xspeed = xspeed
        self.yspeed = yspeed
        self.y = positiony
        self.x = positionx
        self.surf = pg.Surface((width, height))
        self.rect = self.surf.get_rect(midbottom = (self.x, self.y))
        self.top = self.rect.top
        self.bottom = self.rect.bottom
        

    def display(self, screen):
        screen.blit(self.surf,self.rect)

    def player_animation(self):
        self.rect.y += self.yspeed
        self.rect.x += self.xspeed 
        if self.rect.top <= 0:
            self.rect.top =0
        if self.rect.bottom >=HEIGHT:
            self.rect.bottom =HEIGHT

