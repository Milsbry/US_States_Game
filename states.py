from turtle import Turtle, Screen


class States(Turtle):
    def __init__(self, font: str = 'Arial'):
        super().__init__()
        self.font_size = None
        self.colour = None
        self.state = None
        self.y = None
        self.x = None
        self.font = font
        self.penup()
        self.hideturtle()
        self.screen = Screen()
        self.screen.tracer(0)  # Stops the turtles animations until screen.refresh is called

    def add_state(self, state: str = '', x: float = 0, y: float = 0, font_size: int = 8, colour: str = "black"):
        self.state = state
        self.font_size = font_size
        self.color(colour)
        self.x = x
        self.y = y
        self.goto(self.x, self.y)
        self.write(arg=self.state, move=False, align='center', font=(self.font, self.font_size, 'normal'))
        self.screen.tracer(1)
