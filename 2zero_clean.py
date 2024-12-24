import pandas as pd

# Загрузка данных из CSV-файла
file_path = 'validcleaned_file_without-missing.csv'  # Укажите путь к вашему CSV-файлу
data = pd.read_csv(file_path)

# Определяем порог значений
threshold = 0.1

# Создаем DataFrame без столбца 'target' для анализа
data_without_target = data.drop(columns=['target'], errors='ignore')

# Вычисляем долю значений, равных 0 для каждого столбца
zero_fraction = (data_without_target == 0).mean()

# Получаем список столбцов, которые нужно оставить
columns_to_keep = zero_fraction[zero_fraction < threshold].index.tolist()

# Проверяем, есть ли 'target' в исходных данных и добавляем его в список
if 'target' in data.columns:
    columns_to_keep.append('target')

# Оставляем только те столбцы
cleaned_data = data[columns_to_keep]

# Сохраняем очищенные данные в новый CSV-файл
cleaned_data.to_csv('vcleaned_file_without-zero.csv', index=False)

print("Столбцы с более чем 10% значениями 0 были удалены, но столбец 'target' остался.")
