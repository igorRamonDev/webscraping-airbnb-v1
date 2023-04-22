import pandas as pd
from web_scraping import WebScraping
from web_scraping2 import WebScraping2

url = "https://www.airbnb.com.br/s/Araruama-~-RJ/homes?flexible_trip_lengths%5B%5D=one_week&query=Araruama%20-%20RJ&place_id=ChIJ-6YPcGBplwARPMyE_X9my94&refinement_paths%5B%5D=%2Fhomes&tab_id=home_tab&date_picker_type=calendar&source=structured_search_input_header&search_type=autocomplete_click"
url2 = "https://www.airbnb.com.br/s/Araruama-~-RJ/homes?flexible_trip_lengths%5B%5D=one_week&query=Araruama%20-%20RJ&place_id=ChIJ-6YPcGBplwARPMyE_X9my94&refinement_paths%5B%5D=%2Fhomes&tab_id=home_tab&date_picker_type=calendar&source=structured_search_input_header&search_type=autocomplete_click&price_filter_input_type=0&price_filter_num_nights=5&channel=EXPLORE&federated_search_session_id=da6d6707-e8d1-46ba-b45d-2b8a8acf93f3&pagination_search=true&cursor=eyJzZWN0aW9uX29mZnNldCI6MywiaXRlbXNfb2Zmc2V0IjoxOCwidmVyc2lvbiI6MX0%3D"

web_scraping = WebScraping(url)
web_scraping2 = WebScraping2(url2)

print(web_scraping.pick_all_rooms())
print(web_scraping2.pick_all_rooms())

df = pd.DataFrame({
    'title': [web_scraping.get_title(room) for room in web_scraping.get_rooms()],
    'subtitle': [web_scraping.get_subtitle(room) for room in web_scraping.get_rooms()],
    'bedrooms': [web_scraping.get_bedrooms(room) for room in web_scraping.get_rooms()],
    'price': [web_scraping.get_price(room) for room in web_scraping.get_rooms()],
    'rating': [web_scraping.get_rating(room) for room in web_scraping.get_rooms()],
    'is_superhost': [web_scraping.is_superhost(room) for room in web_scraping.get_rooms()]
})

df2 = pd.DataFrame({
    'title': [web_scraping2.get_title(room) for room in web_scraping2.get_rooms()],
    'subtitle': [web_scraping2.get_subtitle(room) for room in web_scraping2.get_rooms()],
    'bedrooms': [web_scraping2.get_bedrooms(room) for room in web_scraping2.get_rooms()],
    'price': [web_scraping2.get_price(room) for room in web_scraping2.get_rooms()],
    'rating': [web_scraping2.get_rating(room) for room in web_scraping2.get_rooms()],
    'is_superhost': [web_scraping2.is_superhost(room) for room in web_scraping2.get_rooms()]
})

# escreve o DataFrame em um arquivo Excel
df.to_excel('output.xlsx', index=False)
df2.to_excel('output2.xlsx', index=False)
