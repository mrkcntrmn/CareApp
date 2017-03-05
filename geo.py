from geopy.geocoders import Nominatim
geolocator = Nominatim()
location = geolocator.geocode("2051 W PARKWOOD AVE FRIENDSWOOD")
print(location.address)
print((location.latitude, location.longitude))
