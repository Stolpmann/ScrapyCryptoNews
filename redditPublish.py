import praw

reddit = praw.Reddit(client_id="CDQv7Uy7ez0MGnGdRLzJlA",
                     client_secret="xL99kLmt1TyBGRskB9_KtXU_EnR1iQ",
                     user_agent="CryptoNewsAPI by u/thecoinisthefuture",
                     password="123Blizzard!",
                     username="thecoinisthefuture")

subr = 'APItesttest'

print(reddit.user.me())

subreddit = reddit.subreddit(subr)

r = open("/Users/Evan/PycharmProjects/ScrapyCryptoNews/test.txt", "r")
#print(r.read())

lines = r.readlines()

last_lines = lines[-2:]

second_last_lines = lines[-5:-3]

print(last_lines)
print(second_last_lines)


def check():
    if last_lines != second_last_lines:
        print("Lines are not equal")

        def append():
            string=''.join(str(item) for item in last_lines)
            a = string.split("\n")
            posttitle, postinfo = a[0],a[1]
            print(string)
            print(posttitle)
            print(postinfo)
            subreddit.submit(posttitle, url=postinfo)
        append()

    elif last_lines == second_last_lines:
        print("Lines are equal")

        #def overwrite():
            #duplicate=''.join(str(item) for item in last_lines)
            #w = open("/Users/Evan/PycharmProjects/ScrapyCryptoNews/test2.txt", "w")
            #w.write(duplicate)
            #print(duplicate)
        #overwrite()

check()