import sys
import re
from parser import Parser
from evaluator import evaluate_puzzle

def main():
   if len(sys.argv) != 2:
       print "Usage: Lab4.py <Filename>"
       sys.exit(1)

   puzzle_file = open(sys.argv[1], "r")

   contents = puzzle_file.read()
   print "PUZZLE:"
   print contents

   # :) 
   modified_contents = re.sub("\n\n", "\n", contents)
   
   p = Parser()
   statements, name_map = p.convert(modified_contents)
   results = evaluate_puzzle(statements)

   if results[0] == True:
      result =  "A is a knight and B is a knave"
   elif results[1] == True:
      result = "A is a knave and B is a knight"
   elif results[2] == True:
      result = "A is a knight and B is a knight"
   elif results[3] == True:
      result = "A is a knave and B is a knave"
   else:
      result = "Indeterminate"

   aval = ""
   bval = ""

   for key, val in name_map.iteritems():
      if val == "A":
         aval = key
      if val == "B":
         bval = key

   result = re.sub("A", aval, result)
   result = re.sub("B", bval, result)

   print "\nRESULT:"
   print result

   puzzle_file.close()


if __name__ == "__main__":
   main()
