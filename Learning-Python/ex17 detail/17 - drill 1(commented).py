### imports ###
from sys import argv
from os.path import exists

### command line arguments ###
script, from_file, to_file = argv  # again, script is a placeholder and is not used

### everything else ###
if not exists(to_file):  # if output file not exists do other stuff
    # open both files through with. the reason for this is that with
    # statements both open under an alias (f_in and f_out here) AND
    # auto-close at the end of the with. this is the standard way to do
    # file read/writes. as far as security is concerned user facing
    # programs should use with so that there is no oppertunity to inject
    # a statement that replaces or alters the open files.
    with open(from_file, 'r') as f_in, open(to_file, 'w') as f_out:  
        f_out.write(f_in.read())  # write to output
