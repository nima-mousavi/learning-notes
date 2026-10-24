import time
from turtle import Screen

from food import Food
from scoreboard import Scoreboard
from snake import Snake

# Set up the game window.
SCREEN_SIZE = 600
GAME_SPEED = 0.1
screen = Screen()
screen.setup(width=SCREEN_SIZE, height=SCREEN_SIZE)
screen.title("Snake")
screen.bgcolor("black")
screen.tracer(0)

# Create the game objects.
snake = Snake()
food = Food()
food.make_food(snake.snake_segments)
scoreboard = Scoreboard()

# Listen for keyboard input and control the snake's direction.
screen.listen()
screen.onkey(key="d", fun=snake.right)
screen.onkey(key="w", fun=snake.up)
screen.onkey(key="a", fun=snake.left)
screen.onkey(key="s", fun=snake.down)


# Main game loop.
game_is_on = True
while game_is_on:
    screen.update()  # Refresh the screen after drawing changes.
    time.sleep(GAME_SPEED)
    snake.move()

    # Check whether the snake has eaten the food.
    if snake.head.distance(food) < 15:
        snake.extend()
        food.make_food(snake.snake_segments)
        scoreboard.increase_score()

    # End the game if the snake hits a wall or its own body.
    if snake.is_collision_with_wall() or snake.is_collision_with_tail():
        scoreboard.game_over()
        game_is_on = False


screen.exitonclick()
