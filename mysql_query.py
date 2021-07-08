import pymysql as MySQLdb
import mysql_connection
import datetime
import time
import os
import cv2

def getPlate(connection):
    sql = "SELECT * FROM plate WHERE check_status=0"
    cursor = connection.cursor()
    cursor.execute(sql)
    result_set = cursor.fetchall()
    for record in result_set:
        print(record)
        print(record[2])
        print(datetime.datetime.strptime(str(record[6]), '%Y-%m-%d %H:%M:%S').strftime("%d-%m-%Y %H:%M:%S"))

def addPlate(connection):
    cardNumber = 34567
    plateNumber = "abcd"
    now = time.localtime()
    current_time = time.strftime('%Y-%m-%d %H:%M:%S', now)
    img_raw = cv2.imread("aa.jpg") ##anh de demo

    image_name = str(cardNumber) +"-"+ plateNumber + "-" + str(round(time.time() * 1000))
    path_image_raw = "img_raw/"+ image_name +".jpg"
    path_image_plate = "img_plate/" + image_name +".jpg"
    if(os.path.exists("img_raw")):
        print("folder exsist")
        cv2.imwrite(path_image_raw , img_raw)
    else:
        os.mkdir("img_raw")
        cv2.imwrite(path_image_raw , img_raw)

    if (os.path.exists("img_plate")):
        print("folder exsist")
        cv2.imwrite(path_image_plate , img_raw)
    else:
        os.mkdir("img_plate")
        cv2.imwrite(path_image_plate , img_raw)

    cursor = connection.cursor()
    sql = ("INSERT INTO plate(number_card, plate_number, img_plate, img_raw, check_status, time_in)"
           + "VALUES (%s, %s, %s, %s, %s, %s)")

    value = (cardNumber, plateNumber, path_image_plate, path_image_raw, 0, current_time)

    try:
        cursor.execute(sql, value)
        connection.commit()
        print("ok")
    except:
        connection.rollback()
        os.remove(path_image_raw)
        os.remove(path_image_plate)

def updatePlate(connection):
    numberCard = 34567
    now = time.localtime()
    current_time = time.strftime('%Y-%m-%d %H:%M:%S', now)
    sql = ("UPDATE plate SET check_status = %s, time_out = %s WHERE number_card = %s")
    value = (1, current_time, numberCard)
    cursor = connection.cursor()
    try:
        cursor.execute(sql, value)
        connection.commit()
        print("ok")
    except:
        connection.rollback()

def findPlate(connection):
    stringFind = "123"
    sql = "SELECT * FROM plate WHERE number_card LIKE '%"+stringFind+"%' OR plate_number LIKE '%"+stringFind+"%'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result_set = cursor.fetchall()
    for record in result_set:
        print(record)
        print(record[2])
        print(datetime.datetime.strptime(str(record[6]), '%Y-%m-%d %H:%M:%S').strftime("%d-%m-%Y %H:%M:%S"))

connection = mysql_connection.connection()
# getPlate(connection)
addPlate(connection)
# updatePlate(connection)
# findPlate(connection)
