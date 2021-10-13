# Project_Section3
project

1) download data
2) data 압축 해제
3) tomongoDB.py 실행
4) mac terminal 입력 : `mongoexport --uri mongodb+srv://whaleuser:song0909@cluster0.bvo67.mongodb.net/Project3 --collection grade7_correct_valid --type csv --fields learnerID,testID,assessmentItemID,answerCode --out ./grade7_correct_valid.csv` 
5) tosql.py 실행
6) modelfromsql.py 실행
7) server파일의 app.py 실행 -> API 서비스
8) dashboard 
- docker 실행 image- metabase
