#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
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
def getQnA(idPage,i):
    db = Database()
    urlQnA = "http://api.alobacsi.vn/qna/list/"+str(idPage)
    myResponse = requests.get(urlQnA)
    if(myResponse.ok):
        jDatas = json.loads(myResponse.content)
        print("The response contains {0} properties".format(len(jDatas)))
        print("\n")
        for jData in jDatas:
            # print(jData)
            if jData:
                x = jData["qnaId"]
                y = jData["name"]
                z = jData["question"]
                print ("answer =========")
                print ("answer =========")
                sz = jData["shortAnswer"]
                tmpA,qID  = getDetailQuestionByID(x)
                p = re.compile('<.*?>')
                a = re.sub(p, '', tmpA)
                p = re.compile('<table[^>]*>(?:.|\n?)')
                a = re.sub(p, '', a)
                # p = re.compile('(?.*)')
                a = re.sub(r"\s+", " ", a)
                # a = re.sub(p, '', a)
                a.strip()
                a.rstrip(os.linesep)

                # a = p.sub('',tmpA )

                print (a)
                # a = str(tmpA)
                # a.replace("</div>"," ")
                #
                # print (a)
                # soup = BeautifulSoup(tmpA)
                # result = soup.find("div")
                # # print (rel_soup.a['rel'])

                print ("answer =========")
                t = jData["title"]
                cat_ID = jData["cat_ID"]
                # query = "INSERT INTO dataTrain.QnA (`id`,`qnaId`,`name`,`question`,`answer`,`shortAnswer`,`title`,`cat_ID`) VALUES (%d, %d,'%s','%s','%s','%s','%s',%d)" % \
                #         (i, x ,y,z,a,sz,t,cat_ID) + ";\n"

                # f.write(query.encode('utf-8'))
                print (qID)
                sText = str(i) + " " + str(qID) + " " + a + "\n"
                anwserFile.write(sText.encode('utf-8'))
                # print (query)
                # db.insert(query)
                i = i + 1
    else:
    # If response code is not ok (200), print the resulting http error code with description
        myResponse.raise_for_status()
    return

def getFullQnA(idPage,i):
    db = Database()
    urlQnA = "http://api.alobacsi.vn/qna/list/"+str(idPage)
    myResponse = requests.get(urlQnA)
    if(myResponse.ok):
        jDatas = json.loads(myResponse.content)
        print("The response contains {0} properties".format(len(jDatas)))
        print("\n")
        for jData in jDatas:
            # print(jData)
            if jData:
                x = jData["qnaId"]
                y = jData["name"]
                z = jData["question"]
                sa= jData["shortAnswer"]
                t = jData["title"]
                cat_ID = jData["cat_ID"]
                query = "INSERT INTO dataTrain.QnA (`id`,`qnaId`,`name`,`question`,`shortAnswer`,`title`,`cat_ID`) VALUES (%d, %d,'%s','%s','%s','%s',%d)" % \
                        (i, x ,y,z,sa,t,cat_ID) + ";\n"
                print(query)
                fullQ.write(query.encode('utf-8'))
                # anwserFile.write(sText.encode('utf-8'))
                # print (query)
                # db.insert(query)
                i = i + 1
    else:
    # If response code is not ok (200), print the resulting http error code with description
        myResponse.raise_for_status()
    return

# get Category
def getCategory(url):
    db = Database()

    myResponse = requests.get(url)

    # For successful API call, response code will be 200 (OK)
    if(myResponse.ok):
        jDatas = json.loads(myResponse.content)
        i = 1
        for jData in jDatas:
            x = jData["catId"]
            y = jData["catName"]
            z = jData["catParentId"]
            # INSERT INTO `dataTrain`.`Category` (`id`, `catId`, `catName`, `type`) VALUES ('1', '12', 'ad', '0');
            #  query = "INSERT INTO `dataTrain`.`Category`(`id`,`catId`,`catName`,`catParentId`) " \
            # "VALUES(%s,%s)"
            # query = ('''INSERT INTO `dataTrain`.`Category` (`id`,`catId`,`catName`,`catParentId`) VALUES (%d,%d,%s,%d)''',(i,x,y,z))
            query = "INSERT INTO Category (`id`,`catId`,`catName`,`catParentId`) VALUES(%d, %d,'%s',%d)" % \
                        (i, x , y, z)
            print ("Query insert")
            print (query)
            db.insert(query)
            i = i + 1
    else:
    # If response code is not ok (200), print the resulting http error code with description
        myResponse.raise_for_status()
    return
#get sub category by Category ID
def getSubCategoryByID(cateID):
    urlSub = "http://api.alobacsi.vn/category/p/"+str(cateID)
    myResponse = requests.get(urlSub)

    # For successful API call, response code will be 200 (OK)
    if(myResponse.ok):
    # myResponse = requests.get(url,auth=HTTPDigestAuth(raw_input("username: "), raw_input("Password: ")), verify=True)
        jDatas = json.loads(myResponse.content)
        print("The response contains {0} properties".format(len(jDatas)))
        print("\n")
        for jData in jDatas:
            print(jData)
            print("ID :")
    else:
    # If response code is not ok (200), print the resulting http error code with description
        myResponse.raise_for_status()
    return
#get detail  by question ID
def getDetailQuestionByID(questionID):
    urlSub = "http://api.alobacsi.vn/qna/details/"+str(questionID)
    myResponse = requests.get(urlSub)

    # For successful API call, response code will be 200 (OK)
    if(myResponse.ok):
    # myResponse = requests.get(url,auth=HTTPDigestAuth(raw_input("username: "), raw_input("Password: ")), verify=True)
        jDatas = json.loads(myResponse.content)
        print("The response contains {0} properties".format(len(jDatas)))
        print("\n")
        # print(jDatas["answer"])
    else:
    # If response code is not ok (200), print the resulting http error code with description
        myResponse.raise_for_status()
    return  jDatas["answer"] ,jDatas["qnaId"]
# get record From DB and Save to file text
def getDataAndSave():
    db = Database()
    filfe = open('dataQnADisease.txt','w')
    # select_query = "select dataTrain.QnA.cat_ID from dataTrain.QnA group by  dataTrain.QnA.cat_ID"
    select_query = "select  dataTrain.QnA.cat_ID, dataTrain.QnA.title ,dataTrain.Diseases.cat_Name from dataTrain.QnA , dataTrain.Diseases where dataTrain.QnA.cat_ID = dataTrain.Diseases.cat_ID"
    dataCategory = db.query(select_query)
    i = 1
    for jData in dataCategory:
        print (i)
        i = i + 1
        # x = str(jData["title"])
        print(jData["title"])
        print(jData["cat_Name"])
        query = "INSERT INTO Category (`id`,`catId`,`catName`,`catParentId`) VALUES(%d, %s,'%d',%s)" % \
                (i,jData["title"],jData["cat_ID"],jData["cat_Name"]) + ";\n"
        filfe.write(query.encode('utf-8'))
        print (query)
    return

# get All Diseases
def getAllDisease(url):
    filfe = open('dataDisease.txt', 'w')
    myResponse = requests.get(url)
    # For successful API call, response code will be 200 (OK)
    if(myResponse.ok):
        jDatas = json.loads(myResponse.content)
        for jData in jDatas:
            x = jData["cat_ID"]
            y = jData["cat_Name"]
            query = "INSERT INTO Diseases (`cat_ID`,`cat_Name`) VALUES(%d,'%s')" % \
                 (x, y) + ";\n"
            print (query)
            filfe.write(query.encode('utf-8'))

    else:
    # If response code is not ok (200), print the resulting http error code with description
        myResponse.raise_for_status()
    return

#get list Question and Ansering
# urlQnA = "http://api.alobacsi.vn/qna/list/1"
# getQnA(urlQnA)
# #get List Category
# urlCategory = "http://api.alobacsi.vn/categories"
# getCategory(urlCategory)
#get List Sub Category By ID
# get ID from Catefory
#get QnA from FB
def getQnAFromDB():
    db = Database()
    fTilte = open('titleFileQuestion.txt', 'w')
    fShortAnser = open('shortQuestion.txt', 'w')
    fAnser = open('answerFile.txt', 'w')

    # select_query = "select dataTrain.QnA.cat_ID from dataTrain.QnA group by  dataTrain.QnA.cat_ID"
    select_query = "select dataTrain.QnA.title , dataTrain.QnA.shortAnswer from dataTrain.QnA"
    dataCategory = db.query(select_query)
    tmp  = 1
    for jData in dataCategory:
        print (i)
        tmp = tmp + 1
        # print(jData["shortAnswer"])
        sText = str(tmp) +" " + jData["shortAnswer"] + "\n"
        fShortAnser.write(sText.encode('utf-8'))
        # print (tmp)
    return
i = 1
# anwserFile = open('anwserFile.txt','w')
def getFullTitleQuestion():
    db = Database()
    fileTitleQuestion = open('titleFullQnA.txt','w')
    select_query = "select dataTrain.QnA.title  from dataTrain.QnA"
    dataCategory = db.query(select_query)
    tmp  = 1
    for jData in dataCategory:
        print (i)
        # print(jData["shortAnswer"])
        sText = str(tmp) +" " + jData["title"] + "\n"
        print (sText)
        fileTitleQuestion.write(sText.encode('utf-8'))
        tmp = tmp + 1

        # print (tmp)
    return
def getFullTitleQuestion2():
    db = Database()
    fileTitleQuestion = open('titleFullQnAver2.txt','w')
    select_query = "select dataTrain.QnA.title  from dataTrain.QnA"
    dataCategory = db.query(select_query)
    tmp  = 1
    for jData in dataCategory:
        print (i)
        # print(jData["shortAnswer"])
        sText = jData["title"] + "\n"
        print (sText)
        fileTitleQuestion.write(sText.encode('utf-8'))
        tmp = tmp + 1

        # print (tmp)
    return
fullQ = open('fullQuestion.txt','w')

# read XML file


if __name__ == "__main__":
    getFullTitleQuestion2()
    # urlCategory = "http://api.alobacsi.vn/categories"
    # # getCategory(urlCategory)
    # f = open('dataTrain.txt', 'w')
    # for x in range(1, 2150):
    #     print ("-------------")
    #     print (x)
    #     print ("----------------")
    #     if x > 1:
    #         getFullQnA(x,i = 15*(x-1))
    #     else:
    #         getFullQnA(x,i)

    # getDataAndSave()
    # getAllDisease("http://api.alobacsi.vn/category/diseases")

    # getQnAFromDB()
    # getDataAndSave()

