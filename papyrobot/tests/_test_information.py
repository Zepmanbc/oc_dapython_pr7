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
        key_words = "adresse openclassrooms"
        result = self.infos.ask_gmap(key_words)
        waited = ['Citée Paradis', (48.8747265, 2.3505517)]
        assert result == waited

    def test_ask_gmaip_fail(self):
        key_words = "Citée Parad"
        result = self.infos.ask_gmap(key_words)
        assert not result

    def test_ask_wiki_ok(self):
        key_words = "Citée Paradis"
        result = self.infos.ask_wiki(key_words)
        waited = "La cité Paradis est une voie publique située dans le 10e arrondissement de Paris. Elle est en forme de té, une branche débouche au 43, rue de Paradis, la deuxième au 57, rue d'Hauteville et la troisième en impasse."
        assert result == waited

    def test_ask_wiki_fail(self):
        key_words = "Citée Parad"
        result = self.infos.ask_wiki(key_words)
        assert not result
        