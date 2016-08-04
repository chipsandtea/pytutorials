# Command Line basics tutorial
# v1.0 - Last Modified: 8/3/2016
# By: Christopher Hsiao
import os.path,time

print('===== Command Line / Terminal Basics Tutorial =====')
print('By: Christopher Hsiao')
print('Last Modified: %s' % time.ctime(os.path.getctime('commandline.py')))

lessonTextData = None
try:
	with open('cmdTutText.json') as data:


lessonNum = 0 # Represents the lesson the user is currently on.

def lessonOne():
	


# ===== LESSON MODULE =====
while True:
	print('\nWould you like to...')
	print('1 - Start from the beginning.')
	print('2 - Choose a section.')
	print('q - Quit the tutorial.')
	choice = input('Enter: ')

	if choice == '1':
		lessonOne()
	elif choice == '2':
		print('Choose a section.')
	elif choice == 'q':
		print('Exiting...')
		quit()
	else:
		print('Invalid choice - Please try again!')