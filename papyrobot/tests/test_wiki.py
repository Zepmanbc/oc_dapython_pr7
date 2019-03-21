#! /usr/bin/env python3

import pytest
from unittest.mock import MagicMock

from papyrobot.utils import information


class TestInformationMEdiaWiki():
    """Test for mediawiki lib version"""
    @pytest.fixture
    def MockGmap(self, monkeypatch):
        MockGm = MagicMock(information.googlemaps)
        monkeypatch.setattr('papyrobot.utils.information.googlemaps', MockGm)

    def test_ask_wiki_ok_mk(self, MockGmap, monkeypatch):
        """Test ask_wiki return is ok"""
        class MockSearch:
            def __init__(self):
                pass

            def search(self, query):
                data = ['']
                return data

            def page(self, _title):
                class FakePage():
                    def __init__(self, _title):
                        pass

                    @property
                    def content(self):
                        return "La cité Paradis est une voie publique située dans le 10e arrondissement de Paris.\n\n\n== Situation et accès ==\nLa cité Paradis est une voie publique située dans le 10e arrondissement de Paris. Elle est en forme de té, une branche débouche au 43, rue de Paradis, la deuxième au 57, rue d'Hauteville et la troisième en impasse.\n\nVues de la cité\n\t\t\n\t\t\nCe site est desservi par les lignes \u2009\u200d\u2009\u200d à la station de métro Bonne-Nouvelle et par la ligne \u2009\u200d à la station Poissonnière.\n\n\n== Origine du nom ==\nElle porte ce nom en raison de sa proximité avec la rue éponyme.\n\n\n== Historique ==\nLa cité Paradis a été aménagée sur les anciens jardins de l'hôtel Titon dont la façade arrière est visible au fond de l'impasse.\nLa partie débouchant rue de Paradis a été ouverte en 1893 et celle débouchant rue d'Hauteville en 1906.\n\n\n== Références ==\n\n\n== Bibliographie ==\nJacques Hillairet, Dictionnaire historique des rues de Paris, Paris, Les Éditions de Minuit, 1972, 1985, 1991, 1997 , etc. (1re éd. 1960), 1 476 p., 2 vol.  [détail des éditions] (ISBN 2-7073-1054-9, OCLC 466966117, présentation en ligne).\n\n\n== Annexes ==\n\n\n=== Articles connexes ===\nListe des voies du 10e arrondissement de Paris\n\n\n=== Liens externes ===\nCité Paradis (mairie de Paris) Portail de Paris   Portail de la route"
                return FakePage(_title)

        monkeypatch.setattr('papyrobot.utils.information.mediawiki.MediaWiki', MockSearch)

        infos = information.Information()

        key_words = "Citée Paradis"
        infos.ask_wiki(key_words)
        result = infos.story
        waited = "La cité Paradis est une voie publique située dans le 10e arrondissement de Paris. Elle est en forme de té, une branche débouche au 43, rue de Paradis, la deuxième au 57, rue d'Hauteville et la troisième en impasse."
        assert result == waited

    def test_ask_wiki_no_situation_mk(self, MockGmap, monkeypatch):
        """Test wiki content without 'situation'."""
        class MockSearch:
            def __init__(self):
                pass

            def search(self, query):
                data = ['']
                return data

            def page(self, _title):
                class FakePage():
                    def __init__(self, _title):
                        pass

                    @property
                    def content(self):
                        return "Le Champ-de-Mars est un vaste jardin public, entièrement ouvert et situé à Paris dans le 7e arrondissement, entre la tour Eiffel au nord-ouest et l'École militaire au sud-est. Avec ses 24,5 ha, le jardin du Champ-de-Mars est l'un des plus grands espaces verts de Paris. Riche d'une histoire bicentenaire, le Champ-de-Mars accueille les Parisiens et les touristes toute l'année autour d'un vaste ensemble d'activités.\n\n\n== Origine du nom ==\nSon nom vient du Champ de Mars romain (et donc du dieu romain de la guerre, Mars).\n\n\n== Historique =="
                return FakePage(_title)

        monkeypatch.setattr('papyrobot.utils.information.mediawiki.MediaWiki', MockSearch)

        infos = information.Information()

        key_words = "Champ de Mars Paris"
        infos.ask_wiki(key_words)
        result = infos.story
        waited = "Le Champ-de-Mars est un vaste jardin public, entièrement ouvert et situé à Paris dans le 7e arrondissement, entre la tour Eiffel au nord-ouest et l'École militaire au sud-est. Avec ses 24,5 ha, le jardin du Champ-de-Mars est l'un des plus grands espaces verts de Paris. Riche d'une histoire bicentenaire, le Champ-de-Mars accueille les Parisiens et les touristes toute l'année autour d'un vaste ensemble d'activités."
        assert result == waited

    def test_ask_wiki_fail_mk_DisambiguationError(self, MockGmap, monkeypatch):
        """no pages returned."""
        class MockSearch:
            def __init__(self):
                pass

            def search(self, query):
                return ['']

            def page(self, _title):
                class FakePage():
                    def __init__(self, _title):
                        raise information.mediawiki.exceptions.DisambiguationError('', [''], '')
                return FakePage(_title)

        monkeypatch.setattr('papyrobot.utils.information.mediawiki.MediaWiki', MockSearch)

        infos = information.Information()

        key_words = "Cité par"
        result = infos.ask_wiki(key_words)
        assert not result

    def test_ask_wiki_fail_mk_keyError(self, MockGmap, monkeypatch):
        """no title return in page."""
        class MockSearch:
            def __init__(self):
                pass

            def search(self, query):
                return ['']

            def page(self, _title):
                class FakePage():
                    def __init__(self, _title):
                        raise KeyError
                return FakePage(_title)

        monkeypatch.setattr('papyrobot.utils.information.mediawiki.MediaWiki', MockSearch)

        infos = information.Information()

        key_words = "Cité par"
        result = infos.ask_wiki(key_words)
        assert not result

    def test_ask_wiki_false_mk(self, MockGmap, monkeypatch):
        """Test ask_wiki no result."""
        class MockSearch:
            def __init__(self):
                pass

            def search(self, query):
                return []

        monkeypatch.setattr('papyrobot.utils.information.mediawiki.MediaWiki', MockSearch)

        infos = information.Information()

        key_words = "Homey Airport"
        result = infos.ask_wiki(key_words)
        assert not result


