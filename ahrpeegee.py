#A basic text-based game demonstrating some familiarity with the python language.
#Patrick Namasondhi, 2012

from sys import argv

script, user_name = argv
prompt = '> '


print "What is your name?"
player_name = raw_input(prompt)
print "What is a handheld item you cannot do without?"
weapon = raw_input(prompt)
print "Who do you trust the most in this world?"
caller = raw_input(prompt)
print "And lastly, where do you run to when all else is lost?"
home = raw_input(prompt)


#print "You wake up at your computer"
#print "The time is _____. The day is ________"
#print "Can you feel reality pulling you back in?"
#
#
#


#Actions that the player can take
commands = ['talk','run','strike','chant','stats','wristwatch']

player_health = 10
enemy_health = 10

while enemy_health > 0:
	print "The mountain lion snarls at you."
	print "You have a %s and a buckler" (weapon)
	print "What do you do?"
	print commands
#	for i in range(0,len.commands):
#		print(commands[i])
	choice = raw_input(prompt)

	if choice == 'talk':
		print "It does not work. The lion strikes you"
		player_health = 0
		
	if choice == 'chant':
		print "You vaporized that mountain bitch like it was nothing!"
		enemy_health = 0
	
	if choice == 'wristwatch':
		print "If you're so damn worried about the time, it's "
		
	elif:
		print "Ineffective. I do not understand you."

