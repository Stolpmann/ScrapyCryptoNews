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

#Bitcoin Magazine Auto Uploader

r3 = open("/Users/Evan/PycharmProjects/ScrapyCryptoNews/test3.txt", "r")

lines3 = r3.readlines()

last_lines3 = lines3[-2:]

second_last_lines3 = lines3[-5:-3]

print(last_lines3)
print(second_last_lines3)

def check3():
    if last_lines3 != second_last_lines3:
        print("\nLines are not equal\n")

        def append3():
            string3=''.join(str(item) for item in last_lines3)
            a3 = string3.split("\n")
            posttitle3, postinfo3 = a3[0],a3[1]
            print(string3)
            print(posttitle3)
            print(postinfo3)
            subreddit.submit(posttitle3, url=postinfo3)
        append3()

    elif last_lines3 == second_last_lines3:
        print("\nLines are equal\n")

check3()

#Bitcoin Magazine Auto Uploader

r4 = open("/Users/Evan/PycharmProjects/ScrapyCryptoNews/test4.txt", "r")

lines4 = r4.readlines()

last_lines4 = lines4[-2:]

second_last_lines4 = lines4[-5:-3]

print(last_lines4)
print(second_last_lines4)

def check4():
    if last_lines4 != second_last_lines4:
        print("\nLines are not equal\n")

        def append4():
            string4=''.join(str(item) for item in last_lines4)
            a4 = string4.split("\n")
            posttitle4, postinfo4 = a4[0],a4[1]
            print(string4)
            print(posttitle4)
            print(postinfo4)
            subreddit.submit(posttitle4, url=postinfo4)
        append4()

    elif last_lines4 == second_last_lines4:
        print("\nLines are equal\n")

check4()

#Bitcoin Magazine Auto Uploader

r5 = open("/Users/Evan/PycharmProjects/ScrapyCryptoNews/test5.txt", "r")

lines5 = r5.readlines()

last_lines5 = lines5[-2:]

second_last_lines5 = lines5[-5:-3]

print(last_lines5)
print(second_last_lines5)

def check5():
    if last_lines5 != second_last_lines5:
        print("\nLines are not equal\n")

        def append5():
            string5=''.join(str(item) for item in last_lines5)
            a5 = string5.split("\n")
            posttitle5, postinfo5 = a5[0], a5[1]
            print(string5)
            print(posttitle5)
            print(postinfo5)
            subreddit.submit(posttitle5, url=postinfo5)
        append5()

    elif last_lines5 == second_last_lines5:
        print("\nLines are equal\n")

check5()