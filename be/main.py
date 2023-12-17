import pandas as pd
from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from langchain.retrievers import WikipediaRetriever
from langchain.chat_models.gigachat import GigaChat
from langchain.chains import ConversationalRetrievalChain

app = FastAPI()

# решаем проблему с CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Разрешает все источники
    allow_credentials=True,
    allow_methods=["*"],  # Разрешает все методы
    allow_headers=["*"],  # Разрешает все заголовки
)


def llm_answer(question:str, chat_history:list, qa) -> str:
    result = qa({"question": question, "chat_history": chat_history})
    chat_history.append((question, result["answer"])) 
    return result['answer']

giga = GigaChat(credentials='YWEyOWY4Y2EtYWI0MC00M2RlLWEzZDQtY2VkZTUwYzdhYTFhOjU4ODUwNTkxLTkzMjAtNGNiOC05YWZlLTQ1YjFjMmY3ODdiMw==', verify_ssl_certs=False)

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
]
retriever = WikipediaRetriever(lang='ru', load_max_docs=2)
chat_history = []

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
    docs = retriever.get_relevant_documents(query=museum_request.name, lang="ru")
    qa = ConversationalRetrievalChain.from_llm(giga, retriever=retriever)

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
        # response_from_neural_network = f'Привет! Это нейросеть. Ты в {museum_request.name} завтра идешь? Билет возьми, я себе уже купила'
        response_from_neural_network = llm_answer(museum_request.prompt, chat_history, qa)


    return {"response": response_from_neural_network}
