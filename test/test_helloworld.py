import pytest
from src.helloworld import *

def test_helloworld_witharg():
    with pytest.raises(TypeError):
        helloworld("")

def test_helloworld_noarg():
    assert helloworld() == "Hello World"
