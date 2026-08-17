from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()

GAME = True

screen.bgcolor("black")
screen.setup(600, 600)
screen.title("The Snake Game")
screen.tracer(0)

scoreboard = Scoreboard()
food = Food()
snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

while GAME:
    time.sleep(0.1)
    screen.update()

    snake.move()

    if snake.head.distance(food) < 15:
        food.spawn()
        snake.extend()
        scoreboard.increase_score()
        scoreboard.update_scoreboard()

    if (snake.head.xcor() > 280 or
            snake.head.xcor() < -280 or
            snake.head.ycor() > 280 or
            snake.head.ycor() < -280):
        scoreboard.reset()
        snake.reset()


    for segment in snake.segment_list[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()

