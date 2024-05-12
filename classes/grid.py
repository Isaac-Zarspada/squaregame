import pygame as pg

# CONSTANTS
WHITE = (255,255,255)
BLACK = (0,0,0)
BLOCK_SIZE = 30
WIDTH = 1280
HEIGHT = 640

def gen_grid(screen):
        for x in range(0, WIDTH, BLOCK_SIZE):
            for y in range(0, HEIGHT, BLOCK_SIZE):
                rect = pg.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
                pg.draw.rect(screen, WHITE, rect, 1)  # Draw grid lines