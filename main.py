import pygame
import random
import sys

# Emojis
PLAYER_EMOJI = "🚲"
HOUSE_EMOJI = "🏠"
OBSTACLE_EMOJIS = ["⛔", "🚧", "🛞", "🚦", "🪤"]
PAPER_EMOJI = "📰"

# Initialize Pygame
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paperboy Arcade Game")
clock = pygame.time.Clock()
FONT = pygame.font.SysFont(None, 40)
EMOJI_FONT = pygame.font.SysFont(None, 64)  # Large font for emojis

# Game variables
player_x = WIDTH // 2
player_y = HEIGHT - 120
player_speed = 6
papers = []
obstacles = []
houses = []
score = 0
lives = 3
scroll_speed = 4

def spawn_house():
    x = random.randint(100, WIDTH-180)
    y = -100
    houses.append({'rect': pygame.Rect(x, y, 64, 64), 'delivered': False})

def spawn_obstacle():
    x = random.randint(100, WIDTH-100)
    y = -100
    emoji = random.choice(OBSTACLE_EMOJIS)
    obstacles.append({'rect': pygame.Rect(x, y, 64, 64), 'emoji': emoji})

def draw():
    screen.fill((30, 180, 30))  # Grass
    # Street
    pygame.draw.rect(screen, (90, 90, 90), (80, 0, WIDTH-160, HEIGHT))

    # Draw houses
    for house in houses:
        emoji_img = EMOJI_FONT.render(HOUSE_EMOJI, True, (255,255,255))
        screen.blit(emoji_img, house['rect'].topleft)
        if house['delivered']:
            pygame.draw.rect(screen, (255, 255, 0), house['rect'], 3)

    # Draw obstacles
    for obs in obstacles:
        emoji_img = EMOJI_FONT.render(obs['emoji'], True, (255,255,255))
        screen.blit(emoji_img, obs['rect'].topleft)

    # Draw papers
    for p in papers:
        emoji_img = EMOJI_FONT.render(PAPER_EMOJI, True, (255,255,255))
        screen.blit(emoji_img, (p['x'], p['y']))

    # Draw player (bike)
    emoji_img = EMOJI_FONT.render(PLAYER_EMOJI, True, (255,255,255))
    screen.blit(emoji_img, (player_x, player_y))

    # Draw HUD
    score_text = FONT.render(f"Score: {score}", True, (255,255,255))
    lives_text = FONT.render(f"Lives: {lives}", True, (255,0,0))
    screen.blit(score_text, (10, 10))
    screen.blit(lives_text, (WIDTH - 150, 10))

def reset_game():
    global player_x, player_y, papers, obstacles, houses, score, lives
    player_x = WIDTH // 2
    player_y = HEIGHT - 120
    papers = []
    obstacles = []
    houses = []
    score = 0
    lives = 3

# Main loop
running = True
spawn_timer = 0
obstacle_timer = 0
while running:
    clock.tick(60)
    spawn_timer += 1
    obstacle_timer += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Throw paper
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                papers.append({'x': player_x+20, 'y': player_y, 'vy': -8})

    # Move player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 80:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH-128:
        player_x += player_speed
    if keys[pygame.K_UP] and player_y > 0:
        player_y -= player_speed
    if keys[pygame.K_DOWN] and player_y < HEIGHT-48:
        player_y += player_speed

    # Spawn houses and obstacles
    if spawn_timer > 90:
        spawn_house()
        spawn_timer = 0
    if obstacle_timer > 70:
        spawn_obstacle()
        obstacle_timer = 0

    # Move houses & obstacles down screen
    for house in houses:
        house['rect'].y += scroll_speed
    for obs in obstacles:
        obs['rect'].y += scroll_speed

    # Move papers
    for p in papers:
        p['y'] += p['vy']

    # Check for collisions and delivery
    for house in houses[:]:
        if house['rect'].y > HEIGHT:
            houses.remove(house)
            continue
        for p in papers[:]:
            paper_rect = pygame.Rect(p['x'], p['y'], 48, 48)
            if house['rect'].colliderect(paper_rect) and not house['delivered']:
                house['delivered'] = True
                score += 100
                papers.remove(p)
    for obs in obstacles[:]:
        if obs['rect'].y > HEIGHT:
            obstacles.remove(obs)
            continue
        # Player collision
        player_rect = pygame.Rect(player_x, player_y, 48, 48)
        if player_rect.colliderect(obs['rect']):
            lives -= 1
            obstacles.remove(obs)
            if lives <= 0:
                reset_game()

    # Remove old papers
    papers = [p for p in papers if p['y'] > -20]

    draw()
    pygame.display.flip()
