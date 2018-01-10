import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = ('http://www.smithandcrown.com/icos/')
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# html soup
page_soup = soup(page_html, "html.parser")


containers = page_soup.findAll("tr", {"class":"clickable-row"})

# csv bounce code - for later use
# filename = "icos.csv"
# f = open(filename, "w")

# headers = "ico_name, ico_url, ico_start_date\n"

# f.write("")


for container in containers:
    name_container = container.span
    ico_name = name_container.text

    # this is the spot I'm having issues with - can't seem to grab the url within this tag.

    url_container = container.findAll("tr")
    ico_url = url_container.findAll("data-url")

    date_container = container.find("td", {"class":"detail-col-date"}).text
    ico_start_date = date_container

    print(ico_name)
    print(ico_url)
    print(ico_start_date)

