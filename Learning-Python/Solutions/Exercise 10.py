__author__ = 'drew bailey'


tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

# Here's a tiny piece of fun code to try out:
##while True:
##    for i in ["/", "-", "|", "\\", "|"]:
##        print "%s\r" % i
# hm... commented so drill code will run.

## drills ##
# 1 #
# no, i don't have flash cards...
# 2 #
# if my string contains """ at any point ''' becomes desireable.
# note that it is common practice to use """ for doc strings in functions/classes.
# see pep standards.
# 3 #
formatter = """\t"%r"\n\v'%r'"""
print formatter % ('a', True)
# 4 #
print '%r and %s' % ('\'', '\''), '%r and %s' % ('\"', '\"')
# the %r notation includes quotes around the injected string, %s does not.
# i do notice that.
