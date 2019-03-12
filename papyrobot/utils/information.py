#! /usr/bin/env python
"""Information Class"""
import os

import googlemaps
import mediawiki
from mediawiki import MediaWiki


class Information():
    """Information class

    search on Gmap API et Wikipedia API

    info = Information()
    keyword_gmap = "OpenClassrooms"
    if info.ask_gmap(keyword_gmap):
        print(info.formatted_address)   # 7 Cité Paradis, 75010 Paris, France
        print(info.location)            # (48.8747265, 2.3505517)
        print(info.street_city)         # Cité Paradis Paris
    if not info.ask_wiki(info.street_city):
        info.ask_wiki(keyword_gmap)     # if street_city does not return a result
                                        # it's possible to try with key words
    print(info.story)                   # return string from wikipedia

    """
    def __init__(self):
        """Init Information class

        create Wikipedia object and set it to French
        create Google Map object
        GMAPKEY_BACK must be set in variable environment

        init variables:
            formatted_address (str)
            location (tuple): ( latitude (float), longitude (float) )
            street_city (str)
            story (str)

        """
        self.wikipedia = MediaWiki()
        self.wikipedia.language = "fr"

        self.gmaps = googlemaps.Client(key=os.environ['GMAPKEY_BACK'])

        self.formatted_address = str()
        self.location = tuple()
        self.street_city = str()
        self.story = str()

    def ask_gmap(self, query):
        """Ask Google Map API.

        Args:
            query(str): key words, "adresse " is added to help the search

        Return:
            False if no result
            True if the API return something and variables had been filled

                formatted_adress (str): full adress
                location (tuple): (longitude, latitude)
                street_city (str): street + " " + city
        """
        geocode_result = self.gmaps.geocode('adresse ' + str(query))
        if not geocode_result:
            return False
        self.formatted_address = geocode_result[0]['formatted_address']
        self.location = (
            geocode_result[0]['geometry']['location']['lat'],
            geocode_result[0]['geometry']['location']['lng']
            )

        # print(self._extract_city(geocode_result[0]['address_components']))
        # print(geocode_result)

        self.street_city = " ".join([
            self._extract_street(geocode_result[0]['address_components']),
            self._extract_city(geocode_result[0]['address_components'])
            ]).strip()
        return True

    @staticmethod
    def _extract_street(address_components):
        """Extracts street name."""
        for component in address_components:
            if 'route' in component['types'] or 'establishment' in component['types']:
                return component['long_name']
        return ''

    @staticmethod
    def _extract_city(address_components):
        """Extracts city name."""
        for component in address_components:
            if 'locality' in component['types']:
                return component['long_name']
        return ''


    def ask_wiki(self, query):
        """Ask Wikipedia API.

        first search return a list of pages
        second search with the first result of previous page

        filter on second result to get localisation text informations

        Args:
            query (str): usualy city_street string
                         can be keywords

        Return:
            False if there is no API return
            True if there is an API return
            story (str) is filled
        """
        search = self.wikipedia.search(query)
        if search:
            try:
                result = self.wikipedia.page(search[0])
            except mediawiki.exceptions.DisambiguationError:
                return False
            content = result.content
            if "== Situation et accès ==" in content:
                content = content.split("== Situation et accès ==")[1]
                for text in content.split('\n'):
                    if text:
                        content = text
                        break
            else:
                content = content.split("==")[0].replace("\n", "")
            self.story = content
            return True
        return False

if __name__ == "__main__":
    # import os
    # from question import Question
    # os.system('clear')
    # question = Question()
    # query = "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?"
    # # query = "où se trouve l'Arc de Triomphe?"
    # # query = "Quelle est l'adresse de la Tour Eiffel?"
    # # query = "Dis Papy, c'est quoi l'adresse de l'Elysée?"
    # # query = "Tu connais l'adresse de l'Opéra Garnier?"
    # query = "zone 51"
    # keyword_gmap = question.analyze(query)
    # keyword_gmap = "tour pise"
    # info = Information()
    # if info.ask_gmap(keyword_gmap):
    #     print(info.formatted_address)
    #     print(info.location)
    #     print(info.street_city)
    # else:
    #     print("pas clair")

    # # info.street_city = 'Cité Paradis Paris'
    # # info.street_city = 'Place Charles de Gaulle Paris'
    # # info.street_city = 'Champ de Mars Paris'
    # # info.street_city = 'Rue du Faubourg Saint-Honoré Paris'
    # # info.street_city = 'Rue Scribe Paris'
    # info.street_city = 'Cité Par'
    # if not info.ask_wiki(info.street_city):
    #     info.ask_wiki(keyword_gmap)
    # print(info.story)
    pass
