#!/usr/bin/python
import csv , json
import pandas as pd 

csvFilePath = "../data/generated_tweets_.csv"
jsonFilePath = "../data/markov_script_data.json"
data = []
#read the csv and add the arr to a arrayn

with open (csvFilePath) as csvFile:
    csvReader = csv.DictReader(csvFile)
    print(csvReader)
    for csvRow in csvReader:
        data.append(csvRow)


# print(data[0:2])

df=pd.DataFrame(data)
print(df)
df.to_json(jsonFilePath, indent=2, )
