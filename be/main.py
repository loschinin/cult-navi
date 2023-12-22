import pandas as pd
from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from langchain.retrievers import WikipediaRetriever
from langchain.chat_models.gigachat import GigaChat
# from langchain.chains import ConversationalRetrievalChain
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from fastapi.responses import JSONResponse

from museums_list import museums_list

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


retriever = WikipediaRetriever(lang='ru', load_max_docs=2)
# chat_history = []

@app.get("/museums")
async def get_museums():
    # На клиент отправляется только список с названиями музеев
    museum_names = [museum['name'] for museum in museums_list]
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

#     print(museum_data)

    context = museum_data

    # Отправка запроса к нейронной сети
    # response_from_neural_network = await query_neural_network(context, museum_request.prompt)

    if museum_request.name == '':
       response_from_neural_network = 'Пожалуйста, выберите музей из списка наверху.'
    else:
        try:
            # response_from_neural_network = llm_answer(museum_request.prompt, chat_history, qa)
            response_from_neural_network = llm_answer(museum_request.prompt, museum_request.name)
            print(response_from_neural_network)
        except Exception as e:
                # Логирование исключения для отладки
                print(f"An error occurred: {e}")
                # Возвращение ответа с ошибкой клиенту
                return JSONResponse(status_code=500, content={"message": "Sorry. Something went wrong. We are working on fixing it."})


    return {"response": response_from_neural_network}
