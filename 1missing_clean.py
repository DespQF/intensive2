import pandas as pd

# Загрузка данных из CSV-файла
file_path = 'valid.csv'  # Укажите путь к вашему CSV-файлу
data = pd.read_csv(file_path)

# Определяем порог пропусков
threshold = 0.1

# Вычисляем долю пропусков для каждого столбца
missing_fraction = data.isnull().mean()

# Оставляем только те столбцы, где доля пропусков меньше или равна 70%
cleaned_data = data.loc[:, missing_fraction <= threshold]

# Сохраняем очищенные данные в новый CSV-файл
cleaned_data.to_csv('validcleaned_file_without-missing.csv', index=False)

print("Столбцы с более чем 90% пропусков были удалены.")
