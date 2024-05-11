import pygame as pg


pg.init()
screen = pg.display.set_mode((1280,720))
clock = pg.time.Clock()


runtime = True


while runtime: #while statement will continue until statement is false
    for event in pg.event.get(): #event.get is grabbing all events during runtime, then we are looping through those events
        if event.type == pg.QUIT: #this event refers to x button on a window
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("cyan")

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pg.display.flip()

    clock.tick(60)  # limits FPS to 60


pg.quit()