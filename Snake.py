import pygame
from Grid_obj import Grid
from Player_obj import Player


pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
GRID_ROWS = 20
GRID_COLS = 10


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tower Defense Game")

# Create a timer event
TIMER_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(TIMER_EVENT, 200)  # 1000 milliseconds (1 second)


clock = pygame.time.Clock()
grid = Grid(GRID_ROWS,GRID_COLS)
player = Player(GRID_ROWS, GRID_COLS, 1,1)

running = True
is_game_over = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == TIMER_EVENT:
            is_game_over = player.move()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False
            elif event.key == pygame.K_w:
                player.set_direction('U')
            elif event.key == pygame.K_a:
                player.set_direction('L')            
            elif event.key == pygame.K_s:
                player.set_direction('D')           
            elif event.key == pygame.K_d:
                player.set_direction('R')

    # Game logic and updates go here
    cell_size = min(SCREEN_WIDTH // GRID_COLS, SCREEN_HEIGHT // GRID_ROWS)


    if (is_game_over):
        running = False


    # Draw game objects
    screen.fill((0, 20, 0))
    grid.paint(screen, cell_size)
    player.paint(screen, cell_size)

    # Update the display
    pygame.display.flip()