import time
import turtle
import random


class Snake:
    def __init__(self) -> None:
        self.snake_head = turtle.Turtle()
        self.snake_body = []

        self.snake_head.shape("square")
        self.snake_head.color("white")
        self.snake_head.speed(0)
        self.snake_head.penup()
        self.snake_head.goto(0, 0)
        self.snake_head.direction = "stop"

    
    def go_up(self):
        if self.snake_head.direction != "down":
            self.snake_head.direction = "up"
    def go_down(self):
        if self.snake_head.direction != "up":
            self.snake_head.direction = "down"
    def go_right(self):
        if self.snake_head.direction != "left":
            self.snake_head.direction = "right"
    def go_left(self):
        if self.snake_head.direction != "right":
            self.snake_head.direction = "left"

    def move(self):
        match self.snake_head.direction:
            case "up":
                self.snake_head.sety(self.snake_head.ycor() + 20)
            case "down":
                self.snake_head.sety(self.snake_head.ycor() - 20)
            case "right":
                self.snake_head.setx(self.snake_head.xcor() + 20)
            case "left":
                self.snake_head.setx(self.snake_head.xcor() - 20)

    
class SnakeGame:
    
    
    def __init__(self, snake) -> None:
        self.snake = snake

        self.window = turtle.Screen()
        self.window.bgcolor("black")
        self.window.setup(500, 500)
        self.window.tracer(0)

        self.snake_food = turtle.Turtle()
        self.snake_food.shape("square")
        self.snake_food.color("red")
        self.snake_food.speed(0)
        self.snake_food.penup()
        self.snake_food.goto(0, 150)

        self.game_info = turtle.Turtle()
        self.game_info.color("white")
        self.game_info.hideturtle()
        self.game_info.penup()
        self.game_info.goto(-235, 210)
        self.game_info.write("Press W to start", font=("Courier New", 20, "normal"), align="left")
        self.record_score = 0
        
        self.window.listen()
        self.window.onkeypress(self.snake.go_up, "w")
        self.window.onkeypress(self.snake.go_down, "s")
        self.window.onkeypress(self.snake.go_right, "d")
        self.window.onkeypress(self.snake.go_left, "a")
        

    def run_game(self):
        score = 0
        while True:
            self.window.update()
            
            if self.snake.snake_head.direction != "stop":
                self.game_info.clear()
                self.game_info.write(f"Score - {score} | Best score - {self.record_score}", font=("Courier New", 20, "normal"), align="left")
            

            if self.snake.snake_head.distance(self.snake_food) < 20:
                score += 1
                x_food = random.randint(-230, 230)
                y_food = random.randint(-230, 230)

                x_body, y_body = self.snake.snake_head.pos()
                new_body = turtle.Turtle()
                new_body.shape("square")
                new_body.color("white")
                new_body.speed(0)
                new_body.penup()


                self.snake.snake_body.append(new_body)

                self.snake_food.goto(x_food, y_food)

                

            for i in range(len(self.snake.snake_body) - 1, 0, -1):
                
                snake_body = self.snake.snake_body[i]
                x_body, y_body = self.snake.snake_body[i - 1].pos()
                snake_body.goto(x_body, y_body)


            if len(self.snake.snake_body) > 0:
                x_head, y_head = self.snake.snake_head.pos()
                self.snake.snake_body[0].goto(x_head, y_head)

            if self.snake.snake_head.xcor() > 235 or self.snake.snake_head.xcor() < -235 or self.snake.snake_head.ycor() > 235 or  self.snake.snake_head.ycor() < -235:
                self.snake.snake_head.setpos(0, 0)
                self.snake.snake_head.direction = "stop"
                
                for del_sb in self.snake.snake_body:
                    del_sb.hideturtle()

                self.snake.snake_body = []
                self.snake_food.clear()
                self.game_info.clear()

                self.game_info.write("Press W to start", font=("Courier New", 20, "normal"), align="left")

                score = 0

            for sb in self.snake.snake_body[1:]:
                if sb.distance(self.snake.snake_head) < 20:
                    self.snake.snake_head.setpos(0, 0)
                    self.snake.snake_head.direction = "stop"

                    for del_sb in self.snake.snake_body:
                        del_sb.hideturtle()

                    self.snake.snake_body = []
                    self.snake_food.clear()

                    self.game_info.clear()
                    self.game_info.write("Press W to start", font=("Courier New", 20, "normal"), align="left")
  
                    
                    score = 0

            self.snake.move()
              
            if self.record_score < score:
                self.record_score = score
            
            time.sleep(0.1)
        

snake = Snake()
game = SnakeGame(snake)
game.run_game()
