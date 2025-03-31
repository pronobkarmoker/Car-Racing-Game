import pygame
import random

# Initialize Pygame
pygame.init()

# Game Constants
WIDTH, HEIGHT = 250, 600
CAR_SPEED = 5
OBSTACLE_SPEED = 5

# Colors
WHITE = (255, 255, 255)
GRAY = (50, 50, 50)
YELLOW = (255, 255, 0)

# Set up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Racing Game")

# Load Assets
car_img = pygame.image.load("car.png") 
obstacle_img = pygame.image.load("obstacle.png")  

# Resize images
car_img = pygame.transform.scale(car_img, (50, 100))
obstacle_img = pygame.transform.scale(obstacle_img, (80, 100))

# Font for displaying score
font = pygame.font.Font(None, 36)

# Player Class
class Player:
    def __init__(self):
        self.x = WIDTH // 2 - 25
        self.y = HEIGHT - 120
        self.speed = CAR_SPEED

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x < WIDTH - 50:
            self.x += self.speed

    def draw(self):
        screen.blit(car_img, (self.x, self.y))

# Obstacle Class
class Obstacle:
    def __init__(self):
        self.x = random.randint(50, WIDTH - 50)
        self.y = -100
        self.speed = OBSTACLE_SPEED

    def move(self):
        self.y += self.speed

    def draw(self):
        screen.blit(obstacle_img, (self.x, self.y))

# Game Setup
player = Player()
obstacles = [Obstacle()]
running = True
clock = pygame.time.Clock()
score = 0

while running:
    screen.fill(GRAY)  

    for i in range(0, HEIGHT, 40):
        pygame.draw.rect(screen, WHITE, (WIDTH // 2 - 5, i, 10, 20)) 

    keys = pygame.key.get_pressed()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    player.move(keys)
    player.draw()
    
    for obstacle in obstacles:
        obstacle.move()
        obstacle.draw()

        if (player.x < obstacle.x + 50 and player.x + 50 > obstacle.x and
            player.y < obstacle.y + 100 and player.y + 100 > obstacle.y):
            running = False
        
        if obstacle.y > HEIGHT:
            obstacles.remove(obstacle)
            obstacles.append(Obstacle())
            score += 1

    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))
    
    pygame.display.update()
    clock.tick(30)

# Display Final Score
screen.fill(GRAY)
final_score_text = font.render(f"Final Score: {score}", True, (255, 0, 0)) 
screen.blit(final_score_text, (WIDTH // 2 - final_score_text.get_width() // 2, HEIGHT // 2 - final_score_text.get_height() // 2))
pygame.display.update()
pygame.time.wait(2000) 

pygame.quit()
