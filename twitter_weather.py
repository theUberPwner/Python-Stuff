#Python: Weatherman Twitter Bot
###rudeweatherman@yahoo.com
###@DatWeather

#If a user tweets @DatWeather followed by a location, the bot
#will reply with the weather in that lcoation followed by a
#randomly chosen insult. The location can be in any format, 
#such as zip code, city and state, etc.

import tweepy
import time
import pywapi
import random

insults = ['idiot','moron','dumbass','loser']

#authenticate with twitter and return the api object
def twitter_auth(verify=False):
    consumer_key="S3o1mWFcDPXgwNBLQu64Hw"
    consumer_secret="VUceCzCSR0F2nrFdhAd4gRpdKuFJ9Qbe3j2ThXjc478"

    access_token="615596453-z4OwcGzoCk9QRxKt3ILODhMVBC2xY55HGS50VbOU"
    access_token_secret="xMZvKhanLwZZgJEFOR4XfWLRIUC9C8WwUGg3jg7rc"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    if verify:
        # Print the name of the account if successfull authentication
        print api.me().name,"Authenticated!"

    return api

#use google to get the weather for the given location
def get_weather(loc_id):
    try:
        weather = pywapi.get_weather_from_google(loc_id)
    except Exception as e:
        print e
        return "error"

    if len(weather["current_conditions"]) == 0:
        return "invalid loc_id"

    return weather

#same as get_weather but for my local zip code
###not used yet
def get_local_weather():
    return pywapi.get_weather_from_google('21043')

#contruct the reply tweet with the given weather information
def construct_tweet(weather):
    city = weather["forecast_information"]["city"]
    condition = weather["current_conditions"]["condition"]
    temp_f = weather["current_conditions"]["temp_f"]
    temp_c = weather["current_conditions"]["temp_c"]
    humidity = weather["current_conditions"]["humidity"].replace("Humidity: ","")
    wind = weather["current_conditions"]["wind_condition"].replace("Wind: ","")

    tweet = "It is currently " + temp_f + " degrees F (" + temp_c + " C) " +\
            "and " + condition + " in " + city + ' '

    #add custom stuff here
    r = random.randint(0,len(insults)-1)
    tweet += insults[r]

    return tweet

#send the weather tweet to the user that tweeted the location
def send_tweet(message,mention,tries=3):
    message = "@" + str(mention.user.screen_name) + " " + message
    index=tries
    while 1:
        try:
            api.update_status(message,in_reply_to_status_id=mention.id)
            print "Tweeted: " + message
            break
        except Exception as e:
            print e
            if index == 3:
                print "Timed Out. Tweet from @" + mention.user.screen_name + " was not replied to"
                break
            print "Tweet reply failed. " + str(index) + "/3"
            index += 1
        time.sleep(1)#wait for 1 second between tries



if __name__ == '__main__':
    random.seed()

    api = twitter_auth(verify=True) #authenticate with twitter

    #initialize some variables
    mentions = api.mentions()
    since_id = mentions[0].id

    ###MAIN LOOP##
    while 1:
        while 1:
            try:
                mentions = api.mentions(since_id)
                break
            except Exception as e:
                time.sleep(1)
                continue
  
        for mention in mentions:
            print mention.text
            tweet = mention.text
            loc_id = tweet.replace("@DatWeather ","")

            weather = get_weather(loc_id)
            if weather == 'error':
                print 'an error has occured!'
                send_tweet("You broke something. SHIT!",mention)
            elif weather == 'invalid loc_id':
                print 'invalid location ID'
                send_tweet("Enter a valid location you idiot",mention)
            else:
            	new_tweet = construct_tweet(weather,mention)

            	send_tweet(new_tweet,mention)

            since_id = mention.id_str
            time.sleep(1)#wait a second between mentions

        time.sleep(10)

