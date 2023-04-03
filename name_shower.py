from turtle import Turtle


class Name(Turtle):
    def __init__(self):
        super(Name, self).__init__()
        self.hideturtle()
        self.penup()

    def move(self, x_cor, y_cor):
        self.goto(x_cor, y_cor)

    def correct(self, answer):
        self.write(f"{answer}", align="center", font=("Courier", 14, "bold"))
