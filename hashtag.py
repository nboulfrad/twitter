import operator 
import json
import collections
def top_hashtag(x,i):
 with open(x, 'r') as handle:
    json_data = [json.loads(line) for line in handle]

 ordre =[]
 for line in json_data :
   for hasht in line["entities"]["hashtags"] :
     ordre.append(hasht)


 hashtags=[]
 for dic in ordre:
   hashtags.append(dic["text"])
 counter=collections.Counter(hashtags)

 hasht = dict(sorted(counter.iteritems(), key=operator.itemgetter(1), reverse=True)[:i])
 print sorted(hasht.items(), key=lambda t: t[1], reverse=True)

