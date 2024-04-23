import csv
from bs4 import BeautifulSoup
import requests


class Parser:
    html = ""

    def __init__(self, url, path):
        self.url = url
        self.path = path

    def get_html(self):
        req = requests.get(self.url).text
        self.html = BeautifulSoup(req, "html.parser")

    def parsing(self):
        news = self.html.find_all("section", class_="news_item")
        for item in news:
            title = item.find("span", class_="item_text__title").text
            news_link = item.find("div", class_="item_text").find("a").get('href')
            rubric_link = item.find("a", class_="rubric_link").get('href')
            rubric_name = item.find("a", class_="rubric_link").text
            data = {"title": title, "news_link": news_link, "rubric_link": rubric_link,
                    "rubric_name": rubric_name}
            # print(data)
            self.save_csv(data)

    def save_csv(self, data):
        with open(self.path, 'a') as f:
            writer = csv.writer(f, delimiter=";", lineterminator="\r")
            writer.writerow([data['title'], data['news_link'], data['rubric_link'], data['rubric_name']])

    def run(self):
        self.get_html()
        self.parsing()


if __name__ == '__main__':
    n = Parser("https://aif.ru/", "news.csv")
    n.run()
