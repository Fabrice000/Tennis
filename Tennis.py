import pygame
import sys
import random

# initialisation

pygame.init()

# constantes de jeu

WIDTH, HEIGHT = 800, 600
FPS = 60
font = pygame.freetype.Font(None,24)
# couleurs

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# fenetre de jeu

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Jeu de Tennis")

# joueurs

player1 = pygame.Rect(50, HEIGHT // 2 - 50, 10, 100)
player2 = pygame.Rect(WIDTH - 60, HEIGHT // 2 - 50, 10, 100)

# ballon

ball = pygame.Rect(WIDTH // 2 - 15, HEIGHT // 2 - 15, 30, 30)
ball_speed_x = 5
ball_speed_y = 5

# scores

score_player_1 = 0
score_player_2 = 0

# etat du game over

game_over = False

# vitesse du joueur automatique

auto_player_speed = 5

# boucle du jeu

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if not game_over:
        # joueur 1 au controle
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and player1.top > 0:
            player1.y -= 5
        if keys[pygame.K_DOWN] and player1.bottom < HEIGHT:
            player1.y += 5
        if keys[pygame.K_LEFT] and player1.left > 0:
            player1.x -= 5
        if keys[pygame.K_RIGHT] and player1.right < WIDTH // 2:
            player1.x += 5
# mouvement du joueur 2
        if ball.centery < player2.centery and player1.top > 0:
            player2.y -= auto_player_speed
        elif ball.centery > player2.centery and player2.bottom < HEIGHT:
            player2.y += auto_player_speed

        # mouvement du ballon

        ball.x += ball_speed_x
        ball.y += ball_speed_y

        # collision du ballon avec les bords du haut et du bas
        if ball.top <= 0 or ball.bottom >= HEIGHT:
            ball_speed_y = -ball_speed_y

        # collision de la balle avec les joueurs

        if ball.colliderect(player1) or ball.colliderect(player2):
            ball_speed_x = -ball_speed_x

        # sorti du ballon

        if ball.left <= 0:
            score_player_2 += 1
            ball_speed_x = abs(ball_speed_x)
            ball_speed_y = random.choice([-5, 5])
            ball.x = WIDTH // 2 - 15
            ball.y = HEIGHT // 2 - 15
        if ball.right >= WIDTH:
            score_player_1 += 1
            ball_speed_x = -abs(ball_speed_x)
            ball_speed_y = random.choice([-5, 5])
            ball.x = WIDTH // 2 - 15
            ball.y = HEIGHT // 2 - 15

        # effacer l'ecran

    screen.fill(BLACK)

    # dessiner les joueurs et le ballon

    pygame.draw.rect(screen, WHITE, player1)
    pygame.draw.rect(screen, WHITE, player2)
    pygame.draw.ellipse(screen, WHITE, ball)
    # dessin des scores

    #score_display = font.render(f"{score_player_1} - {score_player_2}", True, WHITE)
    #screen.blit(score_display, (WIDTH // 2 - 40, 10))

    # actualiser l'ecran

    pygame.display.update()

    # vitesse du jeu
    clock = pygame.time.Clock()
    clock.tick(FPS)

    # condition de fin de jeu
    if score_player_1 >= 5 or score_player_2 >= 5:
        game_over = True

# afficher le gagnant
winner = "Player 1" if score_player_1 >= 5 else "Player 2"
winner_display = font.render(f"Game over {winner} wins", True,WHITE)
screen.blit(winner_display, (WIDTH // 2 - 150, HEIGHT // 2 -18))
pygame.display.update()

# attendre quelques moments

pygame.time.wait(3000)
pygame.quit()
sys.exit()




