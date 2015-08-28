# taggr

Interactive command-line mp3 tagger.

## Requirements

- Python 2.7
- [pytaglib pip package](https://pypi.python.org/pypi/pytaglib)

## Usage

```
./taggr.py snap_out_of_it.mp3
title: Snap out of it
Enter '?' for help.
> ?
Commands:
t [title] - set title
a [artist] - set artist
b [album] - set album
d [t|a|b] - delete a tag
r - restore tags to last save
l - list tags
h, ? - display this help page
e, q - exit without saving
s - save tags to file
. - save tags to file and exit
> a Arctic Monkeys
Artist set to 'Arctic Monkeys'.
> s
Tags saved to file.
> b AM
Album set to 'AM'.
> e
Throwing away modifications.
```
