import json

fp=open("tv.json","r")
mydict=json.load(fp)

items = mydict["Deep Learning"]
for item in items:
	print(f"https://www.youtube.com/watch?v={item}")