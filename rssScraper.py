import feedparser

url = "https://cointelegraph.com/rss"

dir(feedparser)

# Variable for Parsing Given URL
f = feedparser.parse(url)

# Opens test.txt for writing
f2 = open("/Users/Evan/PycharmProjects/ScrapyCryptoNews/test.txt", "a")

# Prints Parsed Data
def scraperPrint():
    print(f.entries[0].title)
    print(f.entries[0].link)

# Function writes Scraped Data to test.txt
def scraperWriteTitle():
    f2.write("\n")
    f2.write(f.entries[0].title)
    f2.write("\n")
    f2.write(f.entries[0].link)
    f2.write("\n")

# Calling all functions
scraperPrint()
scraperWriteTitle()