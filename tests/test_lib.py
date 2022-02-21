# tests/test_lib.py
from sharecode.lib import try_me

def test_try_me():
    result = try_me(default=False)

    assert type(result) == str
