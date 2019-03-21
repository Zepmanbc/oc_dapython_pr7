#! /usr/bin/env python3
import pytest

from papyrobot.utils.answer import Answer


def test_intro_ok():
    """Test if answer.response return a string."""
    answer = Answer()
    result = answer.response("intro")
    assert type('') == type(result)


def test_nok():
    """Test if KeyError is raised with unknwon category from json."""
    answer = Answer()
    with pytest.raises(KeyError):
        answer.response("unknown_category")
