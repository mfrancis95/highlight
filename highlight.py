from json import load
from argparse import ArgumentParser
from re import sub
import sys

with open("jsonPatterns.json") as f:
    patterns = load(f)

parser = ArgumentParser("highlight")
parser.add_argument("-f", "--file")
args = parser.parse_args()

colors = {
    "default": "\033[39m",
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m"
}
colorize = lambda match, color: colors[color] + sub("\033\[..m", "", match.group()) + colors["default"]

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
