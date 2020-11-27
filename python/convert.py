#!/usr/bin/python
import csv , json
import pandas as pd 

# convert real tweets
# csvFilePath = "../data/trump_tweets.csv"
# jsonFilePath = "../data/real_tweets.json"

# convert script generated tweets
# csvFilePath = "../data/generated_tweets_.csv"
# jsonFilePath = "../data/markov_script_data.json"

#  convert package generated tweets
csvFilePath = "../data/makovify_package_generated_tweets.csv"
jsonFilePath = "../data/makovify_package_generated_tweets.json"


data = []
#read the csv and add the arr to a arrayn





with open (csvFilePath) as csvFile:
    # csvReader = csv.DictReader(csvFile)
    # print(csvReader)
    for csvRow in csvFile:
        data.append(csvRow)
# print(data)


json_list=[]
for tweet in data:
    new_dict={
        "tweet" : tweet,
    }
    json_list.append(new_dict)
print(json_list)  



# df=pd.DataFrame(json_list)
# print(df.head())
# print(json.dumps(json_list))

with open(jsonFilePath, "w") as jsonFile:
    jsonFile.write(json.dumps(json_list, indent = 2))

