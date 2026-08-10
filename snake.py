from turtle import Turtle
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.segment_list = []
        self.create_segment(3)
        self.head = self.segment_list[0]

    def create_segment(self,n):
            
        for _ in range(n):
            segment = Turtle()
            segment.color("white")
            segment.shape("square")
            segment.penup()
            self.segment_list.append(segment)

    def segment_positioner(self):
        x_cord = 0
        for segment in self.segment_list:
            segment.goto(x_cord, 0)
            x_cord += 20
    def move(self):
        for seg_num in range(len(self.segment_list) - 1, 0, -1):
            new_x = self.segment_list[seg_num - 1].pos()[0]
            new_y = self.segment_list[seg_num - 1].pos()[1]
            self.segment_list[seg_num].goto(new_x, new_y)
        self.head.forward(20)
    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)
