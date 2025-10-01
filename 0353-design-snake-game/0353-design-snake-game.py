from collections import deque
from typing import List

class SnakeGame:
    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.width = width
        self.height = height
        self.food = food
        self.snake = deque([(0, 0)])
        self.snake_set = set([(0, 0)])
        self.food_index = 0
        self.score = 0
        self.directions = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}

    def move(self, direction: str) -> int:
        head_row, head_col = self.snake[0]
        delta_row, delta_col = self.directions[direction]
        new_row, new_col = head_row + delta_row, head_col + delta_col

        # Check collision with wall
        if not (0 <= new_row < self.height and 0 <= new_col < self.width):
            return -1

        # Check if new position hits the snake itself (except the tail, which will slide forward)
        tail = self.snake.pop()
        self.snake_set.remove(tail)
        if (new_row, new_col) in self.snake_set:
            return -1

        self.snake.appendleft((new_row, new_col))
        self.snake_set.add((new_row, new_col))

        # Check food
        if (self.food_index < len(self.food)) and ([new_row, new_col] == self.food[self.food_index]):
            self.score += 1
            self.food_index += 1
            # Put back the tail (grow snake)
            self.snake.append(tail)
            self.snake_set.add(tail)
        # Otherwise, already popped the tail (move forward)

        return self.score


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)