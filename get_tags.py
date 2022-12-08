import redis
red6 = redis.Redis(host='localhost', port=6379, db=6,encoding='utf-8',decode_responses=True)

result=[]
def process(file_name):
    print(file_name)
    vid=file_name
    tags=red6.smembers(file_name)
    print(tags)
    tags=list(tags)
    tags=tags[:3]
    all_tags=",".join(tags)
    item={}
    item["vid"]=vid
    item["tags"]=all_tags
    result.append(item)




import glob,os,json
os.chdir("data-vid")
for f in glob.glob('*'):
    process(f)

fp=open("out.json","w")
json.dump(result,fp,indent=4)
fp.close()
