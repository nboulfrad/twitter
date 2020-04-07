# List all your methods
import operator 
import collections


def topMentions(tweets, k):
    

    ordre =[]
    for line in tweets :
        for men in line["entities"]["user_mentions"]:
            ordre.append(men["name"])

    counter = collections.Counter(ordre)
    ment = dict(sorted(counter.iteritems(), key=operator.itemgetter(1), reverse=True)[:k])
    ordred = sorted(ment.items(), key=lambda t: t[1], reverse=True)
    return ordred


def topInfluents (tweets, k): 
    
    ordre =[]
    ordre1 ={}
    ordre2 = {}

    for line in tweets :
        for men in line["entities"]["user_mentions"] :
            ordre.append(men["name"])
        ordre1[line["user"]["name"]] = line["user"]["followers_count"]
        ordre2[line["user"]["name"]] = line["retweet_count"]
    
    counter = collections.Counter(ordre)
    ment = dict(sorted(counter.iteritems(), key=operator.itemgetter(1), reverse=True)[:k])
    menord = sorted(ment.items(), key=lambda t: t[1], reverse=True)
    folord = sorted(ordre1.items(), key=lambda t: t[1], reverse=True)[:k]
    # folord = sorted(ordre1.items(), key=lambda t: t[1])[len(ordre1)-300:len(ordre1)]
    retord = sorted(ordre2.items(), key=lambda t: t[1], reverse=True)[:k]

    # [(usen_name, count), (user_name, count)]

    fkeys = [xy[0] for xy in folord]
    mkeys = [xy[0] for xy in menord]
    rkeys = [xy[0] for xy in retord]

    inf = []
    for username in fkeys:
        if username in mkeys and username in rkeys:
            inf.append(username)
   
    return inf

def topHashtags(tweets, k):

    hashtags = []
    for o in tweets:
        for hasht in o["entities"]["hashtags"]:
            hashtags.append(hasht['text'])

    ordre =[]
    hasht = {}
    counter = collections.Counter(hashtags)
    hasht = dict(sorted(counter.iteritems(), key=operator.itemgetter(1),reverse=True)[:k])
    ordre = sorted(hasht.items(), key=lambda t: t[1], reverse=True)
    return ordre



