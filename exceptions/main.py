import csv


def parse_parameters():
    """Функция для ввода параметров из консоли."""
    params = {}
    print("Введите параметры (напр. file=input.csv или rows=3). Нажмите Ctrl+D для завершения ввода:")
    try:
        while True:
            line = input().strip()
            if "=" in line:
                key, value = line.split("=", 1)
                params[key.strip()] = value.strip()
    except EOFError:
        pass

    # Установка значений по умолчанию
    params.setdefault("f", "input.csv")
    return params


def validate_parameters(params):
    """Проверка параметров на корректность."""
    errors = []

    # Проверяем наличие числовых параметров
    for param in ["n", "rows", "cols", "m"]:
        if param in params:
            try:
                params[param] = int(params[param])
            except ValueError:
                errors.append(f"Параметр {param} должен быть целым числом.")
        else:
            errors.append(f"Отсутствует обязательный параметр {param}.")

    # Проверка имени файла
    if "f" not in params or not params["f"].endswith(".csv"):
        errors.append("Параметр 'f' (file) должен указывать на файл с расширением .csv.")

    # Проверка предметов
    if "items" in params:
        items = params["items"].split(";")
        items = [item.strip() for item in items if item.strip()]  # Убираем пустые строки и пробелы
        if len(items) != params.get("m", len(items)):  # Сравниваем количество предметов с m
            errors.append(
                f"Количество предметов ({len(items)}) не совпадает с заявленным параметром 'm' ({params['m']})."
            )
        params["items"] = items
    else:
        if "m" in params and params["m"] > 0:
            errors.append("Список предметов ('items') не указан, но параметр 'm' больше 0.")
        params["items"] = []

    return errors


def read_csv(file_name):
    """Чтение данных из CSV-файла."""
    try:
        with open(file_name, newline='', encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile)
            return [row for row in reader]
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл {file_name} не найден.")
    except Exception as e:
        raise Exception(f"Ошибка при чтении файла {file_name}: {e}")


def validate_csv_data(data, rows, cols):
    """Проверка содержимого CSV-файла на соответствие."""
    errors = []
    if len(data) != rows:
        errors.append(f"Ожидалось {rows} рядов, но найдено {len(data)}.")
    for i, row in enumerate(data):
        if len(row) != cols:
            errors.append(f"В ряде {i + 1} ожидалось {cols} колонок, но найдено {len(row)}.")
    return errors


def pigeonhole_principle(n, m):
    """Формулировка принципа Дирихле."""
    if m > n:
        return f"Если в {n} ящиках лежит {m} предметов, то хотя бы в одном ящике лежит не менее {m // n + 1} предметов."
    elif m < n:
        return f"Если в {n} ящиках лежит {m} предметов, то пустых ящиков как минимум {n - m}."
    else:
        return f"Если в {n} ящиках лежит {m} предметов, то в каждом ящике лежит ровно 1 предмет."


def main():
    # Ввод и парсинг параметров
    params = parse_parameters()

    # Проверка параметров
    errors = validate_parameters(params)
    if errors:
        print("Ошибки параметров:")
        print("\n".join(errors))
        return

    # Чтение данных из CSV-файла
    try:
        csv_data = read_csv(params["f"])
    except Exception as e:
        print(e)
        return

    # Проверка данных CSV
    csv_errors = validate_csv_data(csv_data, params["rows"], params["cols"])
    if csv_errors:
        print("Ошибки в содержимом CSV-файла:")
        print("\n".join(csv_errors))
        return

    # Формулировка принципа Дирихле
    result = pigeonhole_principle(params["n"], params["m"])
    print(result)


if __name__ == "__main__":
    main()

# file=input.csv
# rows=3
# cols=4
# n=6
# m=8
# items=игрушка,коробка с карандашами,свечка,лего,кукла,свитер с оленями,мячик,расчёска
