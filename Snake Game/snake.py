from turtle import Turtle

STARTING_POS = [(20, 0), (0, 0), (-20, 0)]
DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    def __init__(self):
        self.segments =[]
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i in STARTING_POS:
            self.add_segment(i)
    def add_segment(self, position):
        segment = Turtle()
        segment.penup()
        segment.shape("square")
        segment.color("white")
        segment.goto(position)
        self.segments.append(segment)
    def extend(self):
        self.add_segment(self.segments[-1].position())
    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            self.segments[seg_num].goto(self.segments[seg_num-1].pos())
        self.head.fd(DISTANCE)
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
