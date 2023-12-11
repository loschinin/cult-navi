def get_museum_context(file_path):
    # Пытаемся открыть и прочитать файл
    context = ""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            context = file.read()
    except FileNotFoundError:
        context = "Файл не найден."
    except Exception as e:
        context = f"Произошла ошибка: {e}"

    return context