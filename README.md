# py-note

A simple python note manager that can create and search notes in a
human-readable format. 

# Note format

A note file will be named with the current date, as well as an optional title.
For example, these are all valid names for note files.

When a note is created with this tool, it will be based on the following
template.

```
Title:
Date: YYYY-MM-DD
Tags: whitespace separated tags

=====

Note content, which the command line doesn't care about at all.
```

An initial title and tags can be specified on the command line, with the
`-n`/`--name` and `-t`/`--tags` parameters, or they can be added by the user at
any point.

# Installation
