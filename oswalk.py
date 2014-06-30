
import os
import re
import shutil

# something in a filename to match, uses regex patterns (or simple text match)
pattern = '.txt'
# path to copy files to
path = r'C:/gathered_files'

# make destination if it doesn't exist
if not os.path.exists(path):
    os.makedirs(path)

for root, dirs, files in os.walk(os.getcwd()):
    print 'root: ', root
    print 'directories: ', dirs
    print 'files: ', files
    for f in files:
        # regex match object, if the match exists it will have a .group() contaning the full file name
        m = re.search(pattern, f)
        if m:
            # move file, if you want more properties moved (change date and stuff) use .copy2(m.group(), path)
            shutil.copy(root+'\\'+f, path)
