from turtle import  Turtle
class Scoreboard(Turtle):
    def __init__(self):
        self.score = 0
        super().__init__()
        self.hideturtle()
        self.speed("fastest")
        self.penup()
        self.color("white")
        self.goto(0, 260)
        self.update_scoreboard()
    def increase_score(self):
        self.score +=1

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score}", font=('Arial', 20, "bold"), align="center")
    def game_over(self):
        self.goto(0,0)
        self.write(arg="GAME OVER!", font=('Arial', 20, "bold"), align="center")



