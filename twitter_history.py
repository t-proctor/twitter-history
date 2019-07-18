import re
import random
import webbrowser

def favorites(num):
    #use like file to figure out your favorites
    with open('like.js') as dataFile:
        lines = dataFile.read()
        expandedURL = [m.start() for m in re.finditer('expandedUrl', lines)]
        quotes = [m.start() for m in re.finditer('"', lines)]
        entries = []
        # entries.append(lines[401:453])
        for eu in expandedURL:
            for i in range(len(quotes)):
                if quotes[i] == (eu - 1):
                    begIndex = quotes[i+2] + 1
                    endIndex = quotes[i+3]
                    entries.append(lines[begIndex:endIndex])
        x = random.sample(entries, num)
        for z in x:
            webbrowser.open(z)

def retweets(num):
    #use tweets file to figure out your retweets
    with open("tweet.js") as dataFile:
        retweets = []
        contents = dataFile.read()
        retweet = [m.start() for m in re.finditer('RT @', contents)]
        colon = [m.start() for m in re.finditer(':', contents)]
        id = [m.start() for m in re.finditer('id_str', contents)]
        quotes = [m.start() for m in re.finditer('"', contents)]

        for tweet in retweet:
            for i in range(len(colon)):
                if colon[i] == (tweet - 3):
                    begIndex = tweet + 4
                    endIndex = colon[i+1]
                    retweets.append(contents[begIndex:endIndex])
        authors = []
        count = 0
        for i in range(len(retweet)):
            for j in range(len(id)):
                if ((retweet[i]- 300) < id[j]) and (id[j] < retweet[i]):
                    count += 1
                    for k in range(len(quotes)):
                        if quotes[k] == (id[j] + 10):
                            begIndex = quotes[k] + 1
                            endIndex = quotes[k + 1]
                            authors.append(contents[begIndex:endIndex])
        urls = []
        for i in range(len(retweets)):
            url = "https://twitter.com/" + retweets[i] + "/status/" + authors[i]
            urls.append(url)
        q = random.sample(urls, num)
        for wow in q:
            webbrowser.open(wow)


def your_tweets(num):
    your_username = ""
    #use account file to figure out your username
    with open("account.js") as dataFile:
        contents = dataFile.read()
        username = [m.start() for m in re.finditer('username', contents)]
        quotes = [m.start() for m in re.finditer('"', contents)]
        for b in range(len(quotes) - 1):
            if quotes[b] + 1 == username[0]:
                begIndex = quotes[b + 2] + 1
                endIndex = quotes[b + 3]
                your_username = contents[begIndex:endIndex]
    your_username = "tim__proctor"

    #use tweets to figure out your tweets
    with open("tweet2.js") as dataFile:
        contents = dataFile.read()
        fulltext = [m.start() for m in re.finditer('full_text', contents)]
        id = [m.start() for m in re.finditer('id', contents)]
        quotes = [m.start() for m in re.finditer('"', contents)]
        your_tweets = []
        for i in range(len(fulltext)):
            if contents[fulltext[i] + 14:fulltext[i] + 18] != "RT @":
                for j in range(len(id)):
                    if ((fulltext[i] - 300) < id[j]) and (id[j] < fulltext[i]):
                        for k in range(len(quotes)):
                            if quotes[k] == (id[j] + 10):
                                begIndex = quotes[k] + 1
                                endIndex = quotes[k + 1]
                                your_tweets.append(contents[begIndex:endIndex])
        urls = []
        for i in range(len(your_tweets)):
            url = "https://twitter.com/" + your_username + "/status/" + your_tweets[i]
            urls.append(url)
        q = random.sample(urls, num)
        for wow in q:
            webbrowser.open(wow)

def main():
    what_tweets = input("Type in RT for Retweets, FV for Favorites, YT for Your Tweets, RTYT for Retweets and Tweets, etc  \n")
    how_many = int(input("How many tweets would you like to open of each? "))

    if "RT" in what_tweets:
        retweets(how_many)

    if "FV" in what_tweets:
        favorites(how_many)

    if "YT" in what_tweets:
        your_tweets(how_many)

if __name__ == "__main__":
    main()
