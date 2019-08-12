# Aug 12, 2019 (Ch 1 - basic)
# this program says hello and asks for my name 
# ^using the hash tag symbol is how you write comments 

print('Hello world')
# print() function displays the  string val inside the parameter 

print ('What is your name?') # ask for their name 
myName = input() 
# input() function waits for the user to type some text on keyboard 
# 	and press enter 

print('It is good to meet you, ' + myName )
print('The length of your name is: ')
print(len(myName))
# len() function passes a string value and returns the number of character 
#	in that string 

print('What is your age?') # ask for their age 
myAge = input() 
print('You will be ' + str(int(myAge)+ 1) + ' in a year')
# the str(), int, and float() functions 