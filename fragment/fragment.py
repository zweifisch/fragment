"""fragment

Usage:
  fragment [--output=<folder>] [--extension=<md>] [--filter=<headlines>] <source>

Options:
  -h --help     Show this screen.
  --version     Show version.

Example:
  fragment --output /var/www/ --filter public,codesnip ~/wiki/diary
"""

import markdown2
from docopt import docopt


def main():
	args = docopt(__doc__, version='fragment 0.0.1')
	print(args)
