from sys import argv

script, filename = argv

# Lines 1-3 use argv to get the filename
# Line 8 opens the file.  After which print is combined with
# an new command function 

txt = open(filename)

print "Here is your file %r:" % filename
print txt.read()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
