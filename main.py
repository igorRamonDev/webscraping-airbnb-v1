import pandas as pd
import datetime
import re
import openpyxl
from openpyxl.styles import Font
from web_scraping1 import WebScraping1
from web_scraping2 import WebScraping2
from web_scraping3 import WebScraping3
from web_scraping4 import WebScraping4
from web_scraping5 import WebScraping5

url1 = "https://www.airbnb.com.br/s/Araruama-~-RJ/homes?flexible_trip_lengths%5B%5D=one_week&query=Araruama%20-%20RJ&place_id=ChIJ-6YPcGBplwARPMyE_X9my94&refinement_paths%5B%5D=%2Fhomes&tab_id=home_tab&date_picker_type=calendar&source=structured_search_input_header&search_type=autocomplete_click"
url2 = "https://www.airbnb.com.br/s/Araruama-~-RJ/homes?flexible_trip_lengths%5B%5D=one_week&query=Araruama%20-%20RJ&place_id=ChIJ-6YPcGBplwARPMyE_X9my94&refinement_paths%5B%5D=%2Fhomes&tab_id=home_tab&date_picker_type=calendar&source=structured_search_input_header&search_type=autocomplete_click&price_filter_input_type=0&price_filter_num_nights=5&channel=EXPLORE&federated_search_session_id=da6d6707-e8d1-46ba-b45d-2b8a8acf93f3&pagination_search=true&cursor=eyJzZWN0aW9uX29mZnNldCI6MywiaXRlbXNfb2Zmc2V0IjoxOCwidmVyc2lvbiI6MX0%3D"
url3 = "https://www.airbnb.com.br/s/Araruama-~-RJ/homes?flexible_trip_lengths%5B%5D=one_week&query=Araruama%20-%20RJ&place_id=ChIJ-6YPcGBplwARPMyE_X9my94&refinement_paths%5B%5D=%2Fhomes&tab_id=home_tab&date_picker_type=calendar&source=structured_search_input_header&search_type=autocomplete_click&price_filter_input_type=0&price_filter_num_nights=5&channel=EXPLORE&federated_search_session_id=da6d6707-e8d1-46ba-b45d-2b8a8acf93f3&pagination_search=true&cursor=eyJzZWN0aW9uX29mZnNldCI6MywiaXRlbXNfb2Zmc2V0IjozNiwidmVyc2lvbiI6MX0%3D"
url4 = "https://www.airbnb.com.br/s/Araruama-~-RJ/homes?flexible_trip_lengths%5B%5D=one_week&query=Araruama%20-%20RJ&place_id=ChIJ-6YPcGBplwARPMyE_X9my94&refinement_paths%5B%5D=%2Fhomes&date_picker_type=calendar&source=structured_search_input_header&search_type=autocomplete_click&tab_id=home_tab&price_filter_input_type=0&price_filter_num_nights=5&channel=EXPLORE&federated_search_session_id=dfcff709-9370-4430-b652-64e835829a85&pagination_search=true&cursor=eyJzZWN0aW9uX29mZnNldCI6MywiaXRlbXNfb2Zmc2V0Ijo1NCwidmVyc2lvbiI6MX0%3D"
url5 = "https://www.airbnb.com.br/s/Araruama-~-RJ/homes?flexible_trip_lengths%5B%5D=one_week&query=Araruama%20-%20RJ&place_id=ChIJ-6YPcGBplwARPMyE_X9my94&refinement_paths%5B%5D=%2Fhomes&date_picker_type=calendar&source=structured_search_input_header&search_type=autocomplete_click&tab_id=home_tab&price_filter_input_type=0&price_filter_num_nights=5&channel=EXPLORE&federated_search_session_id=dfcff709-9370-4430-b652-64e835829a85&pagination_search=true&cursor=eyJzZWN0aW9uX29mZnNldCI6MywiaXRlbXNfb2Zmc2V0Ijo3MiwidmVyc2lvbiI6MX0%3D"

web_scraping1 = WebScraping1(url1)
web_scraping2 = WebScraping2(url2)
web_scraping3 = WebScraping3(url3)
web_scraping4 = WebScraping4(url4)
web_scraping5 = WebScraping5(url5)


hora = datetime.datetime.now()

print(web_scraping1.pick_all_rooms())
print(web_scraping2.pick_all_rooms())
print(web_scraping3.pick_all_rooms())
print(web_scraping4.pick_all_rooms())
print(web_scraping5.pick_all_rooms())
print(hora)

