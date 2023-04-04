import pygame,sys
pygame.init()

# create a screen:
screen = pygame.display.set_mode((600,600))
done = False



# (red,green,blue)
black = (0,0,0)
color = (255,255,255)
# never ending loop now:
screen.fill(color)
while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    for x in range(0,600,100):
        pygame.draw.line(screen,black,(1,x),(600,x), 2)
        pygame.draw.line(screen,black,(x,1),(x,600), 2)
        pygame.draw.rect(screen,black,(200,100,100,100))
        pygame.display.update()