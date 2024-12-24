import pandas as pd

# Загрузка данных из CSV файла
file_path = 'vcleaned_data_without-one.csv'  # Укажите путь к вашему CSV файлу
df = pd.read_csv(file_path)

# Функция для преобразования текстовых столбцов в float
def convert_columns_to_float(df):
    for column in df.columns:
        try:
            # Пробуем преобразовать столбец в float
            df[column] = df[column].astype(float)
        except ValueError:
            # Если возникает ошибка, столбец не может быть преобразован
            print(f"Столбец '{column}' не может быть преобразован в float.")
    return df

# Применяем функцию
df_converted = convert_columns_to_float(df)

# Выводим результат
print(df_converted)

# Сохраняем преобразованные данные в новый CSV файл (если нужно)
df_converted.to_csv('vconverted_data_to_float.csv', index=False)

