from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
POSITIONS = [(20, 0), (0, 0), (-20, 0)]


class Snake:
    def __init__(self):
        self.segment_list = []
        self.create_segment()
        self.head = self.segment_list[0]

    def create_segment(self):

        for position in POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        segment = Turtle()
        segment.color("white")
        segment.shape("square")
        segment.penup()
        segment.goto(position)
        self.segment_list.append(segment)

    def extend(self):
        self.add_segment(self.segment_list[-1].position())

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
    def reset(self):

        for seg in self.segment_list:
            seg.goto(10000,10000)
        self.segment_list.clear()
        self.create_segment()
        self.head = self.segment_list[0]
