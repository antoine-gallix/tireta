from pdb import set_trace as bp
from pytest import fixture
from pathlib import Path
from textwrap import dedent
from client import text_lib
from .conftest import SIMPLE_TEXT, TAGGED_TEXT, TAG_MARK, TAGS

# ---------------------unit tests---------------------


def test_read_file(note_file):
    # read and check
    read_text = text_lib.get_note_text(note_file)
    assert read_text == SIMPLE_TEXT


def test_extract_tags():
    filtered_text, tags = text_lib.extract_tags(TAGGED_TEXT, TAG_MARK)
    assert filtered_text == SIMPLE_TEXT
    assert len(tags) == len(TAGS)
    assert set(tags) == set(TAGS)
