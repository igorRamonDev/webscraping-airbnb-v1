from bs4 import BeautifulSoup
import requests


class WebScraping:
    def __init__(self, url):
        self.url = url
        self.soup = self.get_html()

    def get_html(self):
        req = requests.get(self.url)
        soup = BeautifulSoup(req.content, "html.parser")
        return soup

    def get_rooms(self):
        return self.soup.find_all("div", class_="c4mnd7m dir dir-ltr")

    def get_title(self, room):
        return room.find("div", class_="t1jojoys dir dir-ltr").text

    def get_subtitle(self, room):
        return room.find("span", class_="t6mzqp7 dir dir-ltr").text

    def get_bedrooms(self, room):
        return room.find("span", class_="dir dir-ltr").text

    def get_price(self, room):
        return room.find("span", class_="a8jt5op dir dir-ltr").text

    def get_rating(self, room):
        return room.find("span", class_="t5eq1io r4a59j5 dir dir-ltr").text

    def is_superhost(self, room):
        return room.find("span", class_="t1mwk1n0 dir dir-ltr") is not None

    def pick_all_rooms(self):
        for room in self.get_rooms():
            title = self.get_title(room)
            subtitle = self.get_subtitle(room)
            bedrooms = self.get_bedrooms(room)
            price = self.get_price(room)
            rating = self.get_rating(room)
            is_superhost = self.is_superhost(room)
            print(title)
            print(subtitle)
            print(bedrooms)
            print(price)
            print(rating)
            print("Superhost: {}".format("Yes" if is_superhost else "No"))
            print("\n")
