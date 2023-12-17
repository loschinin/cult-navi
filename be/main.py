import pandas as pd
from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from langchain.retrievers import WikipediaRetriever
from langchain.chat_models.gigachat import GigaChat
# from langchain.chains import ConversationalRetrievalChain
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

app = FastAPI()

# решаем проблему с CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Разрешает все источники
    allow_credentials=True,
    allow_methods=["*"],  # Разрешает все методы
    allow_headers=["*"],  # Разрешает все заголовки
)


# def llm_answer(question:str, chat_history:list, qa) -> str:
#     result = qa({"question": question, "chat_history": chat_history})
#     chat_history.append((question, result["answer"])) 
#     return result['answer']


def llm_answer(question: str, museum: str) -> str:
    # raw_answer = db.similarity_search_with_score(question)
    giga = GigaChat(credentials='YWEyOWY4Y2EtYWI0MC00M2RlLWEzZDQtY2VkZTUwYzdhYTFhOjU4ODUwNTkxLTkzMjAtNGNiOC05YWZlLTQ1YjFjMmY3ODdiMw==', verify_ssl_certs=False)
    
    docs = retriever.get_relevant_documents(query=museum, lang="ru")
    doc = docs[0].metadata
    doc['question'] = question
    prompt_template = """ Представь, что ты специалист по музеям Санкт-Петербурга.
    Ответь на вопрос: '{question}' используя ТОЛЬКО информацию из документа: 
    ```{summary}```.
    Твой ответ должен быть сухим, кратким и релевантным вопросу. Выведи только свой ответ."""

    PROMPT = PromptTemplate(template=prompt_template,
                            input_variables=['question', 'summary'])

    qa_chain = LLMChain(prompt=PROMPT,llm=giga)
    answer = qa_chain.run(doc)
    return answer.strip()

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
    {"id": 33, 'name': 'Мраморный дворец', "url": 'https://ru.wikipedia.org/wiki/Мраморный_дворец_(Санкт-Петербург)'},
    {"id": 34, 'name': 'Инженерный (Михайловский) замок', "url": 'https://ru.wikipedia.org/wiki/Михайловский_замок'},
    {"id": 35, 'name': 'Строгановский дворец', "url": 'https://ru.wikipedia.org/wiki/Строгановский_дворец'},
    {"id": 36, 'name': 'Научно-исследовательский музей Российской академии художеств', "url": 'https://ru.wikipedia.org/wiki/Санкт-Петербургский_государственный_академический_институт_живописи,_скульптуры_и_архитектуры_имени_И._Е._Репина'},
    {"id": 37, 'name': 'Елагиноостровский дворец-музей декоративно-прикладного искусства и интерьера XVIII-XXI веков', "url": 'https://ru.wikipedia.org/wiki/Елагин_дворец'},
    {"id": 38, 'name': 'Музей прикладного искусства Санкт-Петербургской Государственной художественно-промышленной академии им. А. Л. Штиглица', "url": 'https://ru.wikipedia.org/wiki/Музей_А._Л._Штиглица'},
    {"id": 39, 'name': 'Галерея «Петербургский центр искусств»', "url": 'https://ru.wikipedia.org/w/index.php?title=Галерея_«Петербургский_центр_искусств»&action=edit&redlink=1'},
    {"id": 40, 'name': 'Музей петербургского авангарда', "url": 'https://ru.wikipedia.org/wiki/Музей_петербургского_авангарда'},
    {"id": 41, 'name': 'Государственный музей-институт семьи Рерихов', "url": 'https://ru.wikipedia.org/wiki/Рерих,_Николай_Константинович#Музей-институт_семьи_Рерихов_в_Санкт-Петербурге'},
    {"id": 42, 'name': 'Российский государственный музей Арктики и Антарктики', "url": 'https://ru.wikipedia.org/wiki/Российский_государственный_музей_Арктики_и_Антарктики'},
    {"id": 43, 'name': 'Ботанический музей Ботанического института им. В. Л. Комарова РАН', "url": 'https://ru.wikipedia.org/w/index.php?title=Ботанический_музей_БИН_РАН&action=edit&redlink=1'},
    {"id": 45, 'name': 'Музей Горного института', "url": 'https://ru.wikipedia.org/wiki/Санкт-Петербургский_государственный_горный_институт'},
    {"id": 46, 'name': 'Мемориальный Музей-квартира А.С.Пушкина', "url": 'https://ru.wikipedia.org/wiki/Музей-квартира_А._С._Пушкина_(наб._реки_Мойки,_12)'},
    {"id": 47, 'name': 'Музей-усадьба Г.Р.Державина', "url": 'https://ru.wikipedia.org/wiki/Музей-усадьба_Г.Р.Державина'},
    {"id": 48, 'name': 'Литературно-мемориальный музей Анны Ахматовой в Фонтанном Доме', "url": 'https://ru.wikipedia.org/wiki/Музей_Анны_Ахматовой_в_Фонтанном_доме'},
    {"id": 49, 'name': 'Мемориальный музей-квартира Л. Н. Гумилёва', "url": 'https://ru.wikipedia.org/wiki/Музей-квартира_Льва_Гумилёва'},
    {"id": 50, 'name': 'Государственный литературный музей «XX век»', "url": 'https://ru.wikipedia.org/wiki/Государственный_литературно-мемориальный_музей_М._М._Зощенко'},
    {"id": 51, 'name': 'Музей В.В. Набокова Факультета филологии и искусств Санкт-Петербургского государственного университета', "url": 'https://ru.wikipedia.org/wiki/Дом_Набокова'},
    {"id": 52, 'name': 'Музей-квартира А. А. Блока', "url": 'https://ru.wikipedia.org/wiki/Музей-квартира_А._А._Блока'},
    {"id": 53, 'name': 'Санкт-Петербургский государственный музей театрального и музыкального искусства', "url": 'https://ru.wikipedia.org/wiki/Санкт-Петербургский_государственный_музей_театрального_и_музыкального_искусства'},
    {"id": 54, 'name': 'Мемориальный музей-квартира Н. А. Римского-Корсакова', "url": 'https://ru.wikipedia.org/wiki/Музей-квартира_Н._А._Римского-Корсакова'},
    {"id": 55, 'name': 'Шереметевский дворец - Музей музыки', "url": 'https://ru.wikipedia.org/wiki/Фонтанный_дом'},
    {"id": 56, 'name': 'Музей циркового искусства при Большом Санкт-Петербургском цирке', "url": 'https://ru.wikipedia.org/wiki/Музей_циркового_искусства_(Санкт-Петербург)'},  

]
retriever = WikipediaRetriever(lang='ru', load_max_docs=2)
# chat_history = []

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
        # response_from_neural_network = llm_answer(museum_request.prompt, chat_history, qa)
        response_from_neural_network = llm_answer(museum_request.prompt, museum_request.name)


    return {"response": response_from_neural_network}
