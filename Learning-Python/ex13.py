from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable:", first
print "Your second variable is:", second
print "Your third variable is:", third

# Added for additional exercise.

location = raw_input("Where are you located? ")

print "You are located in %r." % (location)
