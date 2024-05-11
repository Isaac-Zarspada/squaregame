import pygame as pg
import classes as Class
import classes.square as sq
# start the program
pg.init()

# CONSTANTS
WHITE = (255,255,255)
BLACK = (0,0,0)
BLOCK_SIZE = 30
WIDTH = 1280
HEIGHT = 640

dt = 0


SCREEN = pg.display.set_mode((1280,720))
CLOCK = pg.time.Clock()

xspeed = 100
yspeed = 100

playersquare = sq.Player(92, 182, xspeed, yspeed, "red", 27, 27)
# player_RECT = pg.Rect(92, 182, 27, 27)
# vel1 = 100

runtime = True

keys = pg.key.get_pressed()


while runtime: #while statement will continue until statement is false
    for event in pg.event.get(): #event.get is grabbing all events during runtime, then we are looping through those events
        if event.type == pg.QUIT: #this event refers to x button on a window
            runtime = False
        # elif event.type == pg.KEYDOWN: 
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_s:
                playersquare.move('down') 
            if event.key == pg.K_w: 
                playersquare.move('up')
        if event.type == pg.KEYUP:
            if event.key == pg.K_s:
                playersquare.move('up')
            if event.key == pg.K_w:
                playersquare.move('down')

    
            # if keys[pg.K_w]:
            #     player_RECT.y -= 300 
            # if keys[pg.K_s]:
            #     player_RECT.y += 300
            # if keys[pg.K_a]:
            #     player_RECT.x -= 300 
            # if keys[pg.K_d]:
            #     player_RECT.x += 300 

    # fill the screen with a color to wipe away anything from last frame
    SCREEN.fill("black")

   


    # RENDER YOUR GAME HERE
    def gen_grid():
        for x in range(0, WIDTH, BLOCK_SIZE):
            for y in range(0, HEIGHT, BLOCK_SIZE):
                rect = pg.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
                pg.draw.rect(SCREEN, WHITE, rect, 1)  # Draw grid lines

    gen_grid()


    # flip() the display to put your work on screen
    pg.display.flip()

    CLOCK.tick(60)  # limits FPS to 60

# closes game window
pg.quit()