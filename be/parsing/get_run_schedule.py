import time
from get_rus_museum import get_rus_museum
from get_hermitage import get_hermitage
from get_faberzhe import get_faberzhe
from get_summer_garden import get_summer_garden
from get_state_museum_of_urban_sculpture import get_state_museum_of_urban_sculpture
from get_museum_apartment_of_kuindzhi import get_museum_apartment_of_kuindzhi
from get_erarta import get_erarta

# По расприсанию через определенный интервал времени будет вызываться эта функция
# для обновления данных с сайта и записи их в каталог parsing/data

def run_schedule(interval):
    try:
        while True:
            print("Starting the parsing process.")
            rus_museum_path = get_rus_museum()
            hermitage_path = get_hermitage()
            faberzhe_path = get_faberzhe()
            summer_garden_path = get_summer_garden()
            state_museum_of_urban_sculpture_path = get_state_museum_of_urban_sculpture()
            museum_apartment_of_kuindzhi_path = get_museum_apartment_of_kuindzhi()
            erarta_path = get_erarta()
            if rus_museum_path:
                print(f'Data was successfully saved to {rus_museum_path}')
            if hermitage_path:
                print(f'Data was successfully saved to {hermitage_path}')
            if faberzhe_path:
                print(f'Data was successfully saved to {faberzhe_path}')
            if summer_garden_path:
                print(f'Data was successfully saved to {summer_garden_path}')
            if state_museum_of_urban_sculpture_path:
                print(f'Data was successfully saved to {state_museum_of_urban_sculpture_path}')
            if museum_apartment_of_kuindzhi_path:
                print(f'Data was successfully saved to {museum_apartment_of_kuindzhi_path}')
            if erarta_path
                print(f'Data was successfully saved to {erarta_path}')
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
