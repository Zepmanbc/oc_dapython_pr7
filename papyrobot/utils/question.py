#! /usr/bin/env python
import json


class Question():

    def __init__(self):
        with open('papyrobot/static/json/stopwords_fr.json') as json_data: 
            self.stopwords = json.load(json_data)
        stopword_custom = ['adresse', 'trouve', 'quelle', 'quel', 'papy', 'grandpy', 'connais', 'dis', 'salut']
        [self.stopwords.append(x) for x in stopword_custom]
        self.punctuation = [",", ".", "?", "!", ";", "'", "-"]


    def analyze(self, query):
        analyzed_list = list()
        query = query.lower()
        for punc in self.punctuation:
            query = query.replace(punc, ' ')
        for word in query.split():
            if not word in self.stopwords:
                analyzed_list.append(word)
        analyzed = ' '.join(analyzed_list)
        return analyzed

if __name__ == "__main__":
    """
    Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?
    où se trouve l'Arc de Triomphe?
    Quelle est l'adresse de la Tour Eiffel?
    Dis Papy, c'est quoi l'adresse de l'Elysée?
    Tu connais l'adresse de l'Opéra Garnier?
    """
    # import os
    # os.system('clear')
    # question = Question()
    # query = "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?"
    # query = "où se trouve l'Arc de Triomphe?"
    # query = "Quelle est l'adresse de la Tour Eiffel?"
    # query = "Dis Papy, c'est quoi l'adresse de l'Elysée?"
    # query = "Tu connais l'adresse de l'Opéra Garnier?"
    # print(question.analyze(query))
    pass
