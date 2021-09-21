from turtle import Screen
import time
from snake import Snake
from food import Food

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Yuki's snake game")
screen.tracer(0)

snake = Snake()
food = Food()

screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

#my version
#segment_x_position = 0
#
#for _ in range(0, 3):
#    segment = Turtle(shape="square")
#    segment.color("white")
#    segment.pu()
#    segment.goto(x=segment_x_position, y=0)
#    segment_x_position -= 20


#angela's version

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    #detect collistion with food using distance method from Turtle
    if snake.head.distance(food) < 12:
        food.refresh()








screen.exitonclick()