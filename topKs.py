from methods import topHashtags, topMentions, topInfluents, say_hello
import json
import sys

if __name__ == '__main__':
    say_hello()
    sys.exit()
    fname = 'filename.jsonl'
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
    print(top_inflents)
