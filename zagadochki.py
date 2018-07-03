

print('Hello! \nWelcome to the Reddler! \nRiddle #1')
answer = '123'
score = 0
#Riddle numer 1
answer = input('What language are we going to learn? ')
if answer == 'Python':
	print('Correct!')
	score += 1

elif answer == 'python':
	print('correct!')
	score += 1

print('You have got ',score,' correct answers ')


#Riddle number two
if score > 0:
	print('Keep going buddy!')
print('Prepare for the next riddle!')
answer = input('What operator you cant use with 2 strings')
if answer == '-':
	print('Good job!')
	score += 1
print('So far you smashed ', score, 'mysteries \n8 more to come')


