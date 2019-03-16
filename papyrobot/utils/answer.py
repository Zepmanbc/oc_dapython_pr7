#! /usr/bin/env python
"""Random Answer module"""
import json
from random import randint


class Answer():
    """Answer class.

        answer = Amswer()
        print(answer.response(category))

        return: str

    Categories:
        intro
        introduce_story
        no_result

    sentences are in 'papyrobot/static/json/dialog.json'
    """

    def __init__(self):
        """Initialise sentenses."""
        with open('papyrobot/static/json/dialog.json') as json_data:
            self.dialog = json.load(json_data)

    def response(self, category):
        """Return a sentence for a choosen category.

        Arg:
            category (str): from self.dialog keys

        Return:
            str: randomly choosen sentence forn the category

        Error:
            KeyError: if category unknown
        """
        if category in self.dialog.keys():
            return self.dialog[category][randint(0, len(self.dialog[category]) - 1)]
        else:
            raise KeyError("Incorrect Category")


if __name__ == "__main__":
    # answer = Answer()
    # print(answer.response('ff'))
    pass
