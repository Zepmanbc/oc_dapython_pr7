#! /usr/bin/env python
"""Views manager."""
import os

from flask import Flask, render_template, jsonify, request, redirect, url_for
from .utils.information import Information
from .utils.question import Question
from .utils.answer import Answer

app = Flask(__name__)


@app.route('/')
def index():
    """Index page"""
    return render_template("index.html", GMAPKEY=os.environ['GMAPKEY_FRONT'])


@app.errorhandler(404)
def page_not_found(e):
    """Redirect to index for all 'false' urls."""
    return redirect(url_for('index'), code=302)


@app.route('/ajax', methods=['GET'])
def ajax_request():
    """Request page, return json."""
    response_dict = {}
    answer = Answer()
    query = request.args.get('question')
    if query is not None:
        question = Question()
        keywords = question.analyze(query)
        info = Information()
        if info.ask_gmap(keywords):
            if not info.ask_wiki(info.street_city):
                info.ask_wiki(keywords)
            response_dict = {
                "intro": answer.response("intro"),
                "introduce_story": answer.response("introduce_story"),
                "keywords": keywords,
                "formatted_address": info.formatted_address,
                "location": info.location,
                "street_city": info.street_city,
                "story": info.story
            }
        else:
            response_dict = {
                "no_result": answer.response("no_result"),
                "keywords": keywords
            }
    return jsonify(response_dict)
