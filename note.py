#!/usr/bin/env python

import argparse
import sys

def main(args):
    parser = argparse.ArgumentParser(description='Note management utility')

    subparsers = parser.add_subparsers(required=True, help='mode help')
    parser_list = subparsers.add_parser('list', aliases=['ls'], help='list help')
    parser_edit = subparsers.add_parser('edit', aliases=['e'], help='edit help')
    parser_new  = subparsers.add_parser('new', aliases='n', help='new help')

    parser_list.add_argument('-t', '--tags', nargs='+',
                             help='filter notes with tags', metavar='TAG')
    parser_list.add_argument('--long', action='store_true',
                             help='print long listings')

    parser_edit.add_argument('-t', '--tags', nargs='+',
                             help='filter notes with tags', metavar='TAG')

    parser_new.add_argument('-n', '--name', required=False,
                            help='optional note name')
    parser_new.add_argument('-t', '--tags', nargs='+',
                            help='initial note tags', metavar='TAG')

    parser.parse_args(args)

"""

What sorta cli behavior do we need?

note list // note ls

    does a stdout printout of all notes

    with -t / --tags, will filter by tags

    maybe some control over whether we do oneline or multiline output per note

        long vs short listing

        note title
            tags tags tags
            last edited date

        note title

note edit // note e

    interactively search for a note (fzf?), then open it in $EDITOR

    if you use -t / --tags, it will only show notes matching those tags to start off

note new // note n

    create a note

    at minimum will create ~/Notes/YYYYMMDD.md (or whatever they set the note dir to)

    -n will give it a name, YYYYMMDD-note-title.md

    -t will give it tags

    -d will choose the note directory (?)

"""

if __name__ == '__main__':
    main(sys.argv[1:])
