from turtle import Turtle


class scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        with open("data.txt") as file:
            self.highscore = int(file.read())
        self.hideturtle()
        self.penup()
        self.goto(0, 265)
        self.write(f" Score : {self.score} Highscore: {self.highscore}", False, "center", font=("Arial", 20, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f" Score : {self.score} Highscore: {self.highscore}", False, "center", font=("Arial", 20, "normal"))

    def rest(self):
        if self.score>self.highscore:
            self.highscore = self.score
            with open("data.txt",mode="w") as file:
                file.write(f"{self.highscore}")

        self.score = 0
        self.clear()
        self.write(f" Score : {self.score} Highscore: {self.highscore}", False, "center", font=("Arial", 20, "normal"))

    # def gameover(self):
    #     self.goto(0,0)
    #     self.write(f"Game Over", False, "center", font=("Arial", 24, "normal"))


