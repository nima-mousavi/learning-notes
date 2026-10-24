from turtle import Turtle

# Text alignment and font settings for the scoreboard.
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        # Redraw the score at the top of the screen.
        self.clear()
        self.goto(0, 260)
        self.write(
            f"Score: {self.score}",
            align=ALIGNMENT,
            font=FONT,
        )

    def increase_score(self):
        # Update the score and refresh its display.
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        # Display the game-over message in the center of the screen.
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
