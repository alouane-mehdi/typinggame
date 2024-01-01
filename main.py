import pygame
import random
import time

pygame.init()

WIDTH = 800
HEIGHT = 600
black = (0, 0, 0)
gameDisplay = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Typing Game')

background = pygame.image.load('typinggame/entrée.jpg')
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

font = pygame.font.Font('typinggame/comic.ttf', 40)

score = 0

def new_word():
    global displayword, mot, x_cor, y_cor, text
    x_cor = random.randint(300, 700)
    y_cor = 200
    mot = ''
    mots = open("typinggame/words.txt").read().split(', ')
    displayword = random.choice(mots)

new_word()

font_name = pygame.font.match_font('arias')

def draw_text(display, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, black)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    gameDisplay.blit(text_surface, text_rect)

def game_front_screen():
    gameDisplay.blit(background, (0, 0))
    if not game_over:
        draw_text(gameDisplay, "GAME OVER!", 90, WIDTH / 2, HEIGHT / 4)
        draw_text(gameDisplay, "Score : " + str(score), 70, WIDTH / 2, HEIGHT / 2)
    else:
        draw_text(gameDisplay, "Appuyez sur une touche pour jouer !", 54, WIDTH / 2, 500)
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False

game_over = True
game_start = True

while True:
    if game_over:
        if game_start:
            game_front_screen()
        game_start = False
    game_over = False

    background = pygame.image.load('typinggame/city.jpg')
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    personnage = pygame.image.load('typinggame/perso.jpg')
    personnage = pygame.transform.scale(personnage, (50, 50))

    gameDisplay.blit(background, (0, 0))


    gameDisplay.blit(personnage, (x_cor - 100, y_cor))
    draw_text(gameDisplay, str(displayword), 40, x_cor, y_cor)
    draw_text(gameDisplay, 'Score:' + str(score), 40, WIDTH / 2, 5)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            mot += pygame.key.name(event.key)

            if displayword.startswith(mot):
                if displayword == mot:
                    score += len(displayword)
                    new_word()
            else:
                game_front_screen()
                time.sleep(2)
                pygame.quit()

    if y_cor < HEIGHT - 5:
        pygame.display.update()
    else:
        game_front_screen()


