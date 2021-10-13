# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
import joblib

app = Flask(__name__)


# 저장된 모델을 세션에 적용합니다.
save_path = "./model/logistic.pkl"
model = joblib.load(save_path)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        # 파라미터를 전달 받습니다.
        difficultyLevel = float(request.form['difficultyLevel'])
        guessLevel = float(request.form['guessLevel'])
        theta = float(request.form['theta'])
        realScore = float(request.form['realScore'])

     
        discriminationLevel = 0

        # 입력된 파라미터를 배열 형태로 준비합니다.
        input_data = [[difficultyLevel, discriminationLevel, guessLevel, theta, realScore]]
       

        # 입력 값을 토대로 예측 값을 찾아냅니다.
        
        result = model.predict(input_data)
        if result == 1:
            result = '문제를 맞출 가능성이 높습니다'
        else:
            result = '문제를 틀릴 가능성이 높습니다'
            
        
        return render_template('index.html', price=result)

if __name__ == '__main__':
   app.run(debug = True)