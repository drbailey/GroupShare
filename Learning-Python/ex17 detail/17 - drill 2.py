import os, sys
if not os.path.exists(sys.argv[2]): open(sys.argv[2], 'w').write(open(sys.argv[1], 'r').read())
