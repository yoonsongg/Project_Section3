import pandas as pd
import os 
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pickle
import joblib

url = os.getcwd() + '/' + 'data_csv' 

train = pd.read_csv(url + '/train.csv')
valid = pd.read_csv(url + '/valid.csv')

target = 'answerCode'
features = ['difficultyLevel', 'discriminationLevel', 'guessLevel', 'theta', 'realScore']
y_train = train[target]
X_train = train[features]

y_val = valid[target]
X_val = valid[features]

#X_train.values / X_train 의 차이. changed since warning
logistic = LogisticRegression()
logistic.fit(X_train.values, y_train.values)

#validation
y_pred = logistic.predict(X_val.values)
#print(accuracy_score(y_val.values, y_pred))

# visualization
# coefficients = pd.Series(logistic.coef_[0], X_train.columns)
# coefficients.sort_values().plot.barh()

test_case = [[2, 0, 2, -1, 1]]
# if logistic.predict(test_case) == 1:
#     print('Good Job')
# else:
#     print('You need a feedback')
# print(logistic.predict(test_case))

#모델 저장
joblib.dump(logistic, 'logistic.pkl')
#model loading & predict 
model = joblib.load('logistic.pkl')
# print(model.predict(test_case))



