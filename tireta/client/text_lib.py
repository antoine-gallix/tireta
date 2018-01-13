from pathlib import Path
import logging


def get_note_text(file_path):
    """Get text from a file"""

    file = Path(file_path).expanduser().resolve()
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
