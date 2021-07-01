import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=600, height=600)
# Screen background color
screen.bgcolor('black')
screen.title('My Snake Game')
#Causes the animation to display only when update is called
screen.tracer(0)

#################################
# -------------------------------
# Creating the Snake Body
# -------------------------------
#################################

snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Feeds key presses into python
screen.listen()
# Methods or functions within a function do not have ()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


#################################
# -------------------------------
# Move the Snake
# -------------------------------
#################################

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.refresh_scoreboard()

    # Detect collision with wall
    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        scoreboard.game_over()
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail
    # If head collides with any segment in the tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.game_over()
            scoreboard.reset()
            snake.reset()

screen.exitonclick()













screen.exitonclick()
