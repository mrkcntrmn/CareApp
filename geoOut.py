'''
Created on Feb 15, 2017

@author: MARK
'''
import csv

with open('ChildCareCentersDataset.csv', 'r') as file:
    reader = csv.reader(file)
    centers_list = list(reader)

entry = centers_list[2923]

#print(entry)

#print(entry[2])
#print(entry[3])

from geopy.geocoders import Nominatim
geolocator = Nominatim()
location = geolocator.geocode(str(entry[3]))

#print"Address search returned:"
#print location.address
#print "Gps coordinates: Lat, Long"
lat = location.latitude
lon = location.longitude
#print lat, lon

entry.pop(21)
entry.pop(20)

entry.insert(20, lat)
entry.insert(21, lon)

#print(entry)

#center_list.pop(2923)
centers_list.insert(2923, entry)

#print centers_list[2923]

with open('ChildCareCentersEdited.csv', 'wb') as newFile:
    writer = csv.writer(newFile, delimiter=',', quoting=csv.QUOTE_ALL)
    writer.writerows(centers_list)

with open('ChildCareCentersEdited.csv', 'r') as testFile:
    newReader = csv.reader(testFile)
    test_list = list(newReader)



print(test_list[0])
print(test_list[2923])