# DataFrame url1
df1 = pd.DataFrame({
    'title': [web_scraping1.get_title(room) for room in web_scraping1.get_rooms()],
    ' ': None,
    '  ': None,
    'subtitle': [web_scraping1.get_subtitle(room) for room in web_scraping1.get_rooms()],
    '   ': None,
    '    ': None,
    '      ': None,
    '       ': None,
    'bedrooms': [web_scraping1.get_bedrooms(room) for room in web_scraping1.get_rooms()],
    '        ': None,
    'price': [web_scraping1.get_price(room) for room in web_scraping1.get_rooms()],
    '         ': None,
    '          ': None,
    '           ': None,
    'rating': [web_scraping1.get_rating(room) for room in web_scraping1.get_rooms()],
    '            ': None,
    'superhost': [web_scraping1.is_superhost(room) for room in web_scraping1.get_rooms()],
    '             ': None,
    '': None  # Vazio
})

# DataFrame url2
df2 = pd.DataFrame({
    'title': [web_scraping2.get_title(room) for room in web_scraping2.get_rooms()],
    ' ': None,
    '  ': None,
    'subtitle': [web_scraping2.get_subtitle(room) for room in web_scraping2.get_rooms()],
    '   ': None,
    '    ': None,
    '      ': None,
    '       ': None,
    'bedrooms': [web_scraping2.get_bedrooms(room) for room in web_scraping2.get_rooms()],
    '        ': None,
    'price': [web_scraping2.get_price(room) for room in web_scraping2.get_rooms()],
    '         ': None,
    '          ': None,
    '           ': None,
    'rating': [web_scraping2.get_rating(room) for room in web_scraping2.get_rooms()],
    '            ': None,
    'superhost': [web_scraping2.is_superhost(room) for room in web_scraping2.get_rooms()],
    '             ': None,
    '': None  # Vazio
})

# DataFrame url3
df3 = pd.DataFrame({
    'title': [web_scraping3.get_title(room) for room in web_scraping3.get_rooms()],
    ' ': None,
    '  ': None,
    'subtitle': [web_scraping3.get_subtitle(room) for room in web_scraping3.get_rooms()],
    '   ': None,
    '    ': None,
    '      ': None,
    '       ': None,
    'bedrooms': [web_scraping3.get_bedrooms(room) for room in web_scraping3.get_rooms()],
    '        ': None,
    'price': [web_scraping3.get_price(room) for room in web_scraping3.get_rooms()],
    '         ': None,
    '          ': None,
    '           ': None,
    'rating': [web_scraping3.get_rating(room) for room in web_scraping3.get_rooms()],
    '            ': None,
    'superhost': [web_scraping3.is_superhost(room) for room in web_scraping3.get_rooms()],
    '             ': None,
    '': None  # Vazio
})

# DataFrame url4
df4 = pd.DataFrame({
    'title': [web_scraping4.get_title(room) for room in web_scraping4.get_rooms()],
    ' ': None,
    '  ': None,
    'subtitle': [web_scraping4.get_subtitle(room) for room in web_scraping4.get_rooms()],
    '   ': None,
    '    ': None,
    '      ': None,
    '       ': None,
    'bedrooms': [web_scraping4.get_bedrooms(room) for room in web_scraping4.get_rooms()],
    '        ': None,
    'price': [web_scraping4.get_price(room) for room in web_scraping4.get_rooms()],
    '         ': None,
    '          ': None,
    '           ': None,
    'rating': [web_scraping4.get_rating(room) for room in web_scraping4.get_rooms()],
    '            ': None,
    'superhost': [web_scraping4.is_superhost(room) for room in web_scraping4.get_rooms()],
    '             ': None,
    '': None  # Vazio
})

# DataFrame url5
df5 = pd.DataFrame({
    'title': [web_scraping5.get_title(room) for room in web_scraping5.get_rooms()],
    ' ': None,
    '  ': None,
    'subtitle': [web_scraping5.get_subtitle(room) for room in web_scraping5.get_rooms()],
    '   ': None,
    '    ': None,
    '      ': None,
    '       ': None,
    'bedrooms': [web_scraping5.get_bedrooms(room) for room in web_scraping5.get_rooms()],
    '        ': None,
    'price': [web_scraping5.get_price(room) for room in web_scraping5.get_rooms()],
    '         ': None,
    '          ': None,
    '           ': None,
    'rating': [web_scraping5.get_rating(room) for room in web_scraping5.get_rooms()],
    '            ': None,
    'superhost': [web_scraping5.is_superhost(room) for room in web_scraping5.get_rooms()],
    '             ': None,
    '': None  # Vazio
})

