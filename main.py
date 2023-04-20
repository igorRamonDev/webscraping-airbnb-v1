from web_scraping import WebScraping

url = "https://www.airbnb.com.br/s/Araruama-~-RJ/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&price_filter_input_type=0&price_filter_num_nights=5&channel=EXPLORE&query=Araruama%20-%20RJ&place_id=ChIJ-6YPcGBplwARPMyE_X9my94&date_picker_type=calendar&source=structured_search_input_header&search_type=autocomplete_click"
web_scraping = WebScraping(url)
print(web_scraping.pick_all_rooms())
