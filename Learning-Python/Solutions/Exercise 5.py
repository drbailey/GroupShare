__author__ = 'drew bailey'

my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eye and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky, try and get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    my_age, my_height, my_weight, my_age + my_height + my_weight)

## drills ##
# 1 #
# see 'Exercise 5 Drill 1.py'
# 2 #
my_height_cm = my_height * 2.54
my_weight_kg = my_weight * 0.453592
print "His height in cm is %d.", my_height_cm
print "His weight in km is %d.", my_weight_kg
# 3 #
# % ->
##'d'	Signed integer decimal.	 
##'i'	Signed integer decimal.	 
##'o'	Signed octal value.	(1)
##'u'	Obsolete type – it is identical to 'd'.	(7)
##'x'	Signed hexadecimal (lowercase).	(2)
##'X'	Signed hexadecimal (uppercase).	(2)
##'e'	Floating point exponential format (lowercase).	(3)
##'E'	Floating point exponential format (uppercase).	(3)
##'f'	Floating point decimal format.	(3)
##'F'	Floating point decimal format.	(3)
##'g'	Floating point format. Uses lowercase exponential format if exponent is less than -4 or not less than precision, decimal format otherwise.	(4)
##'G'	Floating point format. Uses uppercase exponential format if exponent is less than -4 or not less than precision, decimal format otherwise.	(4)
##'c'	Single character (accepts integer or single character string).	 
##'r'	String (converts any Python object using repr()).	(5)
##'s'	String (converts any Python object using str()).	(6)
##'%'	No argument is converted, results in a '%' character in the result.
# 4 #
print "Testing format 'r' with integer '1' results in '%r'." % 1
class New(object):
    """ example class for __repr__ method """
    def __init__(self):
        pass
    def __repr__(self):
        return "I've replaced this class' __repr__ method!"
n = New()
print "Testing an instance of custom class New's __repr__ method results in '%r'." % n
print "An integer class' __repr__ method must be the same as applying str()."

