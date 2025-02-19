from bs4 import BeautifulSoup

import requests
import random


NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
API_KEY = "GX07FK8Q02082Q46"
NEWS_API_KEY = "86da72a39afa4b9cb0df3d5b48811d82"

news_feed_parameters = {
    "q": "premier league ",
    "from": "2025-01-10",
    "sortBy": "popularity",
    "apiKey": NEWS_API_KEY
}
response=requests.get(url=NEWS_ENDPOINT, params=news_feed_parameters)
news=response.json()
news_feed=news["articles"]
news_article_list = news_feed[:6]
article_list=[]
for article in news_article_list:
    article_list.append(article)


from flask import Flask,render_template
# soup=BeautifulSoup()
app=Flask(__name__)
import datetime

rand_num=random.randint(0,2)



@app.route("/")
def home():
    current_time = datetime.datetime.today()
    current_year = current_time.year
    return render_template("index.html",year=current_year,news=article_list)
@app.route("/injury_updates")
def injury_updates():
    current_time = datetime.datetime.today()
    current_date=current_time.strftime("%Y-%m-%d")
    return render_template("generic.html",date=current_date)
@app.route("/transfer_news")
def transfer_news():
    return render_template("elements.html")


if __name__=="__main__":
    app.run(debug=True)