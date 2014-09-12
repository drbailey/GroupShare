from sys import argv
from os.path import exists

script, from_file, to_file = argv

if not exists(to_file):
    with open(from_file, 'r') as f_in, open(to_file, 'w') as f_out:
        f_out.write(f_in.read())
