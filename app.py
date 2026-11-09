import pygame
from body import RigidBody
pygame.init()

exitgame =0
SCREEN_WIDTH, SCREEN_HEIGHT = 480,480
relativeX, relativeY = 0,0
clock = pygame.time.Clock()
FPS = 100


is_draggingMid = False
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("my phyics Engine")

mainbody = RigidBody([(1,1,1),(100,1,1),(100,100,1),(1,100,1)],0,0,10,5)
mainbody2 = RigidBody([(200,150,1), (350,150,1), (350,200,1), (200,200,1)], 0, 0, 0, 0)


while (not exitgame) :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exitgame = 1
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 2:  # Left click
                is_draggingMid = True
                    
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 2:
                is_draggingMid = False
                
        elif event.type == pygame.MOUSEMOTION:
            if is_draggingMid:
                # Move the box by the relative distance the mouse moved
                relativeX += event.rel[0]
                relativeY += event.rel[1]

    dt = clock.tick(FPS) /1000
    screen.fill((10, 10, 10))
    #draw between this
    mainbody.draw(screen , relativeX , relativeY)
    mainbody.update(dt)
    mainbody2.draw(screen , relativeX , relativeY)
    mainbody2.update(dt)


    #draw between this
    pygame.display.flip()
