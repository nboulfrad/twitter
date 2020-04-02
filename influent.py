import operator 
import json
import collections
with open('file1000', 'r') as handle:
    json_data = [json.loads(line) for line in handle]

ordre =[]
ordre1 ={}
ordre2 = {}
for line in json_data :
  for men in line["entities"]["user_mentions"] :
    ordre.append(men["name"])
  ordre1[line["user"]["name"]] = line["user"]["followers_count"]
  ordre2[line["user"]["name"]] = line["retweet_count"]
counter=collections.Counter(ordre)
ment = dict(sorted(counter.iteritems(), key=operator.itemgetter(1), reverse=True)[:300])
menord = sorted(ment.items(), key=lambda t: t[1], reverse=True)
folord = sorted(ordre1.items(), key=lambda t: t[1])[len(ordre1)-300:len(ordre1)]
retord = sorted(ordre2.items(), key=lambda t: t[1])[len(ordre1)-300:len(ordre1)]

inf= []
for x, y in folord:
 for xx, y in menord:
  for xxx, y in retord:
   if (x == xx) and (xx == xxx):
    inf.append(x)
for x in inf:
 print x
