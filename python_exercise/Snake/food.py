import random
from turtle import Turtle


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("orange")
        self.speed("fastest")

    def make_food(self, snake_segments):
        # Choose random coordinates aligned with the snake's movement grid.
        while True:
            x = random.randint(-14, 14) * 20
            y = random.randint(-14, 14) * 20
            self.goto(x, y)

            # Place food only where it does not overlap the snake.
            if all(self.distance(segment) >= 15 for segment in snake_segments):
                return
