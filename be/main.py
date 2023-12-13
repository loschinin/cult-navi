import pandas as pd
from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# решаем проблему с CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Разрешает все источники
    allow_credentials=True,
    allow_methods=["*"],  # Разрешает все методы
    allow_headers=["*"],  # Разрешает все заголовки
)

# Музеи, с которыми мы работаем.
museums_info = [
    {"id": 1, 'name': 'Музей современного искусства Эрарта', "url": 'https://ru.wikipedia.org/wiki/Эрарта'},
    {"id": 2, 'name': 'Государственный Эрмитаж', "url": 'https://ru.wikipedia.org/wiki/Эрмитаж'},
    {"id": 3, 'name': 'Музей Фаберже', "url": 'https://ru.wikipedia.org/wiki/Музей_Фаберже_в_Санкт-Петербурге'},
    {"id": 4, 'name': 'Государственный Русский музей', "url": 'https://ru.wikipedia.org/wiki/Государственный_Русский_музей'},
    {"id": 5, 'name': 'Летний сад', "url": 'https://ru.wikipedia.org/wiki/Летний_сад'},
    {"id": 6, 'name': 'Государственный музей городской скульптуры', "url": 'https://ru.wikipedia.org/wiki/Государственный_музей_городской_скульптуры'},
    {"id": 7, 'name': 'Музей-квартира А. И. Куинджи', "url": 'https://ru.wikipedia.org/wiki/Музей-квартира_А._И._Куинджи'},
    {"id": 8, 'name': 'Новый музей', "url": "https://ru.wikipedia.org/wiki/Новый_музей_(Санкт-Петербург)"},
    {"id": 9, 'name': 'Музей прикладного искусства СПбГХПА им.А.Л.Штиглица', "url": "https://ru.wikipedia.org/wiki/Музей_А._Л._Штиглица"},
    {"id": 10, 'name': 'Музей стрит-арта', "url": "https://ru.wikipedia.org/wiki/Музей_стрит-арта"},
    {"id": 11, 'name': 'Музей искусства Санкт-Петербурга XX-XXI веков', "url": "https://ru.wikipedia.org/wiki/Музей_искусства_Санкт-Петербурга_XX-XXI_веков"},
    {"id": 12, 'name': 'Елагин дворец', "url": 'https://ru.wikipedia.org/wiki/Елагин_дворец'},
    {"id": 13, 'name': 'Музей «Царскосельская коллекция»', "url": 'https://ru.wikipedia.org/wiki/Царскосельская_коллекция'},
    {"id": 14, 'name': 'Музей «Санкт-Петербургский музей кукол»', "url": 'https://ru.wikipedia.org/wiki/Санкт-Петербургский_музей_кукол'},
    {"id": 15, 'name': 'Зоологический музей', "url": 'https://ru.wikipedia.org/wiki/Зоологический_музей_Зоологического_института_РАН'},
    {"id": 16, 'name': 'Русское географическое общество', "url": 'https://ru.wikipedia.org/wiki/Русское_географическое_общество'},
    {"id": 17, 'name': 'Всероссийский музей А. С. Пушкина', "url": 'https://ru.wikipedia.org/wiki/Всероссийский_музей_А._С._Пушкина'},
    {"id": 18, 'name': 'Санкт-Петербургский музей театрального и музыкального искусства', "url": 'https://ru.wikipedia.org/wiki/Санкт-Петербургский_музей_театрального_и_музыкального_искусства'},
    {"id": 19, 'name': 'Российский этнографический музей', "url": 'https://ru.wikipedia.org/wiki/Российский_этнографический_музей'},
    {"id": 20, 'name': 'Государственный музей истории религии', "url": 'https://ru.wikipedia.org/wiki/Государственный_музей_истории_религии'},
    {"id": 21, 'name': 'Петропавловская крепость', "url": 'https://ru.wikipedia.org/wiki/Петропавловская_крепость'},
    {"id": 22, 'name': 'Нарвская застава (музей)', "url": 'https://ru.wikipedia.org/wiki/Нарвская_застава_(музей)'},
    {"id": 23, 'name': 'Музей политической истории России', "url": 'https://ru.wikipedia.org/wiki/Музей_политической_истории_России'},
    {"id": 24, 'name': 'Дворец Юсуповых на Мойке', "url": 'https://ru.wikipedia.org/wiki/Дворец_Юсуповых_на_Мойке'},
    {"id": 25, 'name': 'Государственный мемориальный музей обороны и блокады Ленинграда', "url": 'https://ru.wikipedia.org/wiki/Государственный_мемориальный_музей_обороны_и_блокады_Ленинграда'},
    {"id": 26, 'name': 'Военно-исторический музей артиллерии, инженерных войск и войск связи', "url": 'https://ru.wikipedia.org/wiki/Военно-исторический_музей_артиллерии,_инженерных_войск_и_войск_связи'},
    {"id": 27, 'name': 'Аврора (крейсер)', "url": 'https://ru.wikipedia.org/wiki/Аврора_(крейсер)'},
    {"id": 28, 'name': 'Центральный военно-морской музей имени императора Петра Великого', "url": 'https://ru.wikipedia.org/wiki/Центральный_военно-морской_музей_имени_императора_Петра_Великого'},
    {"id": 29, 'name': 'Музей игрушки (Санкт-Петербург)', "url": 'https://ru.wikipedia.org/wiki/Музей_игрушки_(Санкт-Петербург)'},
    {"id": 30, 'name': 'Музей сновидений Фрейда', "url": 'https://ru.wikipedia.org/wiki/Музей_сновидений_Фрейда'},
    {"id": 31, 'name': 'Исаакиевский собор', "url": 'https://ru.wikipedia.org/wiki/Исаакиевский_собор'},
    {"id": 32, 'name': 'Нарвские триумфальные ворота', "url": 'https://ru.wikipedia.org/wiki/Нарвские_триумфальные_ворота'},

]

@app.get("/museums")
async def get_museums():
    # На клиент отправляется только список с названиями музеев
    museum_names = [museum['name'] for museum in museums_info]
    return museum_names

class MuseumRequest(BaseModel):
    name: str
    prompt: str

@app.post("/query")
async def query_museum(museum_request: MuseumRequest):

    # Получение самого КОНТЕКСТА из файла, который играет роль базы данных

    new_context_df = pd.read_csv(f'./museums_data.csv')

    filtered_df = new_context_df[new_context_df['name'] == museum_request.name]

    # Check if any data is found
    if not filtered_df.empty:
        museum_data = filtered_df.iloc[0]['data']
    else:
        # Handle the case where no data is found
        museum_data = f"No data available for {museum_request.name}"

    print(museum_data)

    context = museum_data

    # Отправка запроса к нейронной сети
    # response_from_neural_network = await query_neural_network(context, museum_request.prompt)

    if museum_request.name == '':
       response_from_neural_network = 'Пожалуйста, выберите музей из списка наверху.'
    else:
        # TODO: удалить после того, как нейросеть будет подключена и заменить на нормальный ответ.
        response_from_neural_network = f'Привет! Это нейросеть. Ты в {museum_request.name} завтра идешь? Билет возьми, я себе уже купила'



    return {"response": response_from_neural_network}
