#! /usr/bin/env python
import os
import googlemaps

gmaps = googlemaps.Client(key=os.environ['GMAPKEY'])

# Geocoding an address
geocode_result = gmaps.geocode('adresse openclassrooms')

# Look up an address with reverse geocoding
reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))



