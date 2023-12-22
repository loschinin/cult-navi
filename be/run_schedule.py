import time
import pandas as pd
from get_data import get_data

from museums_list import museums_list

# По расприсанию через определенный интервал времени будет вызываться эта функция

def run_schedule(interval):
    try:
        while True:
            print("Starting the parsing process.")

            # Создайте DataFrame для хранения результатов
            df = pd.DataFrame(columns=["id", "name", "data"])

            # Перебор информации о музеях и парсинг данных
            for museum in museums_list:
                museum_data = get_data(museum['url'])
                if museum_data:
                    # Добавление результатов в DataFrame
                    df = df._append({"id": museum["id"], "name": museum["name"], "data": museum_data}, ignore_index=True)
                    print(f'Data was successfully saved for {museum["name"]}')
                else:
                    print(f'Failed to save data for {museum["id"]}')

            # Сохранение DataFrame в CSV файл
            df.to_csv('./museums_data.csv', index=False, encoding='utf-8')
            print("All data has been saved to museums_data.csv")

            print(f"Waiting for {interval} seconds.")
            time.sleep(interval)

    except KeyboardInterrupt:
        print("Stopped the scheduled parsing.")


# Интервал в секундах (1 месяц)
interval = int(1 * 30.44 * 24 * 60 * 60)

# Запуск функции с интервалом.
run_schedule(interval)
