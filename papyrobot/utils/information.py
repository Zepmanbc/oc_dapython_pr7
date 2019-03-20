#! /usr/bin/env python
"""Information Class"""
import os
import requests

import googlemaps
import mediawiki


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
        info.ask_wiki(keyword_gmap)     # if street_city does not return result
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
        self.wikipedia = mediawiki.MediaWiki()
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
        if not geocode_result or query == '':
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
                result = self.wikipedia.page(search[0]).content
            except KeyError:
                return False
            except mediawiki.exceptions.DisambiguationError:
                return False
            self._wiki_story_extract(result)
            return True
        return False

    def ask_wiki_api(self, keyword):
        """Ask Wikipedia API.

        Args:
            query (str): usualy city_street string
                         can be keywords

        Return:
            False if there is no API return
            True if there is an API return
            story (str) is filled
        """
        page_title = self._ask_wiki_api_first_page(keyword)
        if page_title:
            page_content = self._ask_wiki_api_content(page_title)
            self._wiki_story_extract(page_content)
            return True
        return False

    def _ask_wiki_api_first_page(self, keyword):
        """Ask for list a pages and return the first.

        Args:
            keyword (str): usualy city_street string
                         can be keywords
        Returns:
            page_title (str)
            False: if no result
        """
        query = "https://fr.wikipedia.org/w/api.php?action=query&list=search" \
            "&utf8&format=json&srsearch={}".format(keyword)
        query_pages = requests.get(query)
        query_pages = query_pages.json()
        if query_pages["query"]["search"]:
            page_title = query_pages["query"]["search"][0]["title"]
            return page_title
        return False

    def _ask_wiki_api_content(self, page_title):
        """Ask for content of wiki page.

        Args:
            page_title (str)
        Returns:
            page_content (str)
        """
        query = "https://fr.wikipedia.org/w/api.php?" \
            "action=query&format=json&utf8" \
            "&explaintext&prop=extracts&exlimit=1&titles={}".format(page_title)
        query_page = requests.get(query).json()
        page_nbr = next(iter(query_page["query"]["pages"]))
        page_content = query_page["query"]["pages"][page_nbr]["extract"]
        return page_content

    # def ask_wiki_gps(self):
    #     # geosearch
    #     (lng, lat) = self.location
    #     query = "https://en.wikipedia.org/w/api.php?action=query" \
    #         "&list=geosearch&gsradius=10000&gslimit=1" \
    #         "&format=json&gscoord={}|{}".format(lng, lat)
    #     query_pages = requests.get(query)
    #     page_title = query_pages.json()["query"]["geosearch"][0]["title"]
    #     # get wiki page content
    #     query = "https://fr.wikipedia.org/w/api.php?action=query" \
    #         "&format=json&utf8&explaintext&prop=extracts" \
    #         "&exlimit=1&titles={}".format(page_title)
    #     query_page = requests.get(query)
    #     page_nbr = next(iter(query_page.json()["query"]["pages"]))
    #     page_content = query_page.json()["query"]["pages"][page_nbr]["extract"]
    #     # Extract Story and fill self.story
    #     self._wiki_story_extract(page_content)

    def _wiki_story_extract(self, content):
        """Extract the story from wiki content.

            Extract the == Situation et accès == part
            if it does not exist, extract the first sentence

            Args:
                content (str): the text from wiki page
            Return:
                self.story filled
        """
        if "== Situation et accès ==" in content:
            content = content.split("== Situation et accès ==")[1]
            content = [x for x in content.split('\n') if x != ''][0]
        else:
            content = content.split("==")[0].replace("\n", "")
        self.story = content


if __name__ == "__main__":
    # import os
    # from question import Question
    # os.system('clear')
    # question = Question()
    # query = "Salut GrandPy ! Est-ce que tu connais l'adresse" \
    #     " d'OpenClassrooms ?"
    # query = "où se trouve l'Arc de Triomphe?"
    # query = "Quelle est l'adresse de la Tour Eiffel?"
    # query = "Dis Papy, c'est quoi l'adresse de l'Elysée?"
    # query = "Tu connais l'adresse de l'Opéra Garnier?"
    # query = "zone 51"
    # keyword_gmap = question.analyze(query)
    # keyword_gmap = "tour pise"
    # keyword_gmap = "soirée Madame Pahud hier soir indiquer musée art histoire Fribourg plaît"
    # info = Information()
    # if info.ask_gmap(keyword_gmap):
    #     print(info.formatted_address)
    #     print(info.location)
    #     print(info.street_city)
    # else:
    #     print("pas clair")

    # info.street_city = 'Cité Paradis Paris'
    # info.street_city = 'Place Charles de Gaulle Paris'
    # # info.street_city = 'Champ de Mars Paris'
    # # info.street_city = 'Rue du Faubourg Saint-Honoré Paris'
    # # info.street_city = 'Rue Scribe Paris'
    # info.street_city = 'Cité Par'
    # if not info.ask_wiki(info.street_city):
    #     info.ask_wiki(keyword_gmap)
    # print(info.story)

    # info.street_city = 'Cité Paradis Paris'  # OK
    # info.street_city = 'Homey Airport'  # no result
    # info.street_city = 'Cité par'  # raise error

    # info.ask_wiki_api(info.street_city)
    # print(info.story)

    pass
