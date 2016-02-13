from re import sub
import sys

colors = {
    "default": "\033[39m",
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m"
}

patterns = [("[-\+]?\d+(\.(\d+)?)?", "red"), ("null", "green"), ("\"[^\"]*\"", "yellow")]

colorize = lambda match, color: colors[color] + sub("\033\[..m", "", match.group()) + colors["default"]

for line in sys.stdin:
    for pattern in patterns:
        line = sub(pattern[0], lambda match: colorize(match, pattern[1]), line)
    sys.stdout.write(line)
