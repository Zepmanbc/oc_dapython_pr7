#! /usr/bin/env python


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
        pass

    def get_map(self, query):
        pass

    def get_story(self, query):
        pass

if __name__ == "__main__":
    question = input("poser une question")
    question_analysed = Question.analyze(question)
    infos = Information()
    infos.get_map(question_analysed)
    if infos.get_map(question_analysed):
        infos.get_story(question_analysed)
    print(Answer(infos))
    pass
