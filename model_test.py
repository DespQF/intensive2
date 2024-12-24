
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
import matplotlib.pyplot as plt
import pandas as pd

# Загрузка данных
file_path1 = 'vcleaned_file_without_duplicates.csv'
valid = pd.read_csv(file_path1)
file_path = 'cleaned_file_without_duplicates.csv'
train = pd.read_csv(file_path)

# Загрузка Train
X_train = train.drop(columns='target')
y_train = train['target']
X_test = valid.drop(columns='target')
y_test = valid['target']

# инициализация и обучение модели
rf_classifier = RandomForestClassifier(min_samples_leaf=5, n_estimators=100, random_state=384)
rf_classifier.fit(X_train, y_train)

# предсказание вероятностей
y_pred_proba = rf_classifier.predict_proba(X_test)[:,1]

fpr, tpr, _ = metrics.roc_curve(y_test,  y_pred_proba)

# построение ROC кривой
plt.plot(fpr, tpr)
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.savefig('ROC.png')

auc = metrics.roc_auc_score(y_test, y_pred_proba)
print("AUC: %.3f" % auc)

