import feedparser

url = "https://cointelegraph.com/rss"

url2 = "https://bitcoinmagazine.com/.rss/full/"

url3 = "https://news.bitcoin.com/feed/"


dir(feedparser)


# Variable for Parsing Given URL

# Cointelegraph
f = feedparser.parse(url)

# Bitcoin Magazine Data
f2 = feedparser.parse(url2)

# News.Bitcoin.com Data
f3 = feedparser.parse(url3)


# Opens text documents for writing parsed data


append = open("/Users/Evan/PycharmProjects/ScrapyCryptoNews/test.txt", "a")

append2 = open("/Users/Evan/PycharmProjects/ScrapyCryptoNews/test2.txt", "a")

append3 = open("/Users/Evan/PycharmProjects/ScrapyCryptoNews/test3.txt", "a")


# Prints Parsed Data

# Cointelegraph Data
def scraperPrint():
    print(f.entries[0].title)
    print(f.entries[0].link)

# Bitcoin Magazine Data
def scraperPrint2():
    print(f2.entries[0].title)
    print(f2.entries[0].link)

def scraperPrint3():
    print(f3.entries[0].title)
    print(f3.entries[0].link)


# Function writes Scraped Data to test.txt

# Cointelegraph Feed
def scraperWriteTitle():
    append.write("\n")
    append.write(f.entries[0].title)
    append.write("\n")
    append.write(f.entries[0].link)
    append.write("\n")

# Bitcoin Magazine Feed
def scraperWriteTitle2():
    append2.write("\n")
    append2.write(f2.entries[0].title)
    append2.write("\n")
    append2.write(f2.entries[0].link)
    append2.write("\n")

def scraperWriteTitle3():
    append3.write("\n")
    append3.write(f3.entries[0].title)
    append3.write("\n")
    append3.write(f3.entries[0].link)
    append3.write("\n")

# Calling all functions

scraperPrint()
scraperWriteTitle()

scraperPrint2()
scraperWriteTitle2()

scraperPrint3()
scraperWriteTitle3()

