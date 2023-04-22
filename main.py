from web_scraping import WebScraping
from web_scraping2 import WebScraping2

url = "https://www.airbnb.com.br/s/Araruama-~-RJ/homes?tab_id=home_tab&rehttps://www.airbnb.com.br/s/Araruama-~-RJ/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&price_filter_input_type=0&price_filter_num_nights=5&channel=EXPLORE&query=Araruama%20-%20RJ&place_id=ChIJ-6YPcGBplwARPMyE_X9my94&date_picker_type=calendar&source=structured_search_input_header&search_type=autocomplete_click"
url2 = "https://www.airbnb.com.br/s/Araruama-~-RJ/homes?place_id=ChIJ-6YPcGBplwARPMyE_X9my94&refinement_paths%5B%5D=%2Fhomes&flexible_trip_dates%5B%5D=april&flexible_trip_dates%5B%5D=may&flexible_trip_dates%5B%5D=june&flexible_trip_dates%5B%5D=july&flexible_trip_dates%5B%5D=august&flexible_trip_dates%5B%5D=september&flexible_trip_dates%5B%5D=october&flexible_trip_dates%5B%5D=november&flexible_trip_dates%5B%5D=december&flexible_trip_dates%5B%5D=january&flexible_trip_dates%5B%5D=february&flexible_trip_dates%5B%5D=march&flexible_trip_lengths%5B%5D=one_week&date_picker_type=flexible_dates&adults=0&children=0&infants=0&pets=0&search_type=AUTOSUGGEST"

web_scraping = WebScraping(url)
web_scraping2 = WebScraping2(url2)

print(web_scraping.pick_all_rooms())
print(web_scraping2.pick_all_rooms())
