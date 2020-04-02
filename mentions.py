import operator 
import json
import collections
with open('file1000', 'r') as handle:
    json_data = [json.loads(line) for line in handle]

ordre =[]
for line in json_data :
  for men in line["entities"]["user_mentions"] :
    ordre.append(men["name"])
counter=collections.Counter(ordre)
ment = dict(sorted(counter.iteritems(), key=operator.itemgetter(1), reverse=True)[:5])
ordred = sorted(ment.items(), key=lambda t: t[1], reverse=True)
for i in ordred :
  print (i)


