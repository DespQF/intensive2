import pandas as pd

# Загрузка данных из CSV файла
file_path = 'vcleaned_file_level3.csv'  # Укажите путь к вашему CSV файлу
df = pd.read_csv(file_path)


# Функция для удаления столбцов с более чем 10% значений равных 1.0
def drop_columns_with_high_one_percentage(df, threshold=0.3):
    # Определяем количество строк в DataFrame
    total_rows = df.shape[0]

    # Находим столбцы, которые нужно удалить
    columns_to_drop = []
    for column in df.columns:
        # Вычисляем процент значений равных 1.0
        percentage_of_ones = (df[column] == 1.0).mean()
        if percentage_of_ones > threshold:
            columns_to_drop.append(column)
            print(f"Столбец '{column}' будет удален (процент 1.0: {percentage_of_ones * 100:.2f}%)")

    # Удаляем столбцы
    df.drop(columns=columns_to_drop, inplace=True)
    return df


# Применяем функцию
df_cleaned = drop_columns_with_high_one_percentage(df)

# Выводим результат
print(df_cleaned)

# Сохраняем очищенные данные в новый CSV файл (если нужно)
df_cleaned.to_csv('vcleaned_data_without-one.csv', index=False)

