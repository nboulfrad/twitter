
 
import operator 
import json
def top_user(x,i):
 with open(x, 'r') as handle:
    json_data = [json.loads(line) for line in handle]
 print (len(json_data))

 ordre ={}
 for line in json_data :
  if line["user"]["name"] not in ordre.keys() :
   ordre[line["user"]["name"]] = 1
  else : ordre[line["user"]["name"]] += 1

 mostuse = dict(sorted(ordre.iteritems(), key=operator.itemgetter(1), reverse=True)[:i])
 print sorted(mostuse.items(), key=lambda t: t[1], reverse=True)

