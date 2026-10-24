import turtle

# Game movement settings and direction angles.
SNAKE_SEGMENTS_SIZE = 20
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
WALL_LIMIT = 280


class Snake:

    def __init__(self):
        self.snake_segments = []
        self.make_snake()
        self.head = self.snake_segments[0]  # The first segment controls movement.

    def make_snake(self):
        # Create the initial three-segment snake.
        for position in [(0, 0), (-20, 0), (-40, 0)]:
            self.add_segment(position)

    def add_segment(self, position):
        # Place each new segment behind the existing segments.
        snake_segment = turtle.Turtle(shape="square")
        snake_segment.color("white")
        snake_segment.penup()
        snake_segment.goto(position)
        self.snake_segments.append(snake_segment)

    def extend(self):
        self.add_segment(self.snake_segments[-1].position())

    def move(self):
        # Move each segment to the previous segment's position,
        # starting from the tail to preserve the snake's shape.
        for index in range(len(self.snake_segments) - 1, 0, -1):
            self.snake_segments[index].goto(
                self.snake_segments[index - 1].xcor(),
                self.snake_segments[index - 1].ycor(),
            )
        # Move the head forward to lead the snake.
        self.snake_segments[0].forward(MOVE_DISTANCE)

    def is_collision_with_tail(self):
        # Check the head against every body segment, excluding itself.
        for segment in self.snake_segments[1:]:
            if self.head.distance(segment) < 10:
                return True
        return False

    def is_collision_with_wall(self):
        # Detect when the head crosses the play area's boundaries.
        return abs(self.head.xcor()) > WALL_LIMIT or abs(self.head.ycor()) > WALL_LIMIT

    # Direction controls prevent immediate 180-degree turns.
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
