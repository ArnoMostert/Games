# import the modules
import tkinter
import random

# list of possible colour.
colours = ['Red','Blue','Green','Pink','Black',
		'Yellow','Orange','White','Purple','Brown']
score = 0

# the game time left, initially 60 seconds.
timeleft = 60

# function that will start the game.
def startGame(event):
	
	if timeleft == 60:
		
		# start the countdown timer.
		countdown()
		
	# run the function to
	# choose the next colour.
	nextColour()

# Function to choose and
# display the next colour.
def nextColour():

	# use the globally declared 'score'
	# and 'play' variables above.
	global score
	global timeleft

	# if a game is currently in play
	if timeleft > 0:

		# make the text entry box active.
		e.focus_set()

		# if the colour typed is equal
		# to the colour of the text
		if e.get().lower() == colours[1].lower():
			
			score += 1

		# clear the text entry box.
		e.delete(0, tkinter.END)
		
		random.shuffle(colours)
		
		# change the colour to type, by changing the
		# text _and_ the colour to a random colour value
		label.config(fg = str(colours[1]), text = str(colours[0]))
		
		# update the score.
		scoreLabel.config(text = "Score: " + str(score))


# Countdown timer function
def countdown():

	global timeleft

	# if a game is in play
	if timeleft > 0:

		# decrement the timer.
		timeleft -= 1
		
		# update the time left label
		timeLabel.config(text = "Time left: "+ str(timeleft))
								
		# run the function again after 1 second.
		timeLabel.after(1000, countdown)


# Driver Code
# create a tkinter window
root=tkinter.Tk()
# set the title
root.title("Colour game")

# set the size
root.geometry("675x300")
instructions = tkinter.Label(root, text = "WELCOME TOPLAY COLOUR GAME",font = ('Times ', 50,"italic"),fg="purple",bg="pink")
instructions.pack()


# add an instructions label
instructions = tkinter.Label(root, text = "Enter in the colour of the word displayed",font = ('Times', 32,"italic"))
instructions.pack()

# add a score label
scoreLabel = tkinter.Label(root, text = "Type anything and press enter to start",font = ('Times', 32,"italic"))
scoreLabel.pack()

# add a time left label
timeLabel = tkinter.Label(root, text = "Time left: " +
			str(timeleft), font = ('Times',30,"italic","bold"))
				
timeLabel.pack()

# add a label for displaying the colours
label = tkinter.Label(root, font = ('Times ', 90,"bold"))
label.pack()

# add a text entry box for
# typing in colours
e = tkinter.Entry(root, width=30)

# run the 'startGame' function
# when the enter key is pressed
root.bind('<Return>', startGame)
e.pack()

# set focus on the entry box
e.focus_set()

# start the GUI

root.mainloop()


