#! /usr/bin/env python3
import sys
import pytest

sys.path.append('papyrobot/')
from utils.answer import Answer

class TestAnswer():

    def setup(self):
        pass

    def teardown(self):
        pass

    def test_first(self):
        assert 1