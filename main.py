import pygame
import sys

# Inicializar o Pygame
pygame.init()

# Configurações da tela
width, height = 1280, 720
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Robo bom")

# Carregar a imagem do jogador
player_image = pygame.image.load('Robo.png')  # Substitua 'player.png' pelo caminho correto da sua imagem
player_image = pygame.transform.scale(player_image, (120, 150))  # Redimensionar a imagem para 50x50 pixels

player_rect = player_image.get_rect()

# Posição inicial do jogador
player_rect.center = [width // 2, height // 2]

# Velocidade do jogador
speed = 5

# Definindo as bordas da tela (paredes)
left_wall = 0
right_wall = width
top_wall = 0
bottom_wall = height

# Clock para controlar o FPS
clock = pygame.time.Clock()

# Loop do jogo
running = True
while running:
    # Verificar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Verificar as teclas pressionadas
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_rect.left > left_wall:
        player_rect.x -= speed
    if keys[pygame.K_RIGHT] and player_rect.right < right_wall:
        player_rect.x += speed
    if keys[pygame.K_UP] and player_rect.top > top_wall:
        player_rect.y -= speed
    if keys[pygame.K_DOWN] and player_rect.bottom < bottom_wall:
        player_rect.y += speed

    # Preencher o fundo
    screen.fill((0, 0, 255))

    # Desenhar a imagem do jogador
    screen.blit(player_image, player_rect)

    # Atualizar a tela
    pygame.display.flip()

    # Limitar a 60 FPS
    clock.tick(120)

# Sair do Pygame
pygame.quit()
sys.exit()