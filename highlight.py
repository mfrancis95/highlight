from json import load
from argparse import ArgumentParser
from re import sub
import sys

with open("jsonPatterns.json") as f:
    patterns = load(f)

parser = ArgumentParser("highlight")
parser.add_argument("-c", "--colors")
parser.add_argument("-f", "--file")
args = parser.parse_args()

colors = args.colors
if colors:
    with open(colors) as f:
        colors = list(map(lambda color: "\033[" + str(color) + "m", load(f)))
else:
    colors = ["\033[31m", "\033[32m", "\033[33m"]

colorize = lambda match, color: colors[color] + sub("\033\[..m", "", match.group()) + "\033[39m"

def highlight(file):
    for line in file:
        for pattern in patterns:
            line = sub(pattern["pattern"], lambda match: colorize(match, pattern["color"]), line)
        sys.stdout.write(line)

file = args.file
if file:
    with open(file) as f:
        highlight(f)
else:
    highlight(sys.stdin)
