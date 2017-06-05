#!/usr/bin/env python

from pyrun import PyRun
from modules import modules
import sys
import argparse

parser = argparse.ArgumentParser(description='Stream-based python shell tool')
parser.add_argument('-e',
                    dest='command',
                    help='Command to run')
parser.add_argument('-v', '--var',
                    dest='var', default=PyRun.SUBSITUTION_VAR,
                    help='Name of variable to substitute in stdin')
parser.add_argument('-i', '--index',
                    dest='index', default=PyRun.SUBSITUTION_INDEX,
                    help='Name of variable to substitute in current line #')
parser.add_argument('-m', '--modules',
                    dest='modules', default=modules,
                    help='List of modules to import')

if __name__ == '__main__':
    args = parser.parse_args()
    py_cmd = PyRun(
        stream=sys.stdin,
        command=args.command,
        var=args.var,
        index=args.index,
        modules=args.modules
    )
    py_cmd.run()
