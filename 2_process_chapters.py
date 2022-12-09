import os,sys

import subprocess

import redis

red5 = redis.Redis(host='localhost', port=6379, db=5,encoding='utf-8',decode_responses=True)


fp=open("data/vids.txt")
lines=fp.read().splitlines()
for line in lines[:500]:
	print(line)
	vid = line.strip()
	if(red5.get(vid) is not None):
		continue
	cmd=(f"youtube-dl --dump-json {vid}  | jq --raw-output \".chapters[].title\"")
	output = subprocess.getoutput(cmd)
	if(output.startswith("jq: error")):
		continue
	print("OUT="+output)

	red5.set(vid,output)
	
	
