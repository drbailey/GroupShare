### author and docs ###
__author__ = 'drew bailey'
"""
exercise 17 from learning python the hard way:
http://learnpythonthehardway.org/book/ex17.html

drill two: commented
docs and author excluded in non-commented file to make the script short...
"""

### imports ###
# single line imports are generally frowned on, they are harder to read. 
# that being said i sometimes include related packages on one line.
# from package import a, b, c is totally fine however.
import os, sys
# you can reduce this further with an exec("""line_one\nline_two""") or
# with the use of ';' expressions, however you should NEVER EVER DO THIS IN
# REAL CODE. exec is highly dangerous, expecially if it includes user arguments,
# and ';' notation is extremly hard to read and can cause execution problems.

# additionally what i do here is mostly poor programming. it would be easier to
# read and conform to pep8 standards if i used a new line after the ':'.

# it is also easier to read if you declare variables then use them, for example
# f_in, f_out = sys.argv[1], sys.argv[2]
# then using those names would make this program easier to read.

# nesting functions is fine unless it is excessively long, and i do it all the
# time, but keep in mind the standard is 120 characters per line and it is
# often considered poor practice to exceed this limit. (due to standard window
# size i think?
if not os.path.exists(sys.argv[2]): open(sys.argv[2], 'w').write(open(sys.argv[1], 'r').read())

# poor exercise since it teaches new programmers bad habits!
# (literally if you didn't know them before, you do now).
