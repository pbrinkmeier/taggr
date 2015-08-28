tag_commands = {
    't': {
        'tag': u'TITLE',
        'name': u'title'
    },
    'a': {
        'tag': u'ARTIST',
        'name': 'artist'
    },
    'b': {
        'tag': u'ALBUM',
        'name': 'album'
    }
}

def list_tags(mp3file):
    """Prints out the tags in the file which are set and also supported by taggr."""

    for command, command_data in tag_commands.items():
        if command_data['tag'] in mp3file.tags:
            print '{}: {}'.format(
                command_data['name'],
                mp3file.tags[command_data['tag']][0]
            )

def print_help():
    """Prints out a help page."""

    print "Commands:"

    for command, command_data in tag_commands.items():
        print "{} [{}] - set {}".format(
            command,
            command_data['name'],
            command_data['name']
        )

    print """d [{}] - delete a tag
l - List tags
h, ? - display this help page
e, q - exit without saving
s - save tags to file""".format('|'.join(tag_commands.keys()))
