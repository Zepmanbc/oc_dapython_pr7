#! /usr/bin/env python
import os

import googlemaps
import mediawiki
from mediawiki import MediaWiki


class Information():

    def __init__(self):
        self.wikipedia = MediaWiki()
        self.wikipedia.language = "fr"

        self.gmaps = googlemaps.Client(key=os.environ['GMAPKEY'])
        
        self.formatted_address = str()
        self.location = tuple()
        self.street_city = str()
        self.story = str()

    def ask_gmap(self, query):
        geocode_result = self.gmaps.geocode('adresse ' + str(query))
        if not geocode_result:
            return False
        self.formatted_address = geocode_result[0]['formatted_address']
        self.location = (
            geocode_result[0]['geometry']['location']['lat'],
            geocode_result[0]['geometry']['location']['lng']
            )
        self.street_city = " ".join([
            self._extract_street(geocode_result[0]['address_components']), 
            self._extract_city(geocode_result[0]['address_components'])
            ])
        return True

    @staticmethod
    def _extract_street(address_components):
        for component in address_components:
            if 'route' in component['types'] or 'establishment' in component['types']:
                return component['long_name']

    @staticmethod
    def _extract_city(address_components):
        for component in address_components:
            if 'locality' in component['types']:
                return component['long_name']


    def ask_wiki(self, query):
        search = self.wikipedia.search(query)
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
            # content = content.split("\n")[0]
        else:
            content = content.split("==")[0].replace("\n", "")
        self.story = content
        return True

if __name__ == "__main__":
    import os
    from question import Question
    os.system('clear')
    question = Question()
    # query = "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?"
    # query = "où se trouve l'Arc de Triomphe?"
    # query = "Quelle est l'adresse de la Tour Eiffel?"
    # query = "Dis Papy, c'est quoi l'adresse de l'Elysée?"
    query = "Tu connais l'adresse de l'Opéra Garnier?"

    # keyword_gmap = question.analyze(query)
    # # keyword_gmap = "toto"
    info = Information()
    # if info.ask_gmap(keyword_gmap):
    #     print(info.formatted_address)
    #     print(info.location)
    #     print(info.street_city)
    # else:
    #     print("pas clair")

    # info.street_city = 'Cité Paradis Paris'
    info.street_city = 'Place Charles de Gaulle Paris'
    # info.street_city = 'Champ de Mars Paris'
    # info.street_city = 'Rue du Faubourg Saint-Honoré Paris'
    # info.street_city = 'Rue Scribe Paris'
    # info.street_city = 'Cité Par'
    info.ask_wiki(info.street_city)
    print(info.story)