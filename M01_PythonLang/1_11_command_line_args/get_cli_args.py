import sys

# cli_args = sys.argv
# sys.stdout.write(f"CLI Arguments: {cli_args}")

import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-n", "--numlines", default=10, required=False) # option, name=numlines
parser.add_argument("filename") # positional argument, name=filename

arguments = parser.parse_args()
print(arguments.numlines) # arguments.<name>
print(arguments.filename)

numlines = int(arguments.numlines)
filename = str(arguments.filename)

# peek(filename, numlines) # peek from previous lesson
