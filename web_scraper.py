import requests
from bs4 import BeautifulSoup

def web_scraping(url):
    # Effettua la richiesta HTTP alla pagina web
    response = requests.get(url)

    # Verifica se la richiesta è andata a buon fine (status code 200)
    if response.status_code == 200:
        # Utilizza BeautifulSoup per analizzare il contenuto HTML della pagina
        soup = BeautifulSoup(response.text, 'html.parser')

        # Esempio: Estrai tutti i link dalla pagina
        links = soup.find_all('a')
        for link in links:
            print(link.get('href'))
    else:
        print(f"Errore nella richiesta. Status code: {response.status_code}")

# Personalizza l'URL di destinazione
url_da_personalizzare = 'https://example.com'

# Chiama la funzione con l'URL personalizzato
web_scraping(url_da_personalizzare)
