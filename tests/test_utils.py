from tests.utils import is_in


def test_is_in():
    sub = {'a': 12}
    sup = {'a': 12, 'b': 13}
    assert is_in(sub, sup)
    assert is_in(sup, sub) is False
