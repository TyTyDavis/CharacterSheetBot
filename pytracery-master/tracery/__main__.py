#!/usr/bin/env python
# encoding: utf-8
"""
Output an example line from a JSON Tracery grammar.
"""
from __future__ import print_function, unicode_literals
import argparse
import json

import tracery
from tracery.modifiers import base_english

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Output an example line from a JSON Tracery grammar.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument(
        "json", help="Input JSON file")
    parser.add_argument(
        "number", type=int, default=1, nargs="?",
        help="Number of lines to generate")
    args = parser.parse_args()

    with open(args.json) as data_file:
        rules = json.load(data_file)

    grammar = tracery.Grammar(rules)
    grammar.add_modifiers(base_english)

    for i in range(args.number):
        print(grammar.flatten("#origin#"))

# End of file
