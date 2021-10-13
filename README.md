# Project_Section3
project

1) download data
2) data 압축 해제
3) tomongoDB.py 실행
4) mac terminal에 입력 / 수정하여 6개의 csv 만들기
 `mongoexport --uri mongodb+srv://whaleuser:song0909@cluster0.bvo67.mongodb.net/Project3 --collection grade7_correct_valid --type csv --fields learnerID,testID,assessmentItemID,answerCode --out ./grade7_correct_valid.csv` 
6) tosql.py 실행 / dbeaver에서 csv import
7) modelfromsql.py 실행
8) server 폴더의 app.py 실행 -> API 서비스
9) dashboard 
- docker 실행 image- metabase
