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

newpostlines = r.readlines()

new_last_lines = newpostlines[-2:]

new_second_last_lines = newpostlines[-5:-3]

print(new_last_lines)
print(new_second_last_lines)

def join():
    if new_last_lines != new_second_last_lines:
        string = ''.join(str(item) for item in new_last_lines)
        print(string)
        print("strings are not equal")

    elif new_last_lines == new_second_last_lines:
        print("Lines are equal")
join()


#subreddit.submit(posttitle, url=postinfo)