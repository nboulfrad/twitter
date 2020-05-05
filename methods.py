# List all your methods
import operator 
import collections


def topMentions(tweets, k):
    mentions =[]
    for line in tweets :
        for men in line["entities"]["user_mentions"]:
            mentions.append(men["name"])

    counter = collections.Counter(mentions)
    #ment = dict(sorted(counter.iteritems(), key=operator.itemgetter(1), reverse=True)[:k])
    #mentionsd = sorted(ment.items(), key=lambda t: t[1], reverse=True)
    #return mentionsd
    return counter.most_common(k)


def topInfluents (tweets, k): 
    
    mentions = []
    user_followers = {}
    user_retweets = {}

    for line in tweets :
        for men in line["entities"]["user_mentions"] :
            mentions.append(men["name"])
        user_followers[line["user"]["name"]] = line["user"]["followers_count"]
        user_retweets[line["user"]["name"]] = line["retweet_count"]
    
    counter = collections.Counter(mentions)
    #ment = dict(sorted(counter.iteritems(), key=operator.itemgetter(1), reverse=True)[:k])
    #menord = sorted(ment.items(), key=lambda t: t[1], reverse=True)
    menrord = counter.most_common(k)
    folord = sorted(user_followers.items(), key=lambda t: t[1], reverse=True)[:k]
    # folord = sorted(user_followers.items(), key=lambda t: t[1])[len(user_followers)-300:len(user_followers)]
    retord = sorted(user_retweets.items(), key=lambda t: t[1], reverse=True)[:k]

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

    mentions =[]
    hasht = {}
    counter = collections.Counter(hashtags)
    hasht = dict(sorted(counter.iteritems(), key=operator.itemgetter(1),reverse=True)[:k])
    mentions = sorted(hasht.items(), key=lambda t: t[1], reverse=True)
    return mentions



