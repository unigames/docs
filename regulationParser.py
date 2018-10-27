#-------------------------------------#
# Name:   regulationParser.py         #
# Author: Donald Sutherland (2018)    #
#-------------------------------------#

import markdown
from bs4 import BeautifulSoup
import sys

# Grab the command line arguments
args = sys.argv

# Check that there's only one argument
if len(args) != 3:
    print("Usage: regulationParser.py [inFile] [outFile]")
else:
    inFile = open(args[1], "rU")
    outFile = open(args[2], "w")

    html = markdown.markdown(inFile.read())
    
    print(html, file=outFile)