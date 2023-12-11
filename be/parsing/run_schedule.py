import time
from get_rus_museum import get_rus_museum
from get_hermitage import get_hermitage
from get_faberzhe import get_faberzhe

# По расприсанию через определенный интервал времени будет вызываться эта функция
# для обновления данных с сайта и записи их в каталог parsing/data

def run_schedule(interval):
    try:
        while True:
            print("Starting the parsing process.")
            rus_museum_path = get_rus_museum()
            hermitage_path = get_hermitage()
            faberzhe_path = get_faberzhe()
            if rus_museum_path:
                print(f'Data was successfully saved to {rus_museum_path}')
            if hermitage_path:
                print(f'Data was successfully saved to {hermitage_path}')
            if faberzhe_path:
                print(f'Data was successfully saved to {faberzhe_path}')
            else:
                print('Failed to save data.')
            print(f"Waiting for {interval} seconds.")
            time.sleep(interval)
    except KeyboardInterrupt:
        print("Stopped the scheduled parsing.")


# Интервал в секундах (1 месяц)
interval = int(1 * 30.44 * 24 * 60 * 60)

# Запуск функции с интервалом.
run_schedule(interval)
