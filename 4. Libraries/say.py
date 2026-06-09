# pip install cowsay  - in terminal
# cowsay is a package that can be installed using pip hence no need to download a zip file from 
# https://pypi.org/

import cowsay
import sys

if len(sys.argv) == 2:
    # cowsay.cow("hello, " + sys.argv[1])
    cowsay.trex("hello, " + sys.argv[1])