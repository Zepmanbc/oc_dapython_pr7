#! /usr/bin/env python
import os

from flask import Flask, render_template, jsonify, request
from papyrobot.utils.information import Information
from papyrobot.utils.question import Question
from papyrobot.utils.answer import Answer

app = Flask(__name__)

# app.config.from_object('config')
@app.route('/') 
def index(): 
    return render_template("index.html", GMAPKEY=os.environ['GMAPKEY'])

@app.route('/ajax',  methods=['GET', 'POST'])
def ajax_request():
    query = request.args.get('question')
    if query:
        question = Question()
        key_words = question.analyze(query)
        info = Information()
        if info.ask_gmap(key_words):
            info.ask_wiki(info.street_city)
            return jsonify(
                keywords=key_words,
                formatted_address=info.formatted_address,
                location=info.location,
                street_city=info.street_city,
                story=info.story)
    return jsonify()

if __name__ == "__main__": 
    app.run()
