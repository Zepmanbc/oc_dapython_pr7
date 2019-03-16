#! /usr/bin/env python3
import sys
import pytest

from papyrobot.utils.answer import Answer

class TestAnswer():

    def setup(self):
        self.answer = Answer()

    def teardown(self):
        pass

    def test_intro_ok(self):
        result = self.answer.response("intro")
        assert type('') == type(result)

    def test_nok(self):
        with pytest.raises(KeyError):
            self.answer.response("unknown_category")
