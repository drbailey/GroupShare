### imports ###
from sys import argv
from os.path import exists

### command line arguments ###
script, from_file, to_file = argv  # script is a place holder for argv[0], not used

print "Copying from %s to %s" % (from_file, to_file)

### open and write ###
# we could do these two on one line, how?  # nest line 2 in line 1, see drill 1
in_file = open(from_file)
indata = in_file.read()

print "The input file is %d bytes long" % len(indata)  # not needed, calls __len__ method

print "Does the output file exist? %r" % exists(to_file)  # informs user if output file exists
print "Ready, hit RETURN to continue, CTRL-C to abort."  # raise exception on CTRL-C or continue
raw_input()

out_file = open(to_file, 'w')  # opens output file
out_file.write(indata)  # writes data...

print "Alright, all done."

### cleanup ###
out_file.close()
in_file.close()
