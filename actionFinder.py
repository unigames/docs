#--------------------------------------------#
# Name:   actionFinder.py                    #
# Author: Donald Sutherland                  #
# Usage:  actionFinder.py [filename]         #
# Input:  a file                             #
# Output: all action items in that file      #
#         printed and appended to that file  #
# Action Items are formatted as:             #
# 	>[Name](+Name2+Name3):[Action]           #
#--------------------------------------------#

# Import modules
import sys
import re

# Regex pattern to search for
pattern = re.compile("\t*>(.+?):\s(.+)")

# Make each committee member a dictionary that will contain their action items, for sorting
# All others are "other"
committeeNames = ['Gavin','Aoibhinn','Alaura','Donald','Nadia','Jasmine','Alistair','Lewis','Jake','Taylor','Other']
committeeActions = {'Other':[]}
for member in committeeNames:
    committeeActions[member] = []

# Grab the command line arguments
args = sys.argv

# Check that there's only one argument
if len(args) != 2:
    print("Usage: actionFinder.py [filename]")
else:
	# Open the minutes
    minutes = open(args[1], "r+a")
	
	# Search the minutes for the action items
    matches = pattern.findall(minutes.read())
	
	# For each one...
    for match in matches:
		# Strip any excess characters from it
        action = match[1].strip()
		
		# If it belongs to a committee member, put it in their block
        if committeeActions.has_key(match[0]):
            committeeActions[match[0]].append(action)
        
		# Otherwise check if it belongs to multiple committee members, and give it to all of them if it does
		# If not, give it to "Other"
		else:
            involved = []
            for name in committeeActions.keys():
                if name in match[0]:
                    involved.append(name)
            if len(involved) == 1:
                committeeActions[involved[0]].append(action)
            if len(involved) == 0:
                committeeActions['Other'].append("("+match[0].strip()+") "+action)
            else:
                for name in involved:
                    committeeActions[name].append(action+' (along with '+(', '.join([n for n in involved if n!=name]))+')')
    
    # Prepare results to be printed
	outputString = "--\nAction Items:\n"
    for name in committeeNames:
    	if len(committeeActions[name]) == 0:
    		continue
        outputString += name+":\n"
        for item in committeeActions[name]:
            outputString += "> "+item[:1].upper()+item[1:]+"\n"
        outputString += "\n"
		
	# Print them
    print(outputString)
	
	# Append them to the minutes
    minutes.write(outputString)
        