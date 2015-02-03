__author__ = 'drew bailey'

# joke setup
x = "there are %d types of people." % 10
# variable set to string
binary = "binary"
# variable set to string
do_not = "don't"
# joke punchline
y = "Those who know %s and those who %s." % (binary, do_not)

# print setup
print x
# print punchline
print y

# print x's repr method
print "I said: %r." % x
# print y's repr method
print "I also said: '%s'." % y

# variable set to bool
hilarious = False
# inject object's repr into string
joke_evaluation = "Isn't that joke so funny?! %r"

# inject boolean variable's repr into string
print joke_evaluation % hilarious

# string for concatenation example
w = "This is the left side of..."
# string for concatenation example
e = "a string with a right side."

# add (concatenate) string
print w + e

## drills ##
# 1 #
# see above.
# 2 #
# ln 10 (twice), ln 18, ln 20, ln 28. look for the % notation.
# 3 #
# there are 5 places, but only 4 lines.
# 4 #
# the notation "w + e" makes a new string with elements from w and e.
# if both len(w) > 0 and len(e) > 0 then len(w + e) > len(w) and len(w + e) > len(e).
# (function 'len' means 'the length of', and returns an integer).
print all([len(e) > 0, len(w) > 0]) # prints True
