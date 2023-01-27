from turtle import Screen 
from snake import Snake 
import time 
from food import Food
from scoreboard import Scoreboard



screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Snake Game")

snake = Snake()
food = Food()
scoreboard = Scoreboard()

game_is_on = True


screen.listen()
screen.onkey(fun = snake.go_up, key = "Up")
screen.onkey(fun = snake.go_down, key = "Down")
screen.onkey(fun = snake.go_right, key = "Right")
screen.onkey(fun = snake.go_left, key = "Left")

while game_is_on:
    screen.update()
    time.sleep(.1)
    
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.add_point()
    
    if snake.head.xcor() > 280 or snake.head.xcor()< -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset_scoreboard()
        snake.reset()
    
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 15:
            scoreboard.reset_scoreboard()
            snake.reset()
       


screen.exitonclick()