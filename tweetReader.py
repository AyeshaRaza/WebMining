import json
from pprint import pprint

data = []
with open("kanyeWest.txt","r".encoding="UTF-8") as jsonFile:
for line in jsonFile:
try:
data.append(json.loads(data))
except:
pass

pprint(data[0])

print(len(data))

#Ayesha: run python .\tweetReader.py to get total count of tweets

for i, tweet in enumerate(data):
print(tweet["text"])
print(tweet["user"]["id_str"])
print("-----")
if i == 100:
break
