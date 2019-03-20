#! /usr/bin/env python
"""Question module"""
import re
from string import punctuation
import json


class Question():
    """Question Class.

    question = Question()
    query = "Salut GrandPy! Est-ce que tu connais l'adresse d'OpenClassrooms ?"
    question.analyse(query)

    return "OpenClassrooms"
    """

    def __init__(self):
        """Init needed filters.

        loads standard stopwords
        loads custom stopwords

        """
        with open('papyrobot/static/json/stopwords_fr.json') as json_data:
            self.stopwords = json.load(json_data)
        with open('papyrobot/static/json/stopwords_custom.json') as json_data:
            self.stopwords += json.load(json_data)

    def analyze(self, query):
        """Remove all unnecesary words.

        Args:
            query (str): the string send by user

        Return:
            str: cleaned string

        """
        # remove punctuation from query
        query = query.translate(query.maketrans(punctuation, " " * len(punctuation)))
        # remove GrandPy, PyBot like words
        query = re.sub(r"(([a-zA-Z-]*[bB]ot|[a-zA-Z-]*[pP]y))", "", query)
        # remove "Monsieur|Madame|Mademoiselle x"
        query = re.sub(r"([mM]onsieur|[mM]adame|[mM]ademoiselle) \w*", "", query)
        # remove stopwords
        analyzed = ' '.join([x for x in query.split() if not x.lower() in self.stopwords])
        return analyzed


if __name__ == "__main__":
    # import os
    # os.system('clear')
    # question = Question()
    # query = "Salut GrandPy ! PyBot GrandBot Est-ce que tu connais l'adresse d'OpenClassrooms ?"
    # query = "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?"
    # query = "où se trouve l'Arc de Triomphe?"
    # query = "Quelle est l'adresse de la Tour Eiffel?"
    # query = "Dis Papy, c'est quoi l'adresse de l'Elysée?"
    # query = "Tu connais l'adresse de l'Opéra Garnier?"
    # print(question.analyze(query))
    pass
