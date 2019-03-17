import pytest
from unittest.mock import MagicMock
import json

from flask import Flask, render_template, jsonify, request

from papyrobot import app
from papyrobot.utils import information


@pytest.fixture
def client():
    client = app.test_client()
    return client


def test_index(client):
    response = client.get("/")
    assert response.status_code == 200

def test_ajax_no_response(client, monkeypatch):
    """ /ajax?question=dsfsfdafgsfdg

    {
    "keywords": "dsfsfdafgsfdg", 
    "no_result": "hum hum... Je ne sais pas, peut \u00eatre que je pourrais te r\u00e9pondre si tu me posais une question \u00e0 laquelle j'ai une r\u00e9ponse!"
    }
    """
    information.googlemaps = MagicMock()
    information.mediawiki = MagicMock()
    MockAskGmap = MagicMock(information.Information.ask_gmap)
    MockAskGmap.return_value = False

    monkeypatch.setattr('papyrobot.utils.information.Information.ask_gmap', MockAskGmap)

    response = client.get("/ajax?question=dsfsfdafgsfdg")
    assert response.status_code == 200

    data = json.loads(response.data)
    # print(data)
    assert data["no_result"]

def test_ajax_response(client, monkeypatch):
    """ /ajax?question=Salut%20GrandPy%20!%20Est-ce%20que%20tu%20connais%20l%27adresse%20d%27OpenClassrooms%20?
    {
    "formatted_address": "7 Cit\u00e9 Paradis, 75010 Paris, France", 
    "intro": "J'y allais r\u00e9guli\u00e8rement \u00e0 une \u00e9poque, c'est \u00e0 cette adresse : ", 
    "introduce_story": "Je connais tr\u00e8s bien ce coin-l\u00e0! ", 
    "keywords": "OpenClassrooms", 
    "location": [
        48.8747265, 
        2.3505517
    ], 
    "story": "La cit\u00e9 Paradis est une voie publique situ\u00e9e dans le 10e arrondissement de Paris. Elle est en forme de t\u00e9, une branche d\u00e9bouche au 43, rue de Paradis, la deuxi\u00e8me au 57, rue d'Hauteville et la troisi\u00e8me en impasse.", 
    "street_city": "Cit\u00e9 Paradis Paris"
    }
    """
    information.googlemaps = MagicMock()
    information.mediawiki = MagicMock()
    MockAskGmap = MagicMock(information.Information.ask_gmap)
    MockAskGmap.return_value = True
    monkeypatch.setattr('papyrobot.utils.information.Information.ask_gmap', MockAskGmap)

    MockAskWiki = MagicMock(information.Information.ask_wiki)
    MockAskWiki.return_value = True
    monkeypatch.setattr('papyrobot.utils.information.Information.ask_wiki', MockAskWiki)

    response = client.get("/ajax?question=Salut%20GrandPy%20!%20Est-ce%20que%20tu%20connais%20l%27adresse%20d%27OpenClassrooms%20?")
    assert response.status_code == 200

    data = json.loads(response.data)
    # print(data)
    assert "location" in data

def test_ajax_response_wiki_second(client, monkeypatch):
    """ /ajax?question=zone%2051
    {
    "formatted_address": "Homey Airport, Nevada, USA", 
    "intro": "Bien sur mon poussin, voici l'adresse : ", 
    "introduce_story": "Je vais t'en raconter un peu plus d'ailleurs : ", 
    "keywords": "zone 51", 
    "location": [
        37.2371623, 
        -115.8018432
    ], 
    "story": "La zone 51 est une aire g\u00e9ographique du Nevada aux \u00c9tats-Unis \u2014 aussi appel\u00e9e Dreamland, Watertown, The Ranch, Paradise Ranch, The Farm, The Box, Groom Lake, Zone 51 A, Neverland ou encore The Directorate for Development Plans Area \u2014 o\u00f9 se trouve une base militaire dite secr\u00e8te, testant entre autres des appareils exp\u00e9rimentaux. Elle est mentionn\u00e9e pour la premi\u00e8re fois sur des documents officiels am\u00e9ricains d\u00e9classifi\u00e9s en ao\u00fbt 2013 d\u00e9crivant les essais secrets de l'avion Lockheed U-2.Depuis 1989, elle est li\u00e9e aux th\u00e9ories d'OVNI. Le milieu ufologique la reprend fr\u00e9quemment \u00e0 son compte pour \u00e9laborer diverses th\u00e9ories conspirationnistes sugg\u00e9rant des relations secr\u00e8tes entre l'arm\u00e9e am\u00e9ricaine et des extraterrestres. Dans ce milieu complotiste, elle est connue sous son appellation anglaise Area 51.", 
    "street_city": "Homey Airport"
    }
    """
    information.googlemaps = MagicMock()
    information.mediawiki = MagicMock()
    MockAskGmap = MagicMock(information.Information.ask_gmap)
    MockAskGmap.return_value = True
    monkeypatch.setattr('papyrobot.utils.information.Information.ask_gmap', MockAskGmap)

    MockAskWiki = MagicMock(information.Information.ask_wiki)
    MockAskWiki.side_effect = [False, True]
    monkeypatch.setattr('papyrobot.utils.information.Information.ask_wiki', MockAskWiki)

    response = client.get("/ajax?question=zone%2051")
    assert response.status_code == 200

    data = json.loads(response.data)
    # print(data)
    assert "location" in data