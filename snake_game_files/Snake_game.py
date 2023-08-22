from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
screen = Screen()
def main_game():

    screen = Screen()
    screen.clear()
    screen.setup(width = 600, height = 590)
    screen.title("Snake Game")
    screen.addshape("img/snakehead.gif")
    screen.bgpic('img/snakebackground.gif')
    screen.tracer(0)
    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()
    screen.listen()
    screen.onkey(snake.up,"w")
    screen.onkey(snake.down, "s")
    screen.onkey(snake.left, "a")
    screen.onkey(snake.right, "d")

    game_is_on = True  

    while game_is_on:    
        screen.update()
        time.sleep(0.1)
        snake.move()
        if snake.head.distance(food)  < 15:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()

        if snake.head.xcor() >280 or snake.head.xcor() < -300 or snake.head.ycor() > 295 or snake.head.ycor() <- 280:
            game_is_on = False
            scoreboard.gameover()
            again =screen.textinput("GAME OVER", "Would you like the play again?")

            if again == "yes":
                main_game()          

        for segment in snake.segments:
            if segment == snake.head:
                pass

            elif snake.head.distance(segment) <10:
                game_is_on = False
                scoreboard.gameover()
                again =screen.textinput("GAME OVER", "Would you like the play again?")

                if again == "yes":
                    main_game()   
main_game()
screen.exitonclick()
