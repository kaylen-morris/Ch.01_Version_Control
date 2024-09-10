'''
1.0 Jedi Training (17pts)  Name: Kaylen Morris


1. Define Forking (1pt): 
When someone makes a copy of a shared read-only repository. They can then make changes to said copy, and can pull any new changes into the original code.
2. Define Cloning (1pt): 
Once a repository is forked, it can be cloned to the local computer. This allows the user to work on the forked file without affecting the original code.
3. Define Branching (1pt):
Creating different copies of a certain code, still retaining the original code. This seperates in progress "unstable" code from "stable" tested code.
4. Define Committing (1pt): 
A checkpoint in the code, allowing a user to save their code before continuing to alter it.
5. Define Merging (1pt): 
The process of combining two or more code branches into a single code.
6. Define Pushing (1pt):
Sending code from a branch in the local repository to a branch in the remote repository.
7. Define Pull Request (1pt):
A request asking the original organization to pull in the changed code to be merged with the original code. The original organization can decide if they want to pull and merge the new code or not.

8. TURTORIAL ART (10pts.)

Modify the starter code below to create your own cool drawing. 
Make sure you keep the last two lines of code!!!! 
Your first and last name must be written on your art.
The last line keeps the window open until you click to close.
Turtle Documentation: https://docs.python.org/3.3/library/turtle.html?highlight=turtle
'''
import turtle

purple = turtle.Turtle()
pink = turtle.Turtle()
blue = turtle.Turtle()
magenta = turtle.Turtle()
eyes = turtle.Turtle()
background = turtle.Turtle()

purple.color('purple')
pink.color('pink')
blue.color('blue')
magenta.color('magenta')
eyes.color('black')
background.color("green")

background.shape('turtle')
purple.shape('turtle')
pink.shape('turtle')
blue.shape('turtle')
magenta.shape('turtle')
eyes.shape('turtle')

background.speed(5)
purple.speed(5)
pink.speed(5)
blue.speed(5)
magenta.speed(5)
eyes.speed(5)

eyes.penup()
eyes.goto(-300,-300)
purple.penup()
purple.goto(-300,-300)
pink.penup()
pink.goto(-300,-300)
blue.penup()
blue.goto(-300,-300)
magenta.penup()
magenta.goto(-300,-300)

background.penup()
background.goto(200,200)
background.pendown()
background.begin_fill()
background.goto(200,-200)
background.goto(-200,-200)
background.goto(-200,200)
background.goto(200,200)
background.end_fill()
background.penup()
background.goto(-300,-300)

pink.penup()
pink.goto(0,25)
def pinkcircle():
  pink.pendown()
  pink.begin_fill()
  pink.circle(40)
  pink.end_fill()
  pink.penup()
pinkcircle()
pink.goto(-300,-300)

magenta.penup()
magenta.goto(-20,-50)
def magentacircle():
  magenta.pendown()
  magenta.begin_fill()
  magenta.circle(40)
  magenta.end_fill()
  magenta.penup()
magentacircle()
magenta.goto(-300,-300)

purple.penup()
purple.goto(-50,-120)
def purplecircle():
  purple.pendown()
  purple.begin_fill()
  purple.circle(40)
  purple.end_fill()
  purple.penup()
purplecircle()
purple.goto(-300,-300)

blue.penup()
blue.goto(-80,-190)
def bluecircle():
  blue.pendown()
  blue.begin_fill()
  blue.circle(40)
  blue.end_fill()
  blue.penup()
bluecircle()
blue.goto(-300,-300)

eyes.penup()
eyes.goto(20,65)
def eye():
  eyes.pendown()
  eyes.begin_fill()
  eyes.circle(5)
  eyes.end_fill()
  eyes.penup()
eye()
eyes.goto(-15,75)
eye()
eyes.goto(75,15)


eyes.write('Kaylen Morris',font=("Arial", 16, "normal")) # signs your name to your art

eyes.goto(-300,300)

turtle.exitonclick() #Keeps pycharm window open so we can see the drawing
