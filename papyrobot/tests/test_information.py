#! /usr/bin/env python3
import sys
import pytest
from unittest.mock import MagicMock

sys.path.append('papyrobot/')
from utils.information import Information
from utils import information
import mediawiki

class TestAnswer():

    def setup(self):
        information.MediaWiki = MagicMock()
        self.infos = Information()
        self.infos.gmaps = MagicMock()
        self.infos.wikipedia = MagicMock()

    def teardown(self):
        pass

    def test_ask_gmap_ok(self):
        self.infos.gmaps.geocode.return_value = [{
                'address_components': [
                    {'long_name': 'Cité Paradis', 'short_name': 'Cité Paradis', 'types': ['route']},
                    {'long_name': 'Paris', 'short_name': 'Paris', 'types': ['locality', 'political']}
                ],
                'formatted_address': '7 Cité Paradis, 75010 Paris, France',
                'geometry': {'location': {'lat': 48.8747265, 'lng': 2.3505517}}
            }]

        key_words = "openclassrooms"
        self.infos.ask_gmap(key_words)
        result = (self.infos.formatted_address, self.infos.street_city, self.infos.location)
        waited = ("7 Cité Paradis, 75010 Paris, France", 'Cité Paradis Paris', (48.8747265, 2.3505517))
        assert result == waited

    def test_ask_gmap_fail(self):
        self.infos.gmaps.geocode.return_value = []

        key_words = "toto"
        result = self.infos.ask_gmap(key_words)
        assert not result

    def test_ask_gmap_no_route(self):
        self.infos.gmaps.geocode.return_value = [{
                'address_components': [
                    {'long_name': 'Pisa', 'short_name': 'Pisa', 'types': ['locality', 'political']},
                    {'long_name': 'Provincia di Pisa', 'short_name': 'PI', 'types': ['administrative_area_level_2', 'political']},
                    {'long_name': 'Italy', 'short_name': 'IT', 'types': ['country', 'political']},
                    {'long_name': '56126', 'short_name': '56126', 'types': ['postal_code']}
                ],
                'formatted_address': 'Piazza del Duomo, 56126 Pisa PI, Italy',
                'geometry': {'location': {'lat': 43.722952, 'lng': 10.396597}}
            }]

        key_words = "tour pise"
        self.infos.ask_gmap(key_words)
        result = self.infos.street_city
        waited = "Pisa"
        assert result == waited

    def test_ask_gmap_no_locality(self):
        self.infos.gmaps.geocode.return_value = [{
                'address_components': [
                    {'long_name': 'Pisa', 'short_name': 'Pisa', 'types': ['route', 'political']},
                    {'long_name': 'Provincia di Pisa', 'short_name': 'PI', 'types': ['administrative_area_level_2', 'political']},
                    {'long_name': 'Italy', 'short_name': 'IT', 'types': ['country', 'political']},
                    {'long_name': '56126', 'short_name': '56126', 'types': ['postal_code']}
                ],
                'formatted_address': 'Piazza del Duomo, 56126 Pisa PI, Italy',
                'geometry': {'location': {'lat': 43.722952, 'lng': 10.396597}}
            }]

        key_words = "tour pise"
        self.infos.ask_gmap(key_words)
        result = self.infos.street_city
        waited = "Pisa"
        assert result == waited

    def test_ask_wiki_ok(self):
        self.infos.wikipedia.search.return_value = ['']
        page = MagicMock()
        page.content = "La cité Paradis est une voie publique située dans le 10e arrondissement de Paris.\n\n\n== Situation et accès ==\nLa cité Paradis est une voie publique située dans le 10e arrondissement de Paris. Elle est en forme de té, une branche débouche au 43, rue de Paradis, la deuxième au 57, rue d'Hauteville et la troisième en impasse.\n\nVues de la cité\n\t\t\n\t\t\nCe site est desservi par les lignes \u2009\u200d\u2009\u200d à la station de métro Bonne-Nouvelle et par la ligne \u2009\u200d à la station Poissonnière.\n\n\n== Origine du nom ==\nElle porte ce nom en raison de sa proximité avec la rue éponyme.\n\n\n== Historique ==\nLa cité Paradis a été aménagée sur les anciens jardins de l'hôtel Titon dont la façade arrière est visible au fond de l'impasse.\nLa partie débouchant rue de Paradis a été ouverte en 1893 et celle débouchant rue d'Hauteville en 1906.\n\n\n== Références ==\n\n\n== Bibliographie ==\nJacques Hillairet, Dictionnaire historique des rues de Paris, Paris, Les Éditions de Minuit, 1972, 1985, 1991, 1997 , etc. (1re éd. 1960), 1 476 p., 2 vol.  [détail des éditions] (ISBN 2-7073-1054-9, OCLC 466966117, présentation en ligne).\n\n\n== Annexes ==\n\n\n=== Articles connexes ===\nListe des voies du 10e arrondissement de Paris\n\n\n=== Liens externes ===\nCité Paradis (mairie de Paris) Portail de Paris   Portail de la route"
        self.infos.wikipedia.page.return_value = page

        key_words = "Citée Paradis"
        self.infos.ask_wiki(key_words)
        result = self.infos.story
        waited = "La cité Paradis est une voie publique située dans le 10e arrondissement de Paris. Elle est en forme de té, une branche débouche au 43, rue de Paradis, la deuxième au 57, rue d'Hauteville et la troisième en impasse."
        assert result == waited

    def test_ask_wiki_no_situation(self):
        self.infos.wikipedia.search.return_value = ['']
        page = MagicMock()
        page.content = "Le Champ-de-Mars est un vaste jardin public, entièrement ouvert et situé à Paris dans le 7e arrondissement, entre la tour Eiffel au nord-ouest et l'École militaire au sud-est. Avec ses 24,5 ha, le jardin du Champ-de-Mars est l'un des plus grands espaces verts de Paris. Riche d'une histoire bicentenaire, le Champ-de-Mars accueille les Parisiens et les touristes toute l'année autour d'un vaste ensemble d'activités.\n\n\n== Origine du nom ==\nSon nom vient du Champ de Mars romain (et donc du dieu romain de la guerre, Mars).\n\n\n== Historique =="
        self.infos.wikipedia.page.return_value = page

        key_words = "Champ de Mars Paris"
        self.infos.ask_wiki(key_words)
        result = self.infos.story
        waited = "Le Champ-de-Mars est un vaste jardin public, entièrement ouvert et situé à Paris dans le 7e arrondissement, entre la tour Eiffel au nord-ouest et l'École militaire au sud-est. Avec ses 24,5 ha, le jardin du Champ-de-Mars est l'un des plus grands espaces verts de Paris. Riche d'une histoire bicentenaire, le Champ-de-Mars accueille les Parisiens et les touristes toute l'année autour d'un vaste ensemble d'activités."
        assert result == waited

    def test_ask_wiki_fail(self):
        self.infos.wikipedia.search.return_value = ['']
        self.infos.wikipedia.page.side_effect = mediawiki.exceptions.DisambiguationError('','','')

        key_words = "Cité par"
        result = self.infos.ask_wiki(key_words)
        assert not result

    def test_ask_wiki_false(self):
        self.infos.wikipedia.search.return_value = []
        key_words = "Homey Airport"
        result = self.infos.ask_wiki(key_words)
        assert not result
        