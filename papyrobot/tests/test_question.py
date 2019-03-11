#! /usr/bin/env python3
import sys
import pytest

sys.path.append('papyrobot/')
# import utils.question
from utils.question import Question

"""
Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?
où se trouve l'Arc de Triomphe?
Quelle est l'adresse de la Tour Eiffel?
Dis Papy, c'est quoi l'adresse de l'Elysée?
Tu connais l'adresse de l'Opéra Garnier?
"""

class TestAnswer():

    def setup(self):
        self.question = Question()

    def teardown(self):
        pass

    def test_question_1(self):
        query = "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?"
        wanted = "OpenClassrooms"
        result = self.question.analyze(query)
        assert result == wanted

    def test_question_2(self):
        query = "où se trouve l'Arc de Triomphe?"
        wanted = "Arc Triomphe"
        result = self.question.analyze(query)
        assert result == wanted

    def test_question_3(self):
        query = "Quelle est l'adresse de la Tour Eiffel?"
        wanted = "Tour Eiffel"
        result = self.question.analyze(query)
        assert result == wanted

    def test_question_4(self):
        query = "Dis Papy, c'est quoi l'adresse de l'Elysée?"
        wanted = "Elysée"
        result = self.question.analyze(query)
        assert result == wanted

    def test_question_5(self):
        query = "Tu connais l'adresse de l'Opéra Garnier?"
        wanted = "Opéra Garnier"
        result = self.question.analyze(query)
        assert result == wanted

    def test_question_null(self):
        query = ""
        wanted = ""
        result = self.question.analyze(query)
        assert result == wanted