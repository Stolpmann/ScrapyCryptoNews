import feedparser
import schedule


url = "https://cointelegraph.com/rss"

dir(feedparser)

f = feedparser.parse(url)

f2 = open("/Users/Evan/PycharmProjects/ScrapyCryptoNews/test.txt", "a")



#print(f)

print(f.keys())

# Check Feed

#print(f.entries)

def scraperprint():
    print(f.entries[0].title)
    print(f.entries[0].link)

def scraperwritetitle():
    f2.write("\n")
    f2.write(f.entries[0].title)
    f2.write("\n")
    f2.write(f.entries[0].link)


scraperprint()
scraperwritetitle()

    #for entry in f.entries:
        #print(entry.title)
        #print(entry.link)
        #print(entry.published)
        #print(entry.description)

