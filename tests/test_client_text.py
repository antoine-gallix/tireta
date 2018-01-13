from pdb import set_trace as bp
from pytest import fixture
from pathlib import Path
from textwrap import dedent
from tireta.client import text_lib


TAG_MARK = '@:'
TAGS = ['pif', 'paf', 'pouf', 'ploc']
SIMPLE_TEXT = dedent("""\
              this is
              a text with
              only four lines
              in it\
              """)

tag_line = TAG_MARK + ','.join(TAGS)
TAGGED_TEXT = '\n'.join([tag_line, SIMPLE_TEXT])


@fixture
def tmpfile(tmpdir):
    file_path = Path(tmpdir / 'test_file')
    return file_path


# ---------------------unit tests---------------------


def test_read_file(tmpfile):
    # write test file
    tmpfile.write_text(SIMPLE_TEXT)
    # read and check
    read_text = text_lib.get_note_text(tmpfile)
    assert read_text == SIMPLE_TEXT


def test_extract_tags():
    filtered_text, tags = text_lib.extract_tags(TAGGED_TEXT, TAG_MARK)
    assert filtered_text == SIMPLE_TEXT
    assert len(tags) == len(TAGS)
    assert set(tags) == set(TAGS)
