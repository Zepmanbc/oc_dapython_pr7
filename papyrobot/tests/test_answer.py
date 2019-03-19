#! /usr/bin/env python3
import pytest

from papyrobot.utils.answer import Answer


def test_intro_ok():
    answer = Answer()
    result = answer.response("intro")
    assert type('') == type(result)


def test_nok():
    answer = Answer()
    with pytest.raises(KeyError):
        answer.response("unknown_category")
