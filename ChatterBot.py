# Dependencies
import tweepy
import json
import time

# Twitter API Keys
consumer_key = "F8i2hd0l7wEMHwoRf328sGvJB"
consumer_secret = "yAOp0FsCNRNEKomJzb0mMLRGo2GWelQUK3O2wgM8tfNCZFTlSQ"
access_token = "97576524-DgEMdCI8GQ5QI9n8KR18NyPtZmgmxW5AWvwpCdqzj"
access_token_secret = "vu95B5DwWAnbZJMoWbh0RmpggElK2wV0Kin9EM9DTkqKN"

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())


# Create a function that tweets
# CODE GOES HERE