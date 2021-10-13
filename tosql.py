import os
import sqlite3
import csv

DB_FILENAME = 'DB_data.db'
DB_FILEPATH = os.path.join(os.getcwd(), DB_FILENAME)

conn = sqlite3.connect('DB_data.db')
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS grade7_itemIRT_train;")
cur.execute("DROP TABLE IF EXISTS grade7_learnerIRT_train;")
cur.execute("DROP TABLE IF EXISTS grade7_correct_train;")

cur.execute("""CREATE TABLE grade7_itemIRT_train (
    testID VARCHAR(12),
    assessmentItemID VARCHAR(12),
    difficultyLevel NUMERIC,
    discriminationLevel NUMERIC,
    guessLevel NUMERIC,
    knowledgeTag VARCHAR(5),
    FOREIGN KEY(testID) REFERENCES grade7_correct_train(testID),
    FOREIGN KEY(assessmentItemID) REFERENCES grade7_correct_train(assessmentItemID)
);""")

cur.execute("""CREATE TABLE grade7_learnerIRT_train (
    learnerID VARCHAR(12),
    testID VARCHAR(12),
    theta NUMERIC,
    realScore NUMERIC,
    FOREIGN KEY(testID) REFERENCES grade7_correct_train(testID),
    FOREIGN KEY(learnerID) REFERENCES grade7_correct_train(learnerID)
);""")

cur.execute("""CREATE TABLE grade7_correct_train(
    learnerID VARCHAR(12),
    testID VARCHAR(12),
    assessmentItemID VARCHAR(12),
    answerCode INTEGER
    );""")

#valid dataset create table
cur.execute("""CREATE TABLE grade7_itemIRT_valid (
    testID VARCHAR(12),
    assessmentItemID VARCHAR(12),
    difficultyLevel NUMERIC,
    discriminationLevel NUMERIC,
    guessLevel NUMERIC,
    knowledgeTag VARCHAR(5),
    FOREIGN KEY(testID) REFERENCES grade7_correct_valid (testID),
    FOREIGN KEY(assessmentItemID) REFERENCES grade7_correct_valid (assessmentItemID)
);""")

cur.execute("""CREATE TABLE grade7_learnerIRT_valid (
    learnerID VARCHAR(12),
    testID VARCHAR(12),
    theta NUMERIC,
    realScore NUMERIC,
    FOREIGN KEY(testID) REFERENCES grade7_correct_valid (testID),
    FOREIGN KEY(learnerID) REFERENCES grade7_correct_valid (learnerID)
);""")

cur.execute("""CREATE TABLE grade7_correct_valid(
    learnerID VARCHAR(12),
    testID VARCHAR(12),
    assessmentItemID VARCHAR(12),
    answerCode INTEGER
    );""")





# filepath = os.path.join(os.getcwd(), "data_csv/grade7_itemIRT_train.csv")
# item_file = open(filepath, 'r')
# item_rows = csv.reader(item_file)
# cur.executemany("INSERT INTO grade7_itemIRT_train VALUES (?, ?, ?, ?, ?, ?)", item_rows)


# cur.commit()
# cur.close()