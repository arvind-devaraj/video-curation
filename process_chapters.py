import os,sys

import subprocess


fp=open("data/vids.txt")
lines=fp.read().splitlines()
for line in lines:
	print(line)
	vid = line.strip()
	cmd=(f"youtube-dl --dump-json {vid}  | jq --raw-output \".chapters[].title\"")
	output = subprocess.getoutput(cmd)
	if(output.startswith("jq: error")):
		continue
	print("OUT="+output)
	fp=open(f"data-vid/{vid}","w")
	fp.write(output)
	fp.close()
	
	
