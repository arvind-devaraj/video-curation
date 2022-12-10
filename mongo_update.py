import json
from pymongo import MongoClient


client = MongoClient('bookgist.in', 27017)
db = client.textgen
collection = db.group_vids




def write_mongo(record):
    try:
            result = collection.insert_one(record)
            print('written: {0}'.format(result.inserted_id))
    except Exception as e:
            print(e)
            #print('ignored:' +record["_id"])

 


fp = open("tv.json")
mydict = json.load(fp)
print(mydict)

fp = open("mapping.json")
mapping = json.load(fp)

for k,v in mydict.items():
	cat=mapping.get(k,"")
	tag=k
	
	record={"category":cat,"tag":tag,"vids":v}
	write_mongo(record)

