import requests
from bs4 import BeautifulSoup

data_directory = 'parsing/data'

def get_summer_garden():
    # адрес страницы для парсинга
    url = 'https://ru.wikipedia.org/wiki/Летний_сад'
    # путь, куда будет сохранен результат парсинга
    file_path = f'./{data_directory}/summer_garden.txt'
    # Делаем запрос к странице
    response = requests.get(url)

    # Проверяем успешность запроса
    if response.status_code == 200:
        # Инициализируем BeautifulSoup для парсинга страницы
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all paragraph tags
        paragraphs = soup.find_all('p')

        # Extract text from each paragraph
        paragraphs_text = [p.get_text() for p in paragraphs]

        # Combine all paragraphs into a single string
        all_text = ''.join(paragraphs_text)

        # Записываем результаты в файл
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(all_text.strip())
            return file_path
        except IOError as e:
            print(f'An error occurred while writing to the file: {e}')
            return None
    else:
        print(f'Failed to retrieve content from {url}, status code {response.status_code}')
        return None
