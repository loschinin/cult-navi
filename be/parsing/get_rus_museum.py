import requests
from bs4 import BeautifulSoup

data_directory = 'parsing/data'

def get_rus_museum():
    # адрес страницы для парсинга
    url = 'https://rusmuseum.ru/about/'
    # путь, куда будет сохранен результат парсинга
    file_path = f'./{data_directory}/rusmuseum.txt'
    # Делаем запрос к странице
    response = requests.get(url)

    # Проверяем успешность запроса
    if response.status_code == 200:
        # Инициализируем BeautifulSoup для парсинга страницы
        soup = BeautifulSoup(response.text, 'html.parser')

        # Ищем заголовок 'О Русском музее'
        heading = soup.find(lambda tag: tag.name == "h1" and 'О Русском музее' in tag.text)

        all_p = []

        # Если заголовок найден, ищем родительский контейнер
        if heading:
            parent_container = heading.find_next_sibling(class_="container")
            # Затем выбираем все теги <p> внутри этого контейнера
            if parent_container:
                all_p_tags = parent_container.find_all('p')
                for p_tag in all_p_tags:
                    all_p.append(p_tag.text.strip())

        # Преобразуем список строк в одну строку
        one_string = ' '.join(all_p)

        # Записываем результаты в файл
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(one_string)
            return file_path
        except IOError as e:
            print(f'An error occurred while writing to the file: {e}')
            return None
    else:
        print(f'Failed to retrieve content from {url}, status code {response.status_code}')
        return None
