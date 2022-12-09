from collections import defaultdict
import redis
red6 = redis.Redis(host='localhost', port=6379, db=6,encoding='utf-8',decode_responses=True)

result=defaultdict(list)
def process(vid):
    tags=red6.smembers(vid)
    print(tags)
    tags=list(tags)
    
    
    for tag in tags:

        result[tag].append(vid)
        



import glob,os,json


fp=open("data/vids.txt")
lines = fp.read().splitlines()
for line in lines[:500]:
    vid=line.strip()
    process(vid)



fp=open("tv.json","w")
json.dump(result,fp,indent=4)
fp.close()
