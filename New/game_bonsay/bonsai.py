import os  # скрипот поможет посмотреть текущую папку и файлы в ней.
print("текущая папка", os.getcwd())
print("фалйы в текущей папки", os.listdir("."))





# import pygame
# pygame.init()
# width, height = 800,600
# sreen = pygame.display.set_mode((width,height))

# assetes = pygame.image.load("/c/Users/user/Desktop/Programming/fear_of_computers/new/game_bonsay/assetes/branch/brunch_2.png").convert_alpha
# print(assetes)
# # running = True
# # while running:
# #       for event in pygame.event.get():
# #         if event.type == pygame.QUIT:
# #             runnung =False

# #       assetes = pygame.image.load("/c/Users/user/Desktop/Programming/fear_of_computers/new/game_bonsay/assetes/branch/brunch_2.png")
# #       print(assetes)

# # pygame.quit()








# import pygame
# import sys  # библетека для создания скриптов.

# # print(pygame.ver) # узнаю установлен ли py game и версию его.

# pygame.init()
# # высота и ширинка экрана
# WIDTH,HEIGHT = 800,600
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Бонсай-релаксация") # надпись
# # цвета в РГБ
# BACKGROUND_COLOR = (144, 238, 144)  # зеленый
# BONSAI_COLOR = (139, 69, 19)  # коричневый
# # время
# clock = pygame.time.Clock()
# FPS = 60

# #пути к картинкам
# PASS_trunk=""
# PASS_big_trunk="New/game_bonsay/assetes/big_trunk/trunk_big.png"
# PASS_branch="New/game_bonsay/assetes/branch"
# PASS_sprout=""
# # Классы
# class Trunk:
#     def_init_(x,y,w,h)



# runnung = True
# while runnung:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             runnung =False
            
#     screen.fill(BACKGROUND_COLOR)
#     pygame.display.flip()
#     clock.tick(FPS)
 
# pygame.quit()
# sys.tick(FPS)

# # новое перенести в тетрадку.

# # py --version
# # which python
# # py -m pip install pygame
