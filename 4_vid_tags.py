import redis
red6 = redis.Redis(host='localhost', port=6379, db=6,encoding='utf-8',decode_responses=True)

result=[]
def process(vid):
    tags=red6.smembers(vid)
    print(tags)
    tags=list(tags)
    tags=tags[:3]
    all_tags=",".join(tags)
    item={}
    item["vid"]=vid
    item["tags"]=all_tags
    result.append(item)




import glob,os,json


fp=open("data/vids.txt")
lines = fp.read().splitlines()
for line in lines[:500]:
    vid=line.strip()
    process(vid)



fp=open("out.json","w")
json.dump(result,fp,indent=4)
fp.close()
