from highlighter import Highlighter
from json import load
from argparse import ArgumentParser
import sys

highlighter = Highlighter()

with open("jsonPatterns.json") as f:
    highlighter.patterns["json"] = load(f)

parser = ArgumentParser("highlight")
parser.add_argument("-c", "--colors")
parser.add_argument("-f", "--file")
args = parser.parse_args()

colors = args.colors
if colors:
    with open(colors) as f:
        highlighter.colors = list(map(lambda color: "\033[" + str(color) + "m", load(f)))

def highlight(file):
    for line in highlighter.highlight(file, "json"):
        sys.stdout.write(line)

file = args.file
if file:
    with open(file) as f:
        highlight(f)
else:
    highlight(sys.stdin)
