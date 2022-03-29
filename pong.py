import turtle as t
import os 

playerAscore=0
playerBscore=0

#creating a window and declaring a variable called window

window=t.Screen()
window.title("The Ping-Pong Game")
window.bgcolor("#4DED30")
window.setup(width=800,height=600)
window.tracer(0)

#Left Paddle

leftpaddle=t.Turtle()
leftpaddle.speed(0)
leftpaddle.shape("square")
leftpaddle.color("black")
leftpaddle.shapesize(stretch_wid=5,stretch_len=1)
leftpaddle.penup()
leftpaddle.goto(-350,0)

# Right Paddle

rightpaddle=t.Turtle()
rightpaddle.speed(0)
rightpaddle.shape("square")
rightpaddle.color("black")
rightpaddle.shapesize(stretch_wid=5,stretch_len=1)
rightpaddle.penup()
rightpaddle.goto(350,0)

#Creating the ball

ball=t.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("purple")
ball.shapesize(stretch_wid=1.2,stretch_len=1.2)
ball.penup()
ball.goto(0,0)
ballXdirection=1
ballYdirection=1

#Creating pen for scorecard update
pen=t.Turtle()
pen.speed(0)
pen.color("Blue")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0                    Player B: 0 ",align="center",font=('Arial',20,"normal"))


# Moving the left Paddle using the keyboard

def leftpaddle_up():
    y=leftpaddle.ycor()
    y = y + 20
    leftpaddle.sety(y)
    
def leftpaddle_down():
    y=leftpaddle.ycor()
    y = y - 20
    leftpaddle.sety(y)
    
    # Moving the right Paddle using the keyboard

def rightpaddle_up():
    y=rightpaddle.ycor()
    y = y + 20
    rightpaddle.sety(y)
    
def rightpaddle_down():
    y=rightpaddle.ycor()
    y = y - 20
    rightpaddle.sety(y)

# Keyboard binding
window.listen()
window.onkeypress(leftpaddle_up,"w")
window.onkeypress(leftpaddle_down,"s")
window.onkeypress(rightpaddle_up,"Up")
window.onkeypress(rightpaddle_down,"Down")

#Game 's Main Loop

while True:
    window.update() #Important method to run any game
    
    #Ball Movement
    ball.setx(ball.xcor() + ballXdirection)
    ball.sety(ball.ycor() + ballYdirection)
    
    #Border set-up
    if ball.ycor() > 290:   # Right top paddle Border
        ball.sety(290)
        ballYdirection = ballYdirection * -1
    
    if ball.ycor() < -290:  # Left top paddle Border
        ball.sety(-290)
        ballYdirection = ballYdirection * -1
        
    if ball.xcor() > 390:   # right width paddle Border
        ball.goto(0,0)
        ballXdirection = ballXdirection * -1
        playerAscore = playerAscore + 1
        pen.clear()
        pen.write("Player A: {}                 Player B: {} ".format(playerAscore,playerBscore),align="center",font=('Monaco',24,"normal"))
        os.system("afplay wallhit.wav&")
        
    if(ball.xcor()) < -390: # Left width paddle Border
        ball.goto(0,0)
        ballXdirection = ballXdirection * -1
        playerBscore = playerBscore + 1
        pen.clear()
        pen.write("Player A: {}                 Player B: {} ".format(playerAscore,playerBscore),align="center",font=('Monaco',24,"normal"))
        os.system("afplay wallhit.wav&")
        
        
    # Handling the collisions with paddles.

    if(ball.xcor() > 340) and (ball.xcor() < 350) and (ball.ycor() < rightpaddle.ycor() + 40 and ball.ycor() > rightpaddle.ycor() - 40):
        ball.setx(340)
        ballXdirection = ballXdirection * -1
        os.system("afplay paddle.wav&")

    if(ball.xcor() < -340) and (ball.xcor() > -350) and (ball.ycor() < leftpaddle.ycor() + 40 and ball.ycor() > leftpaddle.ycor() - 40):
        ball.setx(-340)
        ballXdirection = ballXdirection * -1
        os.system("afplay paddle.wav&")
