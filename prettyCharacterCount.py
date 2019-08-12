# Aug 12, 2019 (Ch 5: Dictionaries)
# understanding pprint() and pformat() functions 
import pprint 

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message: 
	count.setdefault(character, 0)
	count[character] = count[character] + 1 

pprint.pprint(count)
# the output looks much cleaner! not only sorted but also formatted 
pprint.pformat(count) #obtain preffied text as string value instead of displaying 