import csv
import json

file = open("Frequent_Flier_Cleansed.csv", 'r')
reader = csv.reader(file)

fieldNames = next(reader)
#print (fieldNames)

data = []

for row in reader:
    data.append(dict(zip(fieldNames, row)))

#print(data)

#call the json method
json_data = json.dumps(data)

#open the file and write to it
json_file = open("db.json", 'w')
json_file.write(json_data)

#close both files
file.close()
json_file.close()

