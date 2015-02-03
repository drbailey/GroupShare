__author__ = 'drew bailey'

# number of cars
cars = 100
# passenger space in each car
space_in_a_car = 4.
# number of drivers
drivers = 30
# number of passengers
passengers = 90
# cars with no available driver
cars_not_driven = cars - drivers
# cars with available drivers
cars_driven = drivers
# number of available seats in driven cars
carpool_capacity = cars_driven * space_in_a_car
# average number of people that need to be in each car for all people to get a ride
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "people today."
print "We need to put about", average_passengers_per_car, "in each car."

## explain this error in your own words. make sure you use line numbers and explain why. ##
# there is an unwanted '_' character in 'carpool' on line 8.
# python reads this as a new variable, not the same as carpool_capacity.
# if a variable is used before it is defined python calls an error.

## drills ##
# 1 #
# it is not necessary, if you used an integer for this variable you would still recieve 120 for 'carpool_capacity'.
# 2 #
# ok
# 3 #
# see above
# 4 #
# ok
# 5 #
# ok
# 6 #
# see 'Exercise 4 Drill 6.png'
