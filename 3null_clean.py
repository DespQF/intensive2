import pandas as pd

# Загрузка данных из CSV-файла
file_path = 'vcleaned_file_without-zero.csv'  # Укажите путь к вашему CSV-файлу
data = pd.read_csv(file_path)

# Определяем порог пропусков
threshold = 0.1

# Вычисляем долю пропусков для каждой строки
missing_fraction = data.isnull().mean(axis=1)

# Удаляем строки, где доля пропусков больше 10%
cleaned_data = data[missing_fraction <= threshold]

# Сохраняем очищенные данные в новый CSV-файл
cleaned_data.to_csv('vcleaned_file_level3.csv', index=False)

print("Строки с более чем 10% значениями null были удалены.")
