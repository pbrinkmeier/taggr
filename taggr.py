#!/usr/bin/env python2

import copy
import os
import sys
import taglib
import util

def quit():
    if tags_modified:
        print "Throwing away modifications."

    sys.exit(0)

def save_tags():
    global tags_modified

    if tags_modified:
        mp3file.save()
        tags_modified = False

        print "Tags saved to file."
    else:
        print "No modifications."

prompt = '> '

if len(sys.argv) != 2:
    print "Usage: taggr.py [file name]"

    sys.exit(1)

filename = sys.argv[1]

if not os.path.isfile(filename):
    print "{} is not a file.".format(filename)

mp3file = taglib.File(filename)

util.list_tags(mp3file)
print "Enter '?' for help."

last_saved_tags = copy.deepcopy(mp3file.tags)
tags_modified = False

while True:
    try:
        input = raw_input(prompt).split(' ')
    except KeyboardInterrupt:
        quit()

    instruction = input[0]
    operands = input[1:]

    if instruction in util.tag_commands:
        # TODO: only set if a different value was entered
        cmd_tag = util.tag_commands[instruction]['tag']
        cmd_name = util.tag_commands[instruction]['name']
        new_value = unicode(' '.join(operands))

        mp3file.tags[
            unicode(cmd_tag)
        ] = [new_value]
        tags_modified = True

        print "Set {} to '{}'.".format(cmd_name, new_value)
    elif instruction == 'd':
        cmd_tag = util.tag_commands[operands[0]]['tag']
        cmd_name = util.tag_commands[operands[0]]['name']

        if operands[0] in util.tag_commands:
            if cmd_tag in mp3file.tags:
                del mp3file.tags[cmd_tag]
                tags_modified = True

                print "Deleted {} tag.".format(cmd_name)
    elif instruction == 'r':
        # TODO: Check if initial_tags deep-equal initial_tags
        mp3file.tags = last_saved_tags
        tags_modified = False

        print "Tags restored to last save."
    elif instruction == 'h' or instruction == '?':
        util.print_help()
    elif instruction == 'l':
        util.list_tags(mp3file)
    elif instruction == 'e' or instruction == 'q':
        quit()
    elif instruction == 's':
        save_tags()
    elif instruction == '.':
        save_tags()
        quit()
    else:
        print "Unrecognized instruction: {}".format(instruction)
