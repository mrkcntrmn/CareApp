'''
Created on Feb 15, 2017

@author: MARK
'''
import csv




with open('ChildCareCentersDataset.csv', 'r') as file:
    reader = csv.reader(file)
    centers_list = list(reader)
    num_rows = len(centers_list)

new_centers_list = []

new_centers_list.append(centers_list[0])
#print new_centers_list[0]

for x in range(9000, num_rows): #num_rows
    #print x

    currentEntry = centers_list[x]

    #print(currentEntry)

#    print(currentEntry[3])
#    print(currentEntry[3])
#    print(currentEntry[4])

    from geopy.geocoders import Nominatim
    geolocator = Nominatim()
    location = geolocator.geocode(  str(currentEntry[3]),exactly_one=True, timeout=999 )

    #print"Address search returned:"


    '''


    print "Gps coordinates: Lat, Long"
    '''



    if location is None:
        lat = 0
        lon = 0
        #print "No Address"
    else:
        lat = location.latitude
        lon = location.longitude
        #print location.address

    #print lat, lon

    currentEntry.pop(21)
    currentEntry.pop(20)



    currentEntry.insert(20, lat)
    currentEntry.insert(21, lon)
    #print(currentEntry)

    #centers_list.pop(x)
    new_centers_list.insert(x, currentEntry)
    #print new_centers_list[x]


    with open('ChildCareCentersEdited.csv', 'wb') as newFile:
        writer = csv.writer(newFile, delimiter=',', quoting=csv.QUOTE_ALL)
        writer.writerows(new_centers_list)

    print "" + str(x) + " " + str(lat) + " " +str(lon)



'''
with open('ChildCareCentersEdited.csv', 'r') as testFile:
    newReader = csv.reader(testFile)
    test_list = list(newReader)




print(test_list[0])
print(test_list[2923])
'''
