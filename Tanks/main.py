import pygame.font

from modules.classes import *

pygame.init()

background = pygame.image.load(os.path.join(PATH, 'images/background.png'))
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

font = pygame.font.Font(None, 120)
winer1_text = font.render("BLOE WIN", True, (0, 0, 255))
winer2_text = font.render("BLOE WIN", True, (255, 0, 0))

x, y = 0, 0
blocks_list = []
wall_image1 = os.path.join(PATH, 'images/wall.png')
wall_image2 = os.path.join(PATH, 'images/wall1.png')
for row in map:
    for i in row:
        if i == 1:
            blocks_list.append(Block(x, y, 1, wall_image1))
        elif i == 2:
            blocks_list.append(Block(x, y, 2, wall_image2))
        x += STEP
    y += STEP
    x = 0
is_game_running = True
player1 = Player(1, 1)
player2 = Player2(1, 3)
clock = pygame.time.Clock()
FPS = 15
WINNER = None
while is_game_running:
    window.blit(background, (0, 0))
    for block in blocks_list:
        block.blit()
        if block.colliderect(player1.bullet):
            player1.bullet.stop()
            if block.type_block == 1:
                map[block.y // STEP][block.x // STEP] = 0
                block.x = 100000
        elif block.colliderect(player2.bullet):
            player1.bullet.stop()
            if block.type_block == 1:
                map[block.y // STEP][block.x // STEP] = 0
                block.x = 100000

    player1.bullet.move()
    player2.bullet.move()
    player1.blit()
    player2.blit()
    if player1.colliderect(player2.bullet) or player2.colliderect(player1.bullet):
        WINNER = 2 if player1.colliderect(player2.bullet) else 1
        is_game_running = False
        is_winner = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_game_running = False
    clock.tick(FPS)
    pygame.display.flip()
cors = (SCREEN_WIDTH // 2 - winer1_text.get_width() // 2, SCREEN_HEIGHT // 2 - winer1_text.get_width() // 2)
while is_winner:
    window.blit(background, (0, 0))
    window.blit(winer1_text, cors) if WINNER == 1 else window.blit(winer2_text, cors)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_winner = False
    pygame.display.flip()