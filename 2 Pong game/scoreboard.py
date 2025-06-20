from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):
	def __init__(self, position):
		super().__init__()
		self.score = 0
		self.color("white")
		self.penup()
		self.goto(position, 260)
		self.update_scoreboard()
		self.hideturtle()

	def update_scoreboard(self):
		self.write(f"{self.score}", align="left", font=FONT)

	def game_over(self):
		self.goto(0,0)
		self.write("GAME OVER", align=ALIGNMENT, font=FONT)

	def increase_score(self):
		self.score += 1
		self.clear()
		self.update_scoreboard()