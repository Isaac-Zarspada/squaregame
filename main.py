import pygame as pg
from classes import grid as g, square as sq
# start the program
pg.init()

# CONSTANTS
WHITE = (255,255,255)
BLACK = (0,0,0)
BLOCK_SIZE = 30
WIDTH = 1280
HEIGHT = 640
PLAYER_VEL = 20
FPS = 60
window = pg.display.set_mode((WIDTH,HEIGHT), pg.RESIZABLE)

def handle_move(player):
    keys = pg.key.get_pressed()
    
    player.velx = 0
    player.vely = 0
    if keys[pg.K_LEFT]:
        player.move_left(PLAYER_VEL)
    if keys[pg.K_RIGHT]:
        player.move_right(PLAYER_VEL)
    if keys[pg.K_UP]:
        player.move_up(PLAYER_VEL)
    if keys[pg.K_DOWN]:
        player.move_down(PLAYER_VEL)

# def main(window):
clock = pg.time.Clock()
    
player1 = sq.Player(100, 100, 27, 27)

runtime = True
while runtime: #while statement will continue until statement is false
    clock.tick(FPS)  # limits FPS to 60
    
    for event in pg.event.get(): #event.get is grabbing all events during runtime, then we are looping through those events
        if event.type == pg.QUIT: #this event refers to x button on a window
            runtime = False
    # RENDER GAME HERE
    window.fill("black")
    g.gen_grid(window)
    

    player1.loop(FPS)
    handle_move(player1)
    player1.draw(window)
    pg.display.update()

    # flip() the display to put your work on screen
    pg.display.flip()


    # closes game window
pg.quit()

# if __init__ == "main"