import turtle
import winsound #winsound is used to include sounds in your python game.

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
# sets the size and the position of the window
wn.setup(width=800, height=600)
# This function is used to turn turtle animation on or off and set a delay for update drawings.
wn.tracer(0)

#score
score_pla = 0
score_plb = 0

#paddle A
paddle_a = turtle.Turtle()
"""""
You now have your screen and your turtle. The screen acts as a canvas,
while the turtle acts like a pen. You can program the turtle to move around the screen.  
The turtle has certain changeable characteristics, like size, color, and speed. 
It always points in a specific direction, and will move in that direction unless you tell it otherwise.

"""""
paddle_a.speed(0)#https://www.geeksforgeeks.org/turtle-speed-function-in-python/
paddle_a.shape("square")
paddle_a.color("white")

"""""
this is used to strcech the width and leneth of the shape of the paddle which was drawn using,
the (strech_wid, strech len)

"""""
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)#This method is used to move the turtle to an absolute position. This method has Aliases: setpos, setposition, goto.

#paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)#https://www.geeksforgeeks.org/turtle-speed-function-in-python/
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
"""""
This method is used to move the turtle to an absolute position. This method has Aliases: setpos, setposition, goto.
It should be noted that since this is the paddle for the right side of the screen, it should be +350 and not
negative or -350
"""""
paddle_b.goto(350, 0)


#Ball
ball = turtle.Turtle()
ball.speed(0)#https://www.geeksforgeeks.org/turtle-speed-function-in-python/
ball.shape("square")
ball.color("white")
ball.penup()
#Moving the ball
""""" So first, what we want to do is to makke the ball move. And to do so, we need to seperate the movernent of
the ball into two parts. We'll call the one part x and the other part y.
"""""
ball.dx = 0.2
"""""ball.dx(the "d" means delta and delta simply means change. This determines the speed of movernent
of the ball. The x and y signifies the left and right axis of our game. The 0.2 simply means, move the ball,
0.2 mp right for x axis and most likly same for y axis. You could also go with xspeed if you want to.)
"""""
ball.dy = -0.2
"""""Now we have to go the main game loop, to implement this function.
"""""
#scoring
""""" First we create a turtle pen."""""
pen = turtle.Turtle() #this the coand line that activates turtle draw function.
pen.speed(0) #This is the speed of the animation not the movernment speed.
pen.color("white")
pen.penup()#This is code that prevents us from seeing a pen move while its drawing. Withot said code,we would
#see the pen drawing.
pen.hideturtle() #This just generally hides the pen. We just want to see what the pen is writing.
pen.goto(0, 260)
pen.write("player A: 0 Player B: 0", align="center", font=("courier",24))
"""""The pen.write method, writes on the screen. In this case, it will be writing the score of the players
on our screen. align, means where it should stay at, font contains what font should be used, the size of the font """""


# Functions for to move paddles 
# For, first paddle
def paddle_a_up():
    y = paddle_a.ycor() #so, what this does is that it returns the value of the obect(paddle_a) ycordinates.
    #tied to a variable called Y   
    y +=20 #so, we re adding 20px to the y cordinates.
    paddle_a.sety(y) #so, what this does is replace the old .ycord, with the new one.(ie the one added with the 20px,)               

def paddle_a_down(): #This for the down movernents for the first paddle
    y = paddle_a.ycor()   
    y -=20 # Instead of +(which is for moving up), we use - which for moving the paddle down.
    paddle_a.sety(y)            

#For, second paddle.
def paddle_b_up(): #This for the upper movernents for the second paddle
    y = paddle_b.ycor()   
    y +=20 # Instead of +(which is for moving up), we use - which for moving the paddle down.
    paddle_b.sety(y)

def paddle_b_down(): #This for the down movernents for the second paddle
    y = paddle_b.ycor()   
    y -=20 # Instead of +(which is for moving up), we use - which for moving the paddle down.
    paddle_b.sety(y) 

