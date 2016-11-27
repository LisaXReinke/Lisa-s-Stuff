
sample = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''

# Here are the different list levels for the game.
easy_level_string = "Here is a test of basic vocabulary. In programming, something with a value is called an __1__.  A __2__ is a sequence of characters surrounded by quotation marks. A list is a sequence of anything. A built in function that is already included in Python is called a __3__. An example of this is <__2__ >.find(<__2__ >). To __4__ the function, means to use the function."
medium_level_string = "There are six steps in tackling a computational problem. The first is to not panic. The second is to figure out what the __1__ are. The third is to figure out what the __2__ are. The fourth is to work through some examples by hand. The fifth is to figure out a simple __3__ solution. The last step is to develop incrementally and __4__ as you go."
hard_level_string = "Knowing what kind of output to expect is useful. Equality __1__ like <, >, ==, result in true or false outputs. If you use the index method, which is <list>.index(<value>), the output is a number or an __2__. Even when there is an __3__ set, the output of the len operator is a number.  If you program <value> not in <list>, the output is either true or false. And <list>.append(<element>) __4__ the old list by adding a single element to the end."

# Here are the different answers for each level.
easy_answers_list = ["expression", "string", "method", "call"]
medium_answers_list = ["inputs", "outputs", "mechanical", "test"]
hard_answers_list = ["comparisons", "error", "empty", "mutates"]

# This is the list for the blanks. 
blank_spaces = ["__1__", "__2__", "__3__", "__4__"]

#This function allows users to set difficulty level: Easy, Medium, or Hard.
def introduction():
	print "Hi. Welcome to the fill-in-the-blanks game. What level would you like to play?"
	lvlanswer = "nope"
	while lvlanswer != "Easy" and lvlanswer != "Medium" and lvlanswer != "Hard":
		lvlanswer = raw_input("Type 'Easy', 'Medium', or 'Hard' here:  ")
	print ""
	print "You have selected " + lvlanswer	
	print ""
	return lvlanswer

# This function takes the difficulty lvl and prompts the game to run.
def game(difficulty):
	if difficulty == "Easy":
		answers = easy_answers_list
		question = easy_level_string
	if difficulty == "Medium":
		answers = medium_answers_list
		question = medium_level_string
	if difficulty == "Hard":
		answers = hard_answers_list
		question = hard_level_string
	counter1 = 0
	while counter1 <= 3:
		print answers[counter1]#remove this before end
		answer1 = "nope"
		count = 5
		while answer1 != answers[counter1]:
			current_paragraph = "The fill-in-the-blank paragraph currently reads as such:"
			print current_paragraph
			print ""
			print question
			print ""
			answer1 = raw_input("What word should replace" + blank_spaces[counter1] + "? Type your guess here:  "  )
			if answer1 != answers[counter1]:
				count = count - 1
				if count == 0:
					print "Game Over!"
					counter1 = 4
					break
				else:
					print "Nope. That's not correct. Try again. You have " + str(count) + " tries left."
			else: 
				print ""
				print "Correct! " * 44
				print ""

				#put function here 
				#question = function
		counter1 += 1
		
	if counter1 !=5:
		print "You're a winner."



game(introduction())

#def choices
