#!/usr/bin/env python

from pyrun import PyRun
from modules import modules
import sys
import argparse

parser = argparse.ArgumentParser(description='Stream-based python shell tool')
parser.add_argument('-e', dest='command',
                    help='Command to run')
parser.add_argument('-n', dest='linewise', action='store_true',
                    help='Enables command to run for each line in stdin')
parser.add_argument('-a', dest='var', default='_l',
                    help='Name of variable to substitute in stdin')
parser.add_argument('-i', '--index', dest='index', default='_i',
                    help='Current line the command is running on, if using -n')
parser.add_argument('-m', '--modules', dest='modules', default=modules,
                    help='List of modules to import')

if __name__ == '__main__':
    args = parser.parse_args()
    py_cmd = PyRun(
        stream=sys.stdin,
        command=args.command.strip(),
        linewise=args.linewise,
        var=args.var,
        index=args.index,
        modules=args.modules
    )
    py_cmd.run()
    args = parser.parse_args()
