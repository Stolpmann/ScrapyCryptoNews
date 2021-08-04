import praw

reddit = praw.Reddit(client_id="CDQv7Uy7ez0MGnGdRLzJlA",
                     client_secret="xL99kLmt1TyBGRskB9_KtXU_EnR1iQ",
                     user_agent="CryptoNewsAPI by u/thecoinisthefuture",
                     password="123Blizzard!",
                     username="thecoinisthefuture")

r = open("/Users/Evan/PycharmProjects/ScrapyCryptoNews/test.txt", "r")
#print(r.read())

lines = r.readlines()
second_last_lines = lines[-4:-2]

last_lines = lines[-2:]

print(last_lines)
print(second_last_lines)


def check():
    if last_lines != second_last_lines:
        print("Lines are not equal")

        def pub():
            string=''.join(str(item) for item in last_lines)
            w = open("/Users/Evan/PycharmProjects/ScrapyCryptoNews/test2.txt", "a")
            w.write(string)
        pub()

    else:
        print("Lines are equal")

check()


def pubtoreddit():
    read = open("/Users/Evan/PycharmProjects/ScrapyCryptoNews/test2.txt", "r")
    lines2 = read.readlines()
    second_last_lines2 = lines2[-4:-2]
    last_lines2 = lines2[-2:]
    posttitle, postinfo = read.readlines()

    if last_lines2 != second_last_lines2:
        subr = 'APItesttest'
        subreddit = reddit.subreddit(subr)
        subreddit.submit(posttitle, url=postinfo)
    pubtoreddit()