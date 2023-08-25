import random
import pygame
class Apple(object):
    def __init__(self, rows, cols):
        self.apple_position = [5, 5]
        self.rows = rows
        self.cols = cols

    def generate_apple(self, player):
        while True:
            row = random.randint(0, self.rows - 1)
            col = random.randint(0, self.cols - 1)
            if tuple([row, col]) not in player.body_set:
                self.apple_position = [row, col]
                return
    def paint(self, screen, cell_size):
        row, col = self.apple_position
        cell_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
        pygame.draw.rect(screen, pygame.Color([0.5,0,0]), cell_rect)





