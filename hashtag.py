import operator 
import json
import collections


def top_hashtag(fname, k):
    with open(fname, 'r') as handle:
        json_data = [json.loads(line) for line in handle]

    hashtags = []
    for o in json_data:
        for hasht in o["entities"]["hashtags"]:
            for dic in hasht:
                hashtags.append(dic['text'])


    #hashtags = []
    #for dic in ordre:
    #    hashtags.append(dic["text"])

    counter = collections.Counter(hashtags)
    hasht = dict(sorted(counter.iteritems(), key=operator.itemgetter(1),
        reverse=True)[:k]
    print sorted(hasht.items(), key=lambda t: t[1], reverse=True)

