from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.penup()
        self.goto(0, 265)
        self.hideturtle()

    def gameover(self):
        self.goto(0, 150)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
        self.goto(0, 100)
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font =FONT)
        
    def increase_score(self):
        self.score +=1
        self.clear()
        self.update_scoreboard()  