df1['execution'] = hora.strftime("%d/%m/%Y %H:%M:%S")
df2['execution'] = hora.strftime("%d/%m/%Y %H:%M:%S")
df3['execution'] = hora.strftime("%d/%m/%Y %H:%M:%S")
df4['execution'] = hora.strftime("%d/%m/%Y %H:%M:%S")
df5['execution'] = hora.strftime("%d/%m/%Y %H:%M:%S")

# Concatenando os dois dataframes em um único dataframe
df_total = pd.concat([df1, df2, df3, df4, df5])

# função para converter o preço em float


def convert_price_to_float(price_string):
    # Extrai o valor numérico da string usando uma expressão regular
    match = re.search(r'\d+', price_string)
    if match:
        # Converte o valor numérico em float
        return float(match.group())
    else:
        return None


# Insert the 'media/d' column after the placeholder column
df1.insert(18, 'media/d', df1['price'].apply(convert_price_to_float).mean())
# Insert the 'media/d' column after the placeholder column
df2.insert(18, 'media/d', df2['price'].apply(convert_price_to_float).mean())
# Insert the 'media/d' column after the placeholder column
df3.insert(18, 'media/d', df3['price'].apply(convert_price_to_float).mean())
# Insert the 'media/d' column after the placeholder column
df4.insert(18, 'media/d', df4['price'].apply(convert_price_to_float).mean())
# Insert the 'media/d' column after the placeholder column
df5.insert(18, 'media/d', df5['price'].apply(convert_price_to_float).mean())
# Insert the 'media/d' column after the placeholder column
df_total.insert(
    18, 'media/d', df_total['price'].apply(convert_price_to_float).mean())

# df1
df1['media/d'] = df1['price'].apply(convert_price_to_float).mean()
df1['media/d'] = 'R$ ' + \
    df1['media/d'].apply(lambda x: '{:.2f}'.format(x))
# df2
df2['media/d'] = df2['price'].apply(convert_price_to_float).mean()
df2['media/d'] = 'R$ ' + \
    df2['media/d'].apply(lambda x: '{:.2f}'.format(x))
# df3
df3['media/d'] = df3['price'].apply(convert_price_to_float).mean()
df3['media/d'] = 'R$ ' + \
    df3['media/d'].apply(lambda x: '{:.2f}'.format(x))
# df4
df4['media/d'] = df4['price'].apply(convert_price_to_float).mean()
df4['media/d'] = 'R$ ' + \
    df4['media/d'].apply(lambda x: '{:.2f}'.format(x))
# df5
df5['media/d'] = df5['price'].apply(convert_price_to_float).mean()
df5['media/d'] = 'R$ ' + \
    df5['media/d'].apply(lambda x: '{:.2f}'.format(x))
# df_total
df_total['media/d'] = df_total['price'].apply(convert_price_to_float).mean()
df_total['media/d'] = 'R$ ' + \
    df_total['media/d'].apply(lambda x: '{:.2f}'.format(x))

# escreve o DataFrame em um arquivo Excel,
df1.to_excel('url1.xlsx', index=False)
df2.to_excel('url2.xlsx', index=False)
df3.to_excel('url3.xlsx', index=False)
df4.to_excel('url4.xlsx', index=False)
df5.to_excel('url5.xlsx', index=False)
df_total.to_excel('araruama_stats.xlsx', index=False)

# Carregando o excel
workbook = openpyxl.load_workbook('araruama_stats.xlsx')

# Selecionando o worksheet
worksheet = workbook['Sheet1']

# Procurando o titulo
target_title = "Casa com piscina em condomínio Sonho de Vida"

# Encontrando a linha
for row in worksheet.iter_rows(values_only=True):
    if target_title in row:
        target_row = row
        break

# Armazenando apenas os valores nao nulos
values = [value for value in target_row if value is not None]

# Armazenando cada valor da lista em uma variavel
titulo, subtitulo, camas, preco, avaliacao, superhost, execution = values[:7]

# Printando os valores
print(titulo, subtitulo, camas, preco, avaliacao, superhost, execution)
