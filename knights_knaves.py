import sys
from parser import Parser

def main():
   
   looping = 1
   while(looping):
      user_input = raw_input("Enter the number of the knights and knaves puzzle you would like to run (1-50 are available) or 0 for exit: ")
      if user_input == '0':
         looping = 0
      else:
         file_name = "examples/puzzle" + user_input + ".txt"
         puzzle_file = file(file_name, 'r')
         text = puzzle_file.read()
         #pass text to parser

if __name__ == "__main__":
   main()