"""""keyboard binding, 
since the above function(ie the function to move a paddle) is to specifically move a paddle,
you have to bind said movernents to the keyboard, so that when a particular button is pressed,the paddle moves.
It should also be noted, that our previous function, (paddle_a_up()) hasn't been called. So,
using the below commands, not only are we going to bind the keys to our keyboard, but in doing so, we will
also call the above function.
"""""
wn.listen() #Listening for the paddle_(s)

"""""while .listen() tells the program to listen to when the keybaord is pressed. And it
also passes to it self the actual function so as to call said funtion that has what the button onkeypress is
binding"""""
wn.onkeypress(paddle_a_up,"w",) 
wn.onkeypress(paddle_a_down, "s",)  
#For, second paddle.
wn.onkeypress(paddle_b_up,"Up",)
wn.onkeypress(paddle_b_down,"Down",)

"""""onkeypress() This enables the binding of a keypress with a function."""""

""""" Just repeated the same thing to get paddle_down."""""
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 

# Main game loop
while True:
    wn.update()

    #Moving the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    """"" What ball.setx(ball.xcor + ball.dx) and ball.sety(ball.ycor + ball.yx) essentally does is to implement the speed
to which the ball would move. This is done by combining xcor and ycor which is currently at 0, 0 + the speed or d of the ball,
which is set at 2px.
""""" 

#Boarder checking
    """"" This is to stop the ball from bouncing of the screen. To do this, we need to make sure that the ball
does not bounce of the boarders of the screen. So that would mean to prevent the ball fro bouncing
off the up, down and sides.
"""""
#Right boarder.
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    """"" So, "ball.dy *= -1" what this does is that it reverses the direction of the ball. So since dy 
    is 2px. reveresing it would be -1 px
    """"" 
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
# Adding sound, so that when ball touches border, it makes a sound.
        winsound.PlaySound("SPRTField_Balloon against wall 1 (ID 1825)_BSB.wav", winsound.SND_ASYNC)
        
    """""The two above code provides, that when the ball gets to the up and down border,it should bounce
    back. So if ycor() > 290 let it bounce the off the up boarder. then if ycor() is less than -290
    it should bounce off the down boarder.
    """""
    """""The next thing we want to do is the left and right boarders. So we want to make it in such a way, 
    that if the bounces off the edge of the letf and right screen, then it appears back in the middle.
    """""
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
    # Adding sound, so that when ball touches border, it makes a sound.
        winsound.PlaySound("SPRTField_Balloon against wall 1 (ID 1825)_BSB.wav", winsound.SND_ASYNC)
        
        """""So, what we want to do is that when the ball goes off the sides of the screen, one player wins and the other
    looses. In this case, the right player would win"""""
        score_pla += 1
        pen.clear() #What pen.clear does is to stop the scores fro writing ontop of each other.
        """""you need to also update the scores of the player usig pen.write"""""
        pen.write("player A: {} Player B: {}".format(score_pla, score_plb), align="center", font=("courier",24,"normal"))
    

    # For the left boarder.
    """"" use < negative"""""
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
    # Adding sound, so that when ball touches border, it makes a sound.
        winsound.PlaySound("SPRTField_Balloon against wall 1 (ID 1825)_BSB.wav", winsound.SND_ASYNC)

        """""So, what we want to do is that when the ball goes off the sides of the screen, one player wins and the other
    looses. In this case, the left player would win"""""
        score_plb += 1
        pen.clear() #What pen.clear does is to stop the scores fro writing ontop of each other.
        """""you need to also update the scores of the other player sig pen.write"""""
        pen.write("player A: {} Player B: {}".format(score_pla, score_plb), align="center", font=("courier",24,"normal"))
       
#How to make the paddle collide with the ball.
#getting the right paddle working.
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1
    # Adding sound, so that when ball touches border, it makes a sound.
        winsound.PlaySound("SPRTField_Balloon against wall 1 (ID 1825)_BSB.wav", winsound.SND_ASYNC)
        
    """""The code above, is the maths behind what makes the paddle to touch the ball, which then makes the ball to move."""""

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1
    """"" This is same code but to make the left paddle move."""""


