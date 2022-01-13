from turtle import Screen
import time
from food import Food
from snake import Snake
from score import scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        print("nom nom nom")
        food.refresh()
        score.increase_score()
        snake.extend()

    # detect collision with wall
    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.xcor() < -285:
        snake.rest()
        score.rest()

    # detect collision with any segment in tail
    for segment in snake.segments[1:]:

        if snake.head.distance(segment) < 10:
            snake.rest()
            score.rest()

screen.exitonclick()
