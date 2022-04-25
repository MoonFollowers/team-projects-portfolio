import pygame


# show grid function
def display_grid():
    for idx, rect in enumerate(Grid):
        if idx == 1:
            pygame.draw.rect(screen, WHITE, rect)


# initial set
pygame.init()
screen_width = 1000
screen_height = 1000
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Battle Chess")
pygame.font.Font(None, 40)

# var def
## bgm
pygame.mixer.init()
pygame.mixer.music.load('bgm.mp3')
pygame.mixer.music.play(-1)
## FPS
clock = pygame.time.Clock()

## Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
## Location
x = 0
y = 0
## Size
Cell = 100
Square = pygame.Rect(0,0,100,100)
## Grid
row = 10
column = 10
Grid_ini = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
Grid = [[Square for a in range(column)] for a in range(row)]

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(RED)

    display_grid()

    # Update Screen
    pygame.display.update()

# Quit Game
pygame.quit()
