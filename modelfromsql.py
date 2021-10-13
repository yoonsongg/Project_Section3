import sqlite3
import pandas as pd
import os
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pickle
import joblib

DB_FILENAME = 'DB_data.db'
DB_FILEPATH = os.path.join(os.getcwd(), DB_FILENAME)

conn = sqlite3.connect('DB_data.db')
cur = conn.cursor()

# query = cur.execute("SELECT * FROM grade7_itemIRT_train")
# cols = [column[0] for column in query.description]
# result = pd.DataFrame.from_records(data=query.fetchall(), columns=cols)

# from a sql databse to make a dataframe (train / valid )
class Fromsql():
    def __init__(self, name):
        self.name = name
        #query = self.query
        #cols = self.cols
        pass
    def make_df(self, name):
        query = cur.execute(f"SELECT * FROM grade7_itemIRT_{name}")
        cols = [column[0] for column in query.description]
        itemIRT = pd.DataFrame.from_records(data=query.fetchall(), columns=cols)
        
        query = cur.execute(f"SELECT * FROM grade7_learnerIRT_{name}")
        cols = [column[0] for column in query.description]
        learnerIRT = pd.DataFrame.from_records(data=query.fetchall(), columns=cols)

        query = cur.execute(f"SELECT * FROM grade7_correct_{name}")
        cols = [column[0] for column in query.description]
        correct = pd.DataFrame.from_records(data=query.fetchall(), columns=cols)
        
        return itemIRT, learnerIRT, correct
    
    def merge_df(self, name):
        itemIRT, learnerIRT, correct  = self.make_df(name) 
        second_df = pd.merge(left = correct, right = itemIRT, how = 'left', on = ['testID', 'assessmentItemID'])
        final_df = pd.merge(left = second_df, right = learnerIRT, how = 'left', on = ['testID', 'learnerID'])
        
        return final_df

#Dataframe 생성
a = Fromsql('train')
train = a.merge_df('train')

b = Fromsql('valid')
valid = b.merge_df('valid')

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
#print(accuracy_score(y_val.values, y_pred)) #0.8099

# visualization
# coefficients = pd.Series(logistic.coef_[0], X_train.columns)
# coefficients.sort_values().plot.barh()

#test case 실험
#test_case = [[2, 0, 2, -1, 1]]
# if logistic.predict(test_case) == 1:
#     print('Good Job')
# else:
#     print('You need a feedback')
# print(logistic.predict(test_case))

#모델 저장
joblib.dump(logistic, './Server/model/logistic.pkl')
#model loading & predict 
#model = joblib.load('logistic.pkl')
# print(model.predict(test_case))






