from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

import asyncio
# Допустим, у вас есть функция для взаимодействия с базой данных и нейронной сетью
# from .database import get_museum_context
# from .neural_network import query_neural_network

app = FastAPI()

# решаем проблему с CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Разрешает все источники
    allow_credentials=True,
    allow_methods=["*"],  # Разрешает все методы
    allow_headers=["*"],  # Разрешает все заголовки
)

class MuseumRequest(BaseModel):
    museum_name: str
    prompt: str

@app.get("/museums")
async def get_museums():
    # Здесь должен быть код для получения списка музеев из базы данных, а пока их просто захардкодим
    museums = ["Государственный Эрмитаж", "Музей Фаберже", "Государственный Русский музей", "Летний сад", "Государственный музей городской скульптуры", "Музей-усадьба П. П. Чистякова", "Музей-квартира А. И. Куинджи", "Музей современного искусства Эрарта", "Новый музей", "Музей прикладного искусства СПбГХПА им.А.Л.Штиглица"]
    return museums

@app.post("/query")
async def query_museum(museum_request: MuseumRequest):
    # Получение контекста музея
    context = await get_museum_context(museum_request.museum_name)
    if not context:
        raise HTTPException(status_code=404, detail="Museum not found")

    # Отправка запроса к нейронной сети
    response = await query_neural_network(context, museum_request.prompt)

    return {"response": response}
