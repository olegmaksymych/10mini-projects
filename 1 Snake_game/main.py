from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(600, 600)
screen.bgcolor("grey")
screen.title("The Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
	screen.update()
	time.sleep(0.1)
	snake.move()

#   Detect collision with food.
	if snake.head.distance(food) < 20:
		food.refresh()
		snake.extend()
		scoreboard.increase_score()

# 		Detect collision with wall
	if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
		scoreboard.reset()
		snake.reset()

# 		Detect collision with tail
	for segment in snake.segments[1:]:
		if snake.head.distance(segment) < 10:
			scoreboard.reset()
			snake.reset()


screen.exitonclick()






#
#
# with open("new_file.txt", mode = "a") as file:
# 	file.write("\nNew text 2.")