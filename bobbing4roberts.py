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

namePair = "./namePairs.txt"
namePairs = {}
newNames = []

#  Open namePairs.txt file and create dict
with open(f'{namePair}', 'r') as pairs:
  for x in pairs:
    k, v = x.strip().split(',')
    namePairs[k.strip()] = v.strip()

#  Open inputfile
with open("./names.txt") as myfile:
  addedName = 0
  for line in myfile:
    if not line:
      continue
    names = line.split()
    first = names[0]
    if len(names) == 2:
      last = names[1]
      newNames.append(first+" "+last)
    elif len(names) == 3:
      middle = names[1]
      last = names[2]
      newNames.append(first+" "+last)
    if first in namePairs.keys():
      newNames.append(namePairs.get(first)+" "+last)
      addedName += 1

# Save output to specified filename
## if out file already exists, write new one
print(f"\nsaving to file:  ./{outputfile}")
outFile = open(outputfile, 'w')
for element in newNames:
  outFile.write(element + "\n")
outFile.close()