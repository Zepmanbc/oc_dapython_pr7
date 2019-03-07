#! /usr/bin/env python
import os

import googlemaps
from mediawiki import MediaWiki

class Question():

    def __init__(self):
        pass

    def analyze(self):
        return ""

class Answer():

    def __init__(self, infos):
        pass

class Information():

    def __init__(self):
        self.story = str()
        self.url_map = str()

    def ask_gmap(self, query):
        pass

    def ask_wiki(self, query):
        pass

if __name__ == "__main__":
    question = input("poser une question")
    key_words = Question.analyze(question)
    infos = Information()
    if infos.ask_gmap(key_words):
        infos.ask_wiki(key_words)
    print(Answer(infos))
    pass
