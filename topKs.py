from methods import topHashtags, topMentions, topInfluents
import json


if __name__ == '__main__':
    fname = 'dz_20190507.jsonl'
    tweets = []
    with open(fname) as f:
        for line in f:
            tweets.append(json.loads(line))
    K = 10
    top_hashtags = topHashtags(tweets, K)
    top_mentions = topMentions(tweets, K)
    top_influents = topInfluents(tweets, K)
    # print results
    print(top_hashtags)
    print(top_mentions)
    print(top_influents)
