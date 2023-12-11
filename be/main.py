from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from helpers import get_museum_context

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
museums_map = {'Государственный Эрмитаж': 'hermitage', 'Музей Фаберже': 'faberzhe', 'Государственный Русский музей': 'rusmuseum', 'Летний сад': '', 'Государственный музей городской скульптуры': '', 'Музей-усадьба П. П. Чистякова': '', 'Музей-квартира А. И. Куинджи': '', 'Музей современного искусства Эрарта': '', 'Новый музей': '', 'Музей прикладного искусства СПбГХПА им.А.Л.Штиглица': ''}

# Если значение отсутствует, то музей исключается. Значение должно совпадать с именем файла в parsing/data
filtered_museums_map = {k: v for k, v in museums_map.items() if v}

@app.get("/museums")
async def get_museums():
    # На клиент отправляется только список с названиями музеев
    museums = list(filtered_museums_map.keys())
    return museums

class MuseumRequest(BaseModel):
    name: str
    prompt: str

@app.post("/query")
async def query_museum(museum_request: MuseumRequest):
    data_directory = 'parsing/data'

    # Получение пути к файлу в зависимости от того, что пришло от клиента
    file_name = filtered_museums_map.get(museum_request.name, "")
    file_path = f'./{data_directory}/{file_name}.txt'

    # Получение самого КОНТЕКСТА из директории data_directory
    context = get_museum_context(file_path)

    # Отправка запроса к нейронной сети
    # response_from_neural_network = await query_neural_network(context, museum_request.prompt)

    # TODO: удалить после того, как нейросеть будет подключена и заменить на нормальный ответ.
    response_from_neural_network = f'Привет! Это нейросеть. Ты в {museum_request.name} завтра идешь? Билет возьми, я себе уже купила'

    return {"response": response_from_neural_network}
