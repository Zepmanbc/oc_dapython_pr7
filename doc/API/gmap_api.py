#! /usr/bin/env python
import googlemaps
from key import gmapkey



gmaps = googlemaps.Client(key=gmapkey)

# Geocoding an address
geocode_result = gmaps.geocode('adresse openclassrooms')

# Look up an address with reverse geocoding
reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))



