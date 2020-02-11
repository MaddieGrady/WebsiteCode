import json

#open twitter data
with open('/Users/maddie/Desktop/twitter-2020-02-11-a78b07526621ffada3b98a8686afc07c4602cbde62e511b321765432f525f2e7/tweet.js', 'r') as f:
    data = json.loads(f.read())


"""
    extract from the data:
    
    1. percentage of my tweets which were retweets of other users content
    2. percentage of my tweets which had engagement
    3. hashtags from the tweets with engagment
    4. time of day of tweets with engagement
    5. no of tweets each day of the week
    6. no of tweets each month
"""

#set up variables, lists and dictionaries
totaltweets = len(data)
retweettotal = 0
engagementtotal = 0
hashtags = []
tweetseachday = dict ()
tweetseachmonth = dict()
timeoftweetswithengagment = dict ()
tweettime = dict()
dayoftweetwithengagment = dict ()

#extract from the JSON data
for i in range(0,totaltweets):
    #percentage retweets from other users
    if "RT" in data[i]["tweet"]["full_text"]:
        retweettotal += 1
    #day tweets were made
    if(data[i]["tweet"]["created_at"][0:3]) not in tweetseachday:
        tweetseachday[data[i]["tweet"]["created_at"][0:3]] = 1
    else:
        tweetseachday[data[i]["tweet"]["created_at"][0:3]] += 1
    #month tweets were made
    if(data[i]["tweet"]["created_at"][3:7]) not in tweetseachmonth:
        tweetseachmonth[data[i]["tweet"]["created_at"][3:7]] = 1
    else:
        tweetseachmonth[data[i]["tweet"]["created_at"][3:7]] += 1
    #hour tweets were made
    if(data[i]["tweet"]["created_at"][11:13]) not in tweettime:
        tweettime[data[i]["tweet"]["created_at"][11:13]] = 1
    else:
        tweettime[data[i]["tweet"]["created_at"][11:13]] += 1
    #percentage with engagment, the hashtags used and time of day the tweet was made
    if data[i]["tweet"]["retweet_count"] != "0" or data[i]["tweet"]["favorite_count"] != "0":
        engagementtotal += 1
        if len(data[i]["tweet"]["entities"]["hashtags"]) > 0:
            for j in range(0, len(data[i]["tweet"]["entities"]["hashtags"])):
                hashtags.append(data[i]["tweet"]["entities"]["hashtags"][j]["text"])
            if data[i]["tweet"]["created_at"][11:13] not in timeoftweetswithengagment:
                timeoftweetswithengagment[data[i]["tweet"]["created_at"][11:13]] = 1
            else:
                timeoftweetswithengagment[data[i]["tweet"]["created_at"][11:13]] += 1
            if(data[i]["tweet"]["created_at"][0:3]) not in dayoftweetwithengagment:
                dayoftweetwithengagment[data[i]["tweet"]["created_at"][0:3]] = 1
            else:
                dayoftweetwithengagment[data[i]["tweet"]["created_at"][0:3]] += 1



retweetpercentage = round(retweettotal/totaltweets*100, 2)
engagmentpercentage = round(engagementtotal/totaltweets*100, 2)







