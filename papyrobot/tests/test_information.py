#! /usr/bin/env python3
import sys
import pytest

sys.path.append('papyrobot/')
# import utils.information
from utils.information import Information

class TestAnswer():

    def setup(self):
        self.infos = Information()

    def teardown(self):
        pass

    def test_ask_gmaip_ok(self):
        key_words = "openclassrooms"
        self.infos.ask_gmap(key_words)
        result = (self.infos.formatted_address, self.infos.street_city, self.infos.location)
        waited = ("7 Cité Paradis, 75010 Paris, France", 'Cité Paradis Paris', (48.8747265, 2.3505517))
        assert result == waited

    def test_ask_gmaip_fail(self):
        key_words = "toto"
        result = self.infos.ask_gmap(key_words)
        assert not result

    def test_ask_wiki_ok(self):
        key_words = "Citée Paradis"
        self.infos.ask_wiki(key_words)
        result = self.infos.story
        waited = "La cité Paradis est une voie publique située dans le 10e arrondissement de Paris. Elle est en forme de té, une branche débouche au 43, rue de Paradis, la deuxième au 57, rue d'Hauteville et la troisième en impasse."
        assert result == waited

    def test_ask_wiki_no_situation(self):
        key_words = "Champ de Mars Paris"
        self.infos.ask_wiki(key_words)
        result = self.infos.story
        waited = "Le Champ-de-Mars est un vaste jardin public, entièrement ouvert et situé à Paris dans le 7e arrondissement, entre la tour Eiffel au nord-ouest et l'École militaire au sud-est. Avec ses 24,5 ha, le jardin du Champ-de-Mars est l'un des plus grands espaces verts de Paris. Riche d'une histoire bicentenaire, le Champ-de-Mars accueille les Parisiens et les touristes toute l'année autour d'un vaste ensemble d'activités."
        assert result == waited

    def test_ask_wiki_fail(self):
        key_words = "Citée Par"
        result = self.infos.ask_wiki(key_words)
        assert not result
        