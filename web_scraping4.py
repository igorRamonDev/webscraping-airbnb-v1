# url4 ="https://www.airbnb.com.br/s/Araruama-~-RJ/homes?flexible_trip_lengths%5B%5D=one_week&query=Araruama%20-%20RJ&place_id=ChIJ-6YPcGBplwARPMyE_X9my94&refinement_paths%5B%5D=%2Fhomes&tab_id=home_tab&date_picker_type=calendar&source=structured_search_input_header&search_type=autocomplete_click"
from bs4 import BeautifulSoup
import requests


class WebScraping4:
    def __init__(self, url4):
        self.url4 = url4
        self.soup = self.get_html()

    def get_html(self):
        req = requests.get(self.url4)
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
        rating_elem = room.find("span", class_="r1dxllyb dir dir-ltr")
        return rating_elem.text if rating_elem is not None else "N/A"

    def is_superhost(self, room):
        superhost_div = room.find("div", class_="t1mwk1n0 dir dir-ltr")
        if superhost_div is not None:
            return superhost_div.text
        else:
            return ""

    def pick_all_rooms(self):
        all_rooms = []
        for room in self.get_rooms():
            title = self.get_title(room)
            subtitle = self.get_subtitle(room)
            bedrooms = self.get_bedrooms(room)
            price = self.get_price(room)
            rating = self.get_rating(room)
            is_superhost = self.is_superhost(room)
            all_rooms.append({"title": title,
                              "subtitle": subtitle,
                              "bedrooms": bedrooms,
                              "price": price,
                              "rating": rating,
                              "is_superhost": is_superhost})
        return all_rooms
