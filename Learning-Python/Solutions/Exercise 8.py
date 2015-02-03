__author__ = 'drew bailey'

formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)

## drills ##
# 1 #
# ok
# 2 #
# the third line has an internal ' character causing python to default to the 
# other string notation.