class TestInformationWikiAPI():
    """Tests for request on mediawiki API."""
    @pytest.fixture
    def MockGmMw(self, monkeypatch):
        MockGmaps = MagicMock(information.googlemaps)
        monkeypatch.setattr('papyrobot.utils.information.googlemaps', MockGmaps)
        MockMw = MagicMock(information.mediawiki)
        monkeypatch.setattr('papyrobot.utils.information.mediawiki', MockMw)

    def test_ask_wikiapi_ok_mk(self, MockGmMw, monkeypatch):
        """Test mediawiki return ok"""
        MockFirstPage = MagicMock(information.Information._ask_wiki_api_first_page)
        MockFirstPage.return_value = 'title'
        MockContent = MagicMock(information.Information._ask_wiki_api_content)
        MockContent.return_value = "La cité Paradis est une voie publique située dans le 10e arrondissement de Paris.\n\n\n== Situation et accès ==\nLa cité Paradis est une voie publique située dans le 10e arrondissement de Paris. Elle est en forme de té, une branche débouche au 43, rue de Paradis, la deuxième au 57, rue d'Hauteville et la troisième en impasse.\n\nVues de la cité\n\t\t\n\t\t\nCe site est desservi par les lignes \u2009\u200d\u2009\u200d à la station de métro Bonne-Nouvelle et par la ligne \u2009\u200d à la station Poissonnière.\n\n\n== Origine du nom ==\nElle porte ce nom en raison de sa proximité avec la rue éponyme.\n\n\n== Historique ==\nLa cité Paradis a été aménagée sur les anciens jardins de l'hôtel Titon dont la façade arrière est visible au fond de l'impasse.\nLa partie débouchant rue de Paradis a été ouverte en 1893 et celle débouchant rue d'Hauteville en 1906.\n\n\n== Références ==\n\n\n== Bibliographie ==\nJacques Hillairet, Dictionnaire historique des rues de Paris, Paris, Les Éditions de Minuit, 1972, 1985, 1991, 1997 , etc. (1re éd. 1960), 1 476 p., 2 vol.  [détail des éditions] (ISBN 2-7073-1054-9, OCLC 466966117, présentation en ligne).\n\n\n== Annexes ==\n\n\n=== Articles connexes ===\nListe des voies du 10e arrondissement de Paris\n\n\n=== Liens externes ===\nCité Paradis (mairie de Paris) Portail de Paris   Portail de la route"

        monkeypatch.setattr("papyrobot.utils.information.Information._ask_wiki_api_first_page", MockFirstPage)
        monkeypatch.setattr("papyrobot.utils.information.Information._ask_wiki_api_content", MockContent)

        infos = information.Information()
        key_words = "Citée Paradis"
        infos.ask_wiki_api(key_words)
        result = infos.story
        waited = "La cité Paradis est une voie publique située dans le 10e arrondissement de Paris. Elle est en forme de té, une branche débouche au 43, rue de Paradis, la deuxième au 57, rue d'Hauteville et la troisième en impasse."
        assert result == waited

    def test_ask_wikiapi_fail_mk(self, MockGmMw, monkeypatch):
        """Test mediawiki no result."""
        MockFirstPage = MagicMock(information.Information._ask_wiki_api_first_page)
        MockFirstPage.return_value = []

        monkeypatch.setattr("papyrobot.utils.information.Information._ask_wiki_api_first_page", MockFirstPage)

        infos = information.Information()
        key_words = "Citée Paradis"
        infos.ask_wiki_api(key_words)
        result = infos.story
        assert not result

    def test_ask_wiki_api_first_page_ok(self, MockGmMw, monkeypatch):
        """Test mediawiki does return a page name."""
        class MockReturn:
            def __init__(self, query, params):
                pass

            def json(self):
                results = {'query': {'search': [{'title': 'Cité Paradis'}]}}
                return results

        monkeypatch.setattr("papyrobot.utils.information.requests.get", MockReturn)

        infos = information.Information()
        keywords = "Citée Paradis Paris"
        result = infos._ask_wiki_api_first_page(keywords)
        waited = "Cité Paradis"
        assert result == waited

    def test_ask_wiki_api_first_page_fail(self, MockGmMw, monkeypatch):
        """Test mediawiki does not return a page name."""
        class MockReturn:
            def __init__(self, query, params):
                pass

            def json(self):
                results = {'query': {'search': []}}
                return results

        monkeypatch.setattr("papyrobot.utils.information.requests.get", MockReturn)

        infos = information.Information()
        keywords = "Homey Airport"
        result = infos._ask_wiki_api_first_page(keywords)
        assert not result

    def test_ask_wiki_api_content_ok(self, MockGmMw, monkeypatch):
        """Test mediawiki does return a page content."""
        class MockReturn:
            def __init__(self, query, params):
                pass

            def json(self):
                results = {'query': {'pages': {"1234":
                        {
                            "extract": "La cité Paradis est une voie publique située dans le 10e arrondissement de Paris.\n\n\n== Situation et accès ==\nLa cité Paradis est une voie publique située dans le 10e arrondissement de Paris. Elle est en forme de té, une branche débouche au 43, rue de Paradis, la deuxième au 57, rue d'Hauteville et la troisième en impasse.\n\nVues de la cité\n\t\t\n\t\t\nCe site est desservi par les lignes \u2009\u200d\u2009\u200d à la station de métro Bonne-Nouvelle et par la ligne \u2009\u200d à la station Poissonnière.\n\n\n== Origine du nom ==\nElle porte ce nom en raison de sa proximité avec la rue éponyme.\n\n\n== Historique ==\nLa cité Paradis a été aménagée sur les anciens jardins de l'hôtel Titon dont la façade arrière est visible au fond de l'impasse.\nLa partie débouchant rue de Paradis a été ouverte en 1893 et celle débouchant rue d'Hauteville en 1906.\n\n\n== Références ==\n\n\n== Bibliographie ==\nJacques Hillairet, Dictionnaire historique des rues de Paris, Paris, Les Éditions de Minuit, 1972, 1985, 1991, 1997 , etc. (1re éd. 1960), 1 476 p., 2 vol.  [détail des éditions] (ISBN 2-7073-1054-9, OCLC 466966117, présentation en ligne).\n\n\n== Annexes ==\n\n\n=== Articles connexes ===\nListe des voies du 10e arrondissement de Paris\n\n\n=== Liens externes ===\nCité Paradis (mairie de Paris) Portail de Paris   Portail de la route"
                        }
                    }}}
                return results

        monkeypatch.setattr("papyrobot.utils.information.requests.get", MockReturn)

        infos = information.Information()
        keywords = "Cité Paradis"
        result = infos._ask_wiki_api_content(keywords)
        waited = "La cité Paradis est une voie publique située dans le 10e arrondissement de Paris.\n\n\n== Situation et accès ==\nLa cité Paradis est une voie publique située dans le 10e arrondissement de Paris. Elle est en forme de té, une branche débouche au 43, rue de Paradis, la deuxième au 57, rue d'Hauteville et la troisième en impasse.\n\nVues de la cité\n\t\t\n\t\t\nCe site est desservi par les lignes \u2009\u200d\u2009\u200d à la station de métro Bonne-Nouvelle et par la ligne \u2009\u200d à la station Poissonnière.\n\n\n== Origine du nom ==\nElle porte ce nom en raison de sa proximité avec la rue éponyme.\n\n\n== Historique ==\nLa cité Paradis a été aménagée sur les anciens jardins de l'hôtel Titon dont la façade arrière est visible au fond de l'impasse.\nLa partie débouchant rue de Paradis a été ouverte en 1893 et celle débouchant rue d'Hauteville en 1906.\n\n\n== Références ==\n\n\n== Bibliographie ==\nJacques Hillairet, Dictionnaire historique des rues de Paris, Paris, Les Éditions de Minuit, 1972, 1985, 1991, 1997 , etc. (1re éd. 1960), 1 476 p., 2 vol.  [détail des éditions] (ISBN 2-7073-1054-9, OCLC 466966117, présentation en ligne).\n\n\n== Annexes ==\n\n\n=== Articles connexes ===\nListe des voies du 10e arrondissement de Paris\n\n\n=== Liens externes ===\nCité Paradis (mairie de Paris) Portail de Paris   Portail de la route"
        assert result == waited
