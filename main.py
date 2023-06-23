from turtle import Turtle, Screen

tommy = Turtle()
screen = Screen()

# simple etch-a-sketch program
def move_forward():
    tommy.forward(10)

def move_backward():
    tommy.backward(10)

def turn_left():
    tommy.left(10)

def turn_right():
    tommy.right(10)

def start_again():
    tommy.reset()

screen.listen()
# higher order functions can be used to call/control other functions
# when using methods like .onkey below, pass keyword arguments to prevent confusion.
screen.onkeypress(fun=move_forward, key="w")
screen.onkeypress(fun=move_backward, key="s")
screen.onkeypress(fun=turn_left, key="a")
screen.onkeypress(fun=turn_right, key="d")
screen.onkeypress(fun=start_again, key="c")

screen.exitonclick()