from bs4 import BeautifulSoup
import requests
from database import Database

#initializing Database class
db = Database()

r = requests.get("https://www.reddit.com/r/TechNewsToday/", 
                 headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})

soup = BeautifulSoup(r.content, "html.parser")

#Scrapping Part and adding data to db using functions
article_div = soup.find_all("article" , {"class" : "yn9v_hQEhjlRNZI0xspbA"})

for i in article_div:
    article = i.find("h3", {"class" : "_eYtD2XCVieq6emjKBH3m"}).text #Article
    #Extracting Image url out of a weird Div style attribute
    img_div = i.find("div", {"class" : "_2c1ElNxHftd8W_nZtcG9zf _33Pa96SGhFVpZeI6a7Y_Pl"})
    style_attr = img_div.get("style")
    url_start = style_attr.index("(") + 1
    url_end = style_attr.index(")")
    img = style_attr[url_start : url_end] #Finally Image URL
    all_data = db.fetch_all()
    all_article = [i[0] for i in all_data[0]]
    all_img = [i[0] for i in all_data[1]]
    #checking if content exists already or not, if not then add
    if article not in all_article and img not in all_img:
        db.add_content(article, img) #adding content to db