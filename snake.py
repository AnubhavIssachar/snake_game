from turtle import Turtle, Screen

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
LEFT = 180
RIGHT = 0
DOWN = 270

screen = Screen()


class Snake:
    def __init__(self):
        self.snake_segments = []
        self.create_snake()
        self.head = self.snake_segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        my_snake = Turtle("square")
        my_snake.color("white")
        my_snake.penup()
        my_snake.goto(x=position, y=None)
        self.snake_segments.append(my_snake)

    def extend(self):
        self.add_segment(self.snake_segments[-1].position())

    def move(self):
        for snake_seg in range(len(self.snake_segments) - 1, 0, -1):
            new_x = self.snake_segments[snake_seg - 1].xcor()
            new_y = self.snake_segments[snake_seg - 1].ycor()
            self.snake_segments[snake_seg].goto(new_x, new_y)
        self.head.forward(20)

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
