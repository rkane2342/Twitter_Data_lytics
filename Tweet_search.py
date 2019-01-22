
#for6-10 days old
from TwitterSearch import *
import Credentials
try:
    tso = TwitterSearchOrder() # create a TwitterSearchOrder object
    tso.set_keywords(['tesla']) # let's define all words we would like to have a look for
    #tso.set_language('de') # we want to see German tweets only
    tso.set_include_entities(False) # and don't give us all those entity information

    # it's about time to create a TwitterSearch object with our secret tokens
    ts = TwitterSearch(
        consumer_key = Credentials.consumer_key,
        consumer_secret = Credentials.consumer_secret,
        access_token = Credentials.access_key,
        access_token_secret = Credentials.access_secret
     )

     # this is where the fun actually starts :)
    for tweet in ts.search_tweets_iterable(tso):
        print( '@%s tweeted: %s: @%s' % ( tweet['user']['screen_name'], tweet['text'] ,tweet['created_at']) )
        print('-----------------------------------/n')

except TwitterSearchException as e: # take care of all those ugly errors if there are some
    print(e)