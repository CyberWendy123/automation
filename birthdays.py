#Aug 12, 2019 (Ch 5: Dictionary)
birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol':'Mar 4'}

while True: 
	print('Enter a name: (bank to quit)')
	name = input()
	if name == '': 
		break 

	if name in birthdays: 
		print(birthdays[name] + ' is the birthday of ' + name)
	else: 
		print('I do not have birthday information for ' + name)
		print('What is their britday?')
		bday = input()
		birthdays[name] = bday
		print('Birthday database updated. ')

# of course, all the data entered is forgotten when program terminates 