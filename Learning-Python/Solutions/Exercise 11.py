__author__ = 'drew bailey'

print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall, and %r heavy." % (
    age, height, weight)

## drills ##
# 1 #
# ok
# 2 #
variable = raw_input("give me a variable: ")
# you can use input() or raw_input() to keep a windows shell from closing after
#  executing a python script. just include the line 'input()' at the end and
#  the program will exit only after a user presses enter.
# 3 #
# see 'Exercise 11 Drill 3.py'
# 4 #
# '6\'2"' has an escaped "'" character because both common string notations
#  are used in the string contents. the script must escape the type not used
#  to start and end the string to avoid a parsing error.
