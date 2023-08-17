# py-note

A simple python note utility that can create and search notes in a
human-readable format. 

# Installation

First, just copy the `note` script to somewhere easy to access, like in
`~/.local/bin` or somewhere else in `$PATH`.

You will also need to install the `iterfzf` library. It does not seem to be
currently maintained, so this aspect is a point of improvement in the script.
For now, something like this should work:

```
pip install --user iterfzf
```

Next, create a config file for the utility. This can be in any of the following
locations (in order of priority)

- `$XDG_CONFIG_HOME/note/config`

- `$HOME/.config/note/config`

- `$HOME/note.conf`

The utility file **must** contain a line telling the program the location of your
notes directory (`note_dir`), and may also contain other directives. An example
config file appears below.

```
# Directory where notes are stored
note_dir = /home/<username>/Notes
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

# Todo

- [ ] Remove `iterfzf` dependency so script can just be plug and play

- [ ] Fix `-t` filter behavior to be "all" instead of "any"

- [ ] Allow the config file to parse `$HOME` and other env vars

  - [ ] Possibly using `ConfParse`

- [ ] Use `$EDITOR` variable if config editor is not set

    `conf.editor` > `$EDITOR` > `vi` (fallback)

- [x] Avoid crashing when `note edit` fzf returns nothing (e.g. when no items
    are valid)
