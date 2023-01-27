from turtle import Turtle 

FONT = ("Courier", 24, "normal" )
class Scoreboard(Turtle):
    def __init__(self):
        super(). __init__()
        self.penup()
        self.score = 0
        with open("/Users/neal/Library/Mobile Documents/com~apple~CloudDocs/VS_CODE/my_snake_game/data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.goto(0,270)
        self.hideturtle()
        self.update_scoreboard()
        
        
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align= "center", font = FONT)

    
    def add_point(self):
        self.score += 1
        self.update_scoreboard()
    

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align= "center", font = FONT)
    

    def reset_scoreboard(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("/Users/neal/Library/Mobile Documents/com~apple~CloudDocs/VS_CODE/my_snake_game/data.txt", mode ="w") as data:
                data.write(str(self.score))
        self.score = 0
        self.update_scoreboard()
        