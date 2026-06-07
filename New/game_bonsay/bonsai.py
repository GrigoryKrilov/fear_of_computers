import pygame
import sys  # библетека для создания скриптов.
# print(pygame.ver)
pygame.init()
# высота и ширинка экрана
WIDTH,HEIGHT = 800,600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Бонсай-релаксация") # надпись
# цвета в РГБ
BACKGROUND_COLOR = (144, 238, 144)  # зеленый
BONSAI_COLOR = (139, 69, 19)  # коричневый
# время
clock = pygame.time.Clock()
FPS = 60

runnung = True
while runnung:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runnung =False
            
    screen.fill(BACKGROUND_COLOR)
    pygame.display.flip()
    clock.tick(FPS)
 
pygame.quit()
sys.tick(FPS)

# новое перенести в тетрадку.

# py --version
# which python
# py -m pip install pygame
