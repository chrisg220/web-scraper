from BeautifulSoup import BeautifulSoup
import mechanize
import time

url = "http://www.hypem.com/"

br = mechanize.Browser()

page = br.open(url)

count = 0

nextLink = []

errorlog = open("errorlog.txt","w")
errorlog.write("Pages not downloaded:\n")
errorlog.close()

while nextLink != None:
    time.sleep(1)
    links = []
    soup = BeautifulSoup(page)
    excerpts = soup.findAll("p",{"class":"excerpt"})
    for excerpt in excerpts:
        link = excerpt.findNext("a", {"class":"more-link"})["href"]
        links.append(link)
        
    for link in links:
        try:
            site = br.open(str(link)).read()
            filename = "/path/to/folder" + str(count) + ".html"
            print filename
            html = open(filename,"wb")
            html.write(site)
            html.close()
            count += 1
        except:
            error = open("errorlog.txt","a")
            text = str(link) + "\n"
            error.write(text)
            error.close()

    current = soup.find("span",{"class":"current"}).text
    nextNumber = str(int(current) + 1)
    try:
        nextLink = soup.find("a", title = nextNumber)["href"]
        page = br.open(nextLink)
    except:
        nextLink = None