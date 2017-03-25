import csv
import json
import geojson

from geojson import Feature, Point, FeatureCollection



with open('ChildCareCentersGPS.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    centers_list = list(reader)
    num_rows = len(centers_list)

    
features = []


for x in range(1, num_rows): 
    #print x

    current_entry = centers_list[x]
    current_feature = Feature(geometry=Point((float(current_entry[20]), float(current_entry[21]))), properties={"Operation #": str(current_entry[0]), "Agency Number":  str(current_entry[1]), "Operation/Caregiver Name": str(current_entry[2]), "Address": str(current_entry[3]), "City": str(current_entry[4]), "State": str(current_entry[5]), "Zip": str(current_entry[6]), "County": str(current_entry[7]), "Phone": str(current_entry[8]), "Type": str(current_entry[9]), "Status": str(current_entry[10]), "Issue Date": str(current_entry[11]), "Capacity": str(current_entry[12]), "Email Address": str(current_entry[13]), "Facility ID": str(current_entry[14]), "Monitoring Frequency": str(current_entry[15]), "Infant": str(current_entry[16]), "Toddler": str(current_entry[17]), "Preschool": str(current_entry[18]), "School": str(current_entry[19])})
    
    features.append(current_feature)

data = json.loads(geojson.dumps(FeatureCollection(features)))

with open('data.json', 'w') as outfile:
    json.dump(data, outfile, sort_keys = False, indent = 4, ensure_ascii = False, separators=(',', ':'))



#print geojson.dumps(FeatureCollection(features))

