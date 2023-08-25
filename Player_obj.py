from collections import deque
import pygame

class Player(object):
    def __init__(self, num_rows, num_cols, pos_x, pos_y, direction = 'R'):
        self.head_position = [pos_x, pos_y]
        self.direction = 'R'
        self.last_direction = 'R'
        self.rows = num_rows
        self.cols = num_cols
        self.body_queue = deque()
        self.body_queue.appendleft(self.head_position.copy())
        self.body_set = set()
        self.body_set.add(tuple(self.head_position))

    def set_direction(self, new_direction):
        if new_direction == 'R':
            if self.last_direction == 'L':
                return 
        elif new_direction== 'L':
            if self.last_direction == 'R':
                return 
        elif new_direction== 'U':
            if self.last_direction == 'D':
                return 
        elif new_direction== 'D':
            if self.last_direction == 'U':
                return 

        self.direction = new_direction

    def move(self, apple):
        self.last_direction = self.direction
        if self.direction == 'R':
            self.head_position[1] += 1
        elif self.direction == 'L':
            self.head_position[1] -= 1
        elif self.direction == 'U':
            self.head_position[0] -= 1
        elif self.direction == 'D':
            self.head_position[0] += 1

        if self.detect_collision():
            return 1

        self.body_queue.appendleft(self.head_position.copy())
        self.body_set.add(tuple(self.head_position))
        if self.head_position == apple.apple_position:
            apple.generate_apple(self)
        else:
            tail_position = self.body_queue.pop()
            self.body_set.discard(tuple(tail_position))


    def paint(self, screen, cell_size):
        for col, row in self.body_set:
            cell_rect = pygame.Rect(row * cell_size, col * cell_size, cell_size, cell_size)
            pygame.draw.rect(screen, pygame.Color('black'), cell_rect)

    def detect_collision(self):
        head = self.head_position
        
        # Check if the head is out of bounds
        if head[0] < 0 or head[0] >= self.rows or head[1] < 0 or head[1] >= self.cols:
            return True
        
        # Check if the head collides with the body
        if tuple(head)in self.body_set:
            return True
        
        return False