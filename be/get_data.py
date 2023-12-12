import requests
from bs4 import BeautifulSoup
from urllib.parse import unquote

def get_data(url):
    # Делаем запрос к странице
    response = requests.get(url)

    # Проверяем успешность запроса
    if response.status_code == 200:
        # Инициализируем BeautifulSoup для парсинга страницы
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all paragraph tags
        paragraphs = soup.find_all('p')

        # Extract text from each paragraph
        paragraphs_text = ' '.join(p.get_text(strip=True) for p in paragraphs if p.get_text(strip=True))

        # Возвращаем текст всех параграфов
        return paragraphs_text
    else:
        print(f'Failed to retrieve content from {url}, status code {response.status_code}')
        return None, None