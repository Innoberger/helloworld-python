import pytest
from src.helloworld import *

def test_helloname_noarg():
    with pytest.raises(TypeError):
        assert helloname()

def test_helloname_emptystring():
    assert helloname("") == "Hello "

def test_helloname_john():
    assert helloname("John") == "Hello John"
