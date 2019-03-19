#! /usr/bin/env python3

import pytest

from papyrobot.utils.question import Question

"""
Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?
où se trouve l'Arc de Triomphe?
Quelle est l'adresse de la Tour Eiffel?
Dis Papy, c'est quoi l'adresse de l'Elysée?
Tu connais l'adresse de l'Opéra Garnier?
"""


@pytest.fixture
def question():
    question = Question()
    return question


def test_question_1(question):
    query = "Salut GrandPy! Est-ce que tu connais l'adresse d'OpenClassrooms ?"
    wanted = "OpenClassrooms"
    result = question.analyze(query)
    assert result == wanted


def test_question_2(question):
    query = "où se trouve l'Arc de Triomphe?"
    wanted = "Arc Triomphe"
    result = question.analyze(query)
    assert result == wanted


def test_question_3(question):
    query = "Quelle est l'adresse de la Tour Eiffel?"
    wanted = "Tour Eiffel"
    result = question.analyze(query)
    assert result == wanted


def test_question_4(question):
    query = "Dis Papy, c'est quoi l'adresse de l'Elysée?"
    wanted = "Elysée"
    result = question.analyze(query)
    assert result == wanted


def test_question_5(question):
    query = "Tu connais l'adresse de l'Opéra Garnier?"
    wanted = "Opéra Garnier"
    result = question.analyze(query)
    assert result == wanted


def test_question_null(question):
    query = ""
    wanted = ""
    result = question.analyze(query)
    assert result == wanted
