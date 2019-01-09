import tweepy
import json

# API Information: replace values with your own
consumer_key = "XXXXXXXXX"
consumer_secret = "XXXXXXX"
access_key = "XXXXX"
access_secret = "XXXXXX"

# Authorization for consumer key and consumer secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

# Access to user's access key and access secret
auth.set_access_token(access_key, access_secret)
# Call api
api = tweepy.API(auth)

# Empty Array
tmp = []

# Function to extract tweets
def get_tweets(username):

    # 200 tweets to be extracted
    number_of_tweets = 200
    tweets = api.user_timeline(screen_name=username, count=number_of_tweets)


    #Get the first 200 tweets: So we can use the last tweet ID to get even older tweets.
    for j in tweets:
        # Appending tweets to the empty array tmp
        tmp.append(j)
        print(j)
        print("-------------------------------")

    # Get older Tweet
    grab_old_tweets(tmp[-1].id - 1,username)

def grab_old_tweets(oldest,username):
    flag = True
    # keep grabbing tweets until there are no tweets left to grab
    while flag:
        print ("getting tweets before %s" % (oldest))

        #The max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name=username, count=200, max_id=oldest)

        # save most recent tweets
        for tweet in new_tweets:
            tmp.append(tweet)

        # update the id of the oldest tweet less one
        oldest = tmp[-1].id - 1

        print ("...%s tweets downloaded so far" % (len(tmp)))
        if len(new_tweets) < 200:
            flag = False
    count= 0
    for tweet in tmp:
        print("#######################################")
        print(count)
        print(tweet.id_str)
        print(tweet.created_at)
        print(tweet.text.encode("utf-8"))
        count=count+1



# Start
if __name__ == '__main__':
    # twitter handle whose tweets are to be extracted.
    get_tweets("@markets")