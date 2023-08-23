import pygame

class Grid(object):
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols


    def paint(self, screen, cell_size):
        for row in range(self.rows):
            for col in range(self.cols):
                cell_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                pygame.draw.rect(screen, pygame.Color('black'), cell_rect, 1)






