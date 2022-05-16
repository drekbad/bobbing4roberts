#!/usr/bin/python3
#  Input full name file
#    - matches inputfile first names against default namePairs.txt
#      and adds asctd match to new list, outputs all unique names
#    e.g.  inputfile:  Dave Thomas  ::  +ouputfile:  David Thomas
#    - removes duplicates, sorts; provides details about I/O lists

#  TO DO:
#    >  solve multiple dictionary input file names with different out:
#       i.e.  Pat,Patricia and Pat,Patrick
#       need to add both to dictionary, but likely must use nested dict
#    >  solve outputfile exists, create new or overwrite?
#    >  count # provided names, # after matches, # after username format
#    >  test + allow read/write from alternate dir of script

import os, sys, getopt

def main(argv):
  global inputfile
  global outputfile
  try:
    opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
  except getopt.GetoptError:
    print(os.path.basename(__file__)+" -i <inputfile> -o <outputfile>")
    sys.exit(2)
  for opt, arg in opts:
    if opt == '-h':
      print(os.path.basename(__file__)+" -i <inputfile> -o <outputfile>")
      sys.exit()
    elif opt in ("-i", "--ifile"):
      inputfile = arg
    elif opt in ("-o", "--ofile"):
      outputfile = arg

if len(sys.argv) < 4:
  print(os.path.basename(__file__)+" -i <inputfile> -o <outputfile>")
  sys.exit()

if __name__ == "__main__":
 main(sys.argv[1:])

script = os.path.dirname(os.path.abspath(__file__))
namePair = script + "/namePairs.txt"
namePairs = {}
newNames = []
unameList = []
unameCount = 0

def unameFormat():
  global unameCount
  fLast = first[0]+last
  firstL = first+last[0]
  unameList.append(first)
  unameList.append(fLast)
  unameList.append(firstL)
  unameList.append(first+"."+last)
  unameCount += 4

#  Open namePairs.txt file and create dict
with open(f'{namePair}', 'r') as pairs:
  for x in pairs:
    k, v = x.strip().split(',')
    namePairs[k.strip()] = v.strip()

#  Open inputfile
with open(f'{inputfile}', 'r') as myfile:
  inpCount = len(open(inputfile).readlines(  ))
  addedName = 0
  for line in myfile:
    if not line:
      continue
    names = line.split()
    first = names[0]
    if len(names) == 2:
      last = names[1]
    elif len(names) == 3:
      middle = names[1]
      last = names[2]
#^^^ create condition for names longer than 3 words ^^^#
#   Prevent adding if already in newNames
    newFullname = first+" "+last
    unameFormat()
    if newFullname not in newNames:
      newNames.append(newFullname)
    if first in namePairs.keys():
      keysNewFullname = namePairs.get(first)+" "+last
#      newNames.append(namePairs.get(first)+" "+last)
      if keysNewFullname not in newNames:
        newNames.append(keysNewFullname)
        addedName += 1 # counting for stats of newly-added names
#   Reverse lookup: for-each loop to prevent StopIteration via generator exprs
    exp = (key for key, value in namePairs.items() if value == first)
    for key in exp:
      valuesNewFullname = key+" "+last
      if valuesNewFullname not in newNames:
        newNames.append(valuesNewFullname)
        addedName += 1

# Save output to specified filename
#  to-do: if out file already exists, write new one
#  :sort list and report stats
print(f"\nThere were {inpCount} names in the input file,")
print(f" and {addedName} names were added to the list.")
print(f"Generating {unameCount} usernames...")
print(f"\nsaving to file:  ./{outputfile}")
outFile = open(outputfile, 'w')
for element in unameList:
#for element in newNames:
  outFile.write(element + "\n")
outFile.close()
