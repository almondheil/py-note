# py-note

A simple python note utility that can create and search notes in a
human-readable format. 

# Installation

## Requirements

- Python 3.6 or greater

- `fzf` system utility ((https://github.com/junegunn/fzf)[https://github.com/junegunn/fzf])

- `pyfzf` Python package ((https://github.com/nk412/pyfzf)[https://github.com/nk412/pyfzf])

    Note: Must be visible to python when you run the script, so best to install
    for user or globally rather than in an environment.

## Install steps

First, make sure you have the requirements listed above.

Then, clone this repository somewhere on your system. The repo can be deleted after
installation if desired, so don't worry about location too much.

```
git clone https://github.com/almondheil/py-note.git
```

With the repo cloned, copy the `note` script somewhere on `$PATH`, such as `~/.local/bin`. 

Next, create a config file for the utility. This can be in any of the following
locations (in order of priority)

- `%APPDATA\note\config` (on Windows)

    Note: I do not own any Windows machines to test this on. If something
    breaks, filing an issue or creating a pull request is the best way to make
    sure it gets fixed.

- `$XDG_CONFIG_HOME/note/config`

- `$HOME/.config/note/config`

The config file **must** contain a line telling the program the location of your
notes directory (`note_dir`), and may also contain other directives. An example
config file appears below.

```
# Directory where notes are stored
note_dir = $HOME/Notes
# File extension for created notes (default: .txt)
extension = .md
# Editor for notes (default: vi)
editor = nvim
```

Once all this setup is in place, you can verify the installation is complete
with `note -h`. 

# Usage

The behavior of the `note` utility is controlled by three subcommands.

## List notes

List all notes

```
note list
```

List notes with tags `t1`, `t2`, ..., `tn`

```
note list -t t1 t2 ... tn
```

List notes with extra information (long printout)

```
note list --long
```

## Edit a note

Fzf the filenames of all notes and edit one

```
note edit
```

Filter fzf choices by only notes with tags `t1`, `t2`, ..., `tn`

```
note edit -t t1 t2 ... tn
```

## New note

Create a new note marked with today's date (`YYYYMMDD.ext`)

```
note new
```

Create a new note with a particular filename (`YYYYMMDD-name.ext`)

```
note new name
```

Create a new note with tags `t1`, `t2`, ..., `tn`

```
note new -t t1 t2 ... tn
```

# Note format

A note file will be named with the current date, as well as an optional title.
For example, these are all valid names for note files.

When a note is created with this tool, it will be based on the following
template.

```
Title: Title string, used for long listing display
Date:  YYYY-MM-DD
Tags:  whitespace separated tags

=====

Note content, which the command line doesn't care about at all.
```

If you are adding your own header, you may include or omit any of the tags that
you want. This script reads the first three lines of the file looking for
a title, date, and tags, and does not attempt to read any further.

# Todo

- [ ] Remove `pyfzf` dependency so script can just be plug and play
