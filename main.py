from turtle import Turtle,Screen
import time
from snake import Snake



# def create_segment(n):
#     segment_list = []
#     for _ in range(n):
#         segment = Turtle()
#         segment.color("white")
#         segment.shape("square")
#         segment.penup()
#         segment_list.append(segment)
#     return segment_list
#
# def segment_postioner(l:list):
#     xcord = 0
#     for segment in l:
#         segment.goto(xcord,0)
#         xcord +=20
screen = Screen()
screen.bgcolor("black")
screen.setup(600,600)
screen.title("The snake game".title())
screen.tracer(0)


snake = Snake()
snake.create_segment(3)
snake.segment_positioner()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

while True:
    time.sleep(0.1)
    screen.update()
    snake.move()





screen.exitonclick()