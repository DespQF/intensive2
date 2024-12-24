import pandas as pd

# Загрузка данных из CSV-файла
file_path = 'vconverted_data_to_float.csv'  # Укажите путь к вашему CSV-файлу
data = pd.read_csv(file_path)

# Функция для подсчета совпадений значений между строками
def count_matches(row, df):
    return (df == row).sum(axis=1)

# Создаем маску для удаления строк
rows_to_drop = []

for index, row in data.iterrows():
    match_count = count_matches(row, data)
    # Удаляем текущую строку из подсчета совпадений
    match_count = match_count.drop(index)
    if (match_count > 10).any():  # Если есть строка с более чем 10 совпадениями
        rows_to_drop.append(index)

# Удаляем строки из DataFrame
cleaned_data = data.drop(index=rows_to_drop)

# Сохраняем очищенные данные в новый CSV-файл
cleaned_data.to_csv('vcleaned_file_without_duplicates.csv', index=False)

print("Строки с более чем 10 совпадениями были удалены.")
