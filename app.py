import pygame
from body import RigidBody
pygame.init()

exitgame =0
SCREEN_WIDTH, SCREEN_HEIGHT = 480,480
relativeX, relativeY = 0,0
clock = pygame.time.Clock()
FPS = 100


is_dragging = False
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("my phyics Engine")

mainbody = RigidBody(0,0,100,100,1,0,0,10,5)

while (not exitgame) :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exitgame = 1
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left click
                is_dragging = True
                    
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                is_dragging = False
                
        elif event.type == pygame.MOUSEMOTION:
            if is_dragging:
                # Move the box by the relative distance the mouse moved
                relativeX += event.rel[0]
                relativeY += event.rel[1]

    dt = clock.tick(FPS) /1000
    screen.fill((10, 10, 10))
    #draw between this
    pygame.draw.rect(screen, (255,255,255), (mainbody.x+relativeX,mainbody.y+relativeY,mainbody.sizeX,mainbody.sizeY))
    mainbody.update(dt)
    #draw between this
    pygame.display.flip()
    print(mainbody.x,mainbody.y)
