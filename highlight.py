from json import load
from re import sub
import sys

with open("jsonPatterns.json") as f:
    patterns = load(f)

colors = {
    "default": "\033[39m",
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m"
}
colorize = lambda match, color: colors[color] + sub("\033\[..m", "", match.group()) + colors["default"]

for line in sys.stdin:
    for pattern in patterns:
        line = sub(pattern["pattern"], lambda match: colorize(match, pattern["color"]), line)
    sys.stdout.write(line)
