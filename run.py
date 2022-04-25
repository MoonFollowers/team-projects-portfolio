import pygame

# initial set
pygame.init()
screen_width = 1000
screen_height = 1000
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Battle Chess")

# var def
## bgm
pygame.mixer.init()
pygame.mixer.music.load('bgm.mp3')
pygame.mixer.music.play(-1)
## FPS
clock = pygame.time.Clock()
## Grid
row = 10
column = 10
Grid_ini = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
Grid = [Grid_ini for a in range(row)]
## Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
## Location
x = 0
y = 0
## Size
Cell = 100


# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


pygame.quit()
