'''
Created on Feb 15, 2017

@author: MARK
'''
import csv
with open('ChildCareCenters.csv', 'r') as f:
    reader = csv.reader(f)
    your_list = list(reader)

entry = your_list[2923]

print(entry[2])
print(entry[3])

from geopy.geocoders import Nominatim
geolocator = Nominatim()
location = geolocator.geocode(str(entry[3]))

print"Address search returned:" 
print location.address
print "Gps coordinates: Lat, Long"
print location.latitude, location.longitude