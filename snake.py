from turtle import Turtle

MOVE_DISTANCE = 20
STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
UP = 90
RIGHT = 0
DOWN = 270
LEFT = 180



class Snake():
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
    
    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def move(self):
        for seg_number in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_number -1].xcor()
            new_y = self.segments[seg_number -1].ycor()
            self.segments[seg_number].goto(x = new_x, y =new_y)
        self.head.forward(MOVE_DISTANCE)
    
    def extend(self):
        self.add_segment(self.segments[-1].position())


    def go_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


    def go_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    
    def go_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def go_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def reset(self):
        for seg in self.segments:
            seg.goto(500,500)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]