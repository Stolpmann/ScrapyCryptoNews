import praw

reddit = praw.Reddit(client_id="CDQv7Uy7ez0MGnGdRLzJlA",
                     client_secret="xL99kLmt1TyBGRskB9_KtXU_EnR1iQ",
                     user_agent="CryptoNewsAPI by u/thecoinisthefuture",
                     password="123Blizzard!",
                     username="thecoinisthefuture")

subr = 'APItesttest'

print(reddit.user.me())

subreddit = reddit.subreddit(subr)


#Cointelegraph Auto Uploader

r = open("/Users/Evan/PycharmProjects/ScrapyCryptoNews/test.txt", "r")

lines = r.readlines()

last_lines = lines[-2:]

second_last_lines = lines[-5:-3]

print(last_lines)
print(second_last_lines)

def check():
    if last_lines != second_last_lines:
        print("\nLines are not equal\n")

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
        print("\nLines are equal\n")

check()


#Bitcoin Magazine Auto Uploader

r2 = open("/Users/Evan/PycharmProjects/ScrapyCryptoNews/test2.txt", "r")

lines2 = r2.readlines()

last_lines2 = lines2[-2:]

second_last_lines2 = lines2[-5:-3]

print(last_lines2)
print(second_last_lines2)

def check2():
    if last_lines2 != second_last_lines2:
        print("\nLines are not equal\n")

        def append2():
            string2=''.join(str(item) for item in last_lines2)
            a2 = string2.split("\n")
            posttitle2, postinfo2 = a2[0],a2[1]
            print(string2)
            print(posttitle2)
            print(postinfo2)
            subreddit.submit(posttitle2, url=postinfo2)
        append2()

    elif last_lines2 == second_last_lines2:
        print("\nLines are equal\n")

check2()