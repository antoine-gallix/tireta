from pathlib import Path
import json
import logging

tag_mark = '#TAGS:'


def get_note_text(file):
    """Get text from a file"""
    logging.info('reading file : {}'.format(file))
    text = file.read_text()
    return text


def extract_tags(text, tag_mark):
    """Extract tags from a string

    returns : (text,tags)
        text : filtered text
        tags : list of tags
    """
    lines = text.split('\n')
    tags = []
    note_lines = []
    for l in lines:
        if l.startswith(tag_mark):
            tag_string = l[len(tag_mark):]
            tags.extend(tag_string.split(','))
        else:
            note_lines.append(l)
    tags = [t.strip() for t in tags]  # strip whitespaces
    filtered = '\n'.join(note_lines)
    logging.info('extracted tags : {}'.format(tags))
    return filtered, tags


def read_note(file_path):
    """Extract name, text and tags from a text file
    """
    file = Path(file_path) if not isinstance(file_path, Path) else file_path
    file = file.expanduser().resolve()
    name = file.stem
    raw_text = get_note_text(file)
    text, tags = extract_tags(raw_text, tag_mark)
    payload = {'name': name,
               'body': text,
               'tags': tags}
    return payload


def write_note():
    """Write a 
    """
