import yaml


in_dict={}
out_dict={}

with open('data/tags.yaml', 'r') as file:
   in_dict = yaml.safe_load(file)

print(in_dict)

for k,v in in_dict.items():
	print(k)
	for item in v:
		out_dict[item]=k


import json
print(out_dict)
json.dump(out_dict,open("mapping.json","w"))