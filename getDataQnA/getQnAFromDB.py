import requests
from requests.auth import HTTPDigestAuth
import json
import mysql.connector
import MySQLdb
import os,sys
from bs4 import BeautifulSoup
from bs4 import Tag
import codecs
import re

class Database:

    host = 'localhost'
    user = 'root'
    password = 'root'
    db = 'dataTrain'

    def __init__(self):
        self.connection = MySQLdb.connect(self.host, self.user, self.password, self.db,use_unicode=1,charset="utf8")
        self.cursor = self.connection.cursor()

    def insert(self, query):
        try:
            self.cursor.execute(query)
            self.connection.commit()
        except:
            self.connection.rollback()

    def query(self, query):
        cursor = self.connection.cursor( MySQLdb.cursors.DictCursor )
        cursor.execute(query)

        return cursor.fetchall()

    def __del__(self):
        self.connection.close()
#get QnA from FB
def getQnAFromDB():
    db = Database()
    question = open('titleQuestionFile.txt','w')

    # select_query = "select dataTrain.QnA.cat_ID from dataTrain.QnA group by  dataTrain.QnA.cat_ID"
    select_query = "select dataTrain.QnA.qnaId, dataTrain.QnA.title , dataTrain.QnA.shortAnswer from dataTrain.QnA"
    dataCategory = db.query(select_query)
    tmp  = 1
    for jData in dataCategory:
        
        # print(jData["shortAnswer"])
        sText = str(tmp) +" " + str(jData["qnaId"]) + " "+ jData["title"] + "\n"
        print(sText)
        question.write(sText.encode('utf-8'))
        tmp = tmp + 1
        # print (tmp)
    return

getQnAFromDB()

