#! /usr/bin/env python3
import pytest
from unittest.mock import MagicMock

from papyrobot.utils import information


class TestInformationGMap():

    @pytest.fixture
    def MockMediaWiki(self, monkeypatch):
        Mock_mw = MagicMock(information.mediawiki)
        monkeypatch.setattr('papyrobot.utils.information.mediawiki', Mock_mw)

    def test_ask_gmap_ok_mk(self, MockMediaWiki, monkeypatch):
        class MockClient:
            def __init__(self, key):
                pass

            def geocode(self, search):
                return [{'address_components': [{'long_name': 'Cité Paradis', 'short_name': 'Cité Paradis', 'types': ['route']}, {'long_name': 'Paris', 'short_name': 'Paris', 'types': ['locality', 'political']}], 'formatted_address': '7 Cité Paradis, 75010 Paris, France', 'geometry': {'location': {'lat': 48.8747265, 'lng': 2.3505517}}}]

        monkeypatch.setattr('papyrobot.utils.information.googlemaps.Client', MockClient)

        infos = information.Information()
        key_words = "openclassrooms"
        infos.ask_gmap(key_words)
        result = (infos.formatted_address, infos.street_city, infos.location)
        waited = ("7 Cité Paradis, 75010 Paris, France", 'Cité Paradis Paris', (48.8747265, 2.3505517))
        assert result == waited

    def test_ask_gmap_fail_mk(self, MockMediaWiki, monkeypatch):
        class MockClient:
            def __init__(self, key):
                pass

            def geocode(self, search):
                return []

        monkeypatch.setattr('papyrobot.utils.information.googlemaps.Client', MockClient)

        infos = information.Information()
        key_words = "toto"
        result = infos.ask_gmap(key_words)
        assert not result

    def test_ask_gmap_no_route_mk(self, MockMediaWiki, monkeypatch):
        class MockClient:
            def __init__(self, key):
                pass

            def geocode(self, search):
                data = [{
                            'address_components': [
                                {'long_name': 'Pisa', 'short_name': 'Pisa', 'types': ['locality', 'political']},
                                {'long_name': 'Provincia di Pisa', 'short_name': 'PI', 'types': ['administrative_area_level_2', 'political']},
                                {'long_name': 'Italy', 'short_name': 'IT', 'types': ['country', 'political']},
                                {'long_name': '56126', 'short_name': '56126', 'types': ['postal_code']}
                            ],
                            'formatted_address': 'Piazza del Duomo, 56126 Pisa PI, Italy',
                            'geometry': {'location': {'lat': 43.722952, 'lng': 10.396597}}
                        }]
                return data

        monkeypatch.setattr('papyrobot.utils.information.googlemaps.Client', MockClient)

        infos = information.Information()
        key_words = "tour pise"
        infos.ask_gmap(key_words)
        result = (infos.street_city)
        waited = ("Pisa")
        assert result == waited

    def test_ask_gmap_no_locality_mk(self, MockMediaWiki, monkeypatch):
        class MockClient:
            def __init__(self, key):
                pass

            def geocode(self, search):
                data = [{
                            'address_components': [
                                {'long_name': 'Pisa', 'short_name': 'Pisa', 'types': ['route', 'political']},
                                {'long_name': '56126', 'short_name': '56126', 'types': ['postal_code']}
                            ],
                            'formatted_address': 'Piazza del Duomo, 56126 Pisa PI, Italy',
                            'geometry': {'location': {'lat': 43.722952, 'lng': 10.396597}}
                        }]
                return data

        monkeypatch.setattr('papyrobot.utils.information.googlemaps.Client', MockClient)

        infos = information.Information()
        key_words = "tour pise"
        infos.ask_gmap(key_words)
        result = (infos.street_city)
        waited = ("Pisa")
        assert result == waited
