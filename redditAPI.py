import praw

reddit = praw.Reddit(client_id="CDQv7Uy7ez0MGnGdRLzJlA",
                     client_secret="xL99kLmt1TyBGRskB9_KtXU_EnR1iQ",
                     user_agent="CryptoNewsAPI by u/thecoinisthefuture",
                     password="123Blizzard!",
                     username="thecoinisthefuture")

subr = 'APItesttest'

print(reddit.user.me())


subreddit = reddit.subreddit(subr)

print(reddit.subreddit(subr))

r = open("/Users/Evan/PycharmProjects/ScrapyCryptoNews/test2.txt", "r")

posttitle, postinfo = r.readlines()

print(posttitle)

print(postinfo)

#def join():
#    string = ''.join(str(item) for item in postinfo)
#    print(string)
#join()


subreddit.submit(posttitle, url=postinfo)