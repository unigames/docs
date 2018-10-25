import sys
import re

pattern = re.compile("\t*>(.+?):\s(.+)")

committeeNames = ['Gavin','Aoibhinn','Alaura','Donald','Nadia','Jasmine','Alistair','Lewis','Jake','Taylor','Other']
committeeActions = {'Other':[]}
for member in committeeNames:
    committeeActions[member] = []


args = sys.argv
if len(args) != 2:
    print("Usage: actionFinder.py [filename]")
else:
    minutes = open(args[1], "r+a")
    matches = pattern.findall(minutes.read())
    for match in matches:
        action = match[1].strip()
        if committeeActions.has_key(match[0]):
            committeeActions[match[0]].append(action)
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
    #print committeeActions
    # Print results
	outputString = "--\nAction Items:\n"
    for name in committeeNames:
    	if len(committeeActions[name]) == 0:
    		continue
        outputString += name+":\n"
        for item in committeeActions[name]:
            outputString += "> "+item[:1].upper()+item[1:]+"\n"
        outputString += "\n"
    print(outputString)
    minutes.write(outputString)
        