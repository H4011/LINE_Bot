# -*- coding: utf-8 -*-
from re import A
from flask import *
from flask_httpauth import HTTPBasicAuth
from github import Github
from urllib.request import urlopen, quote
import urllib
import os
import datetime as dt
import requests
import jpholiday as jp
import random
import linecache as li
import json
import random
from bs4 import BeautifulSoup
try:
    from apiclient.discovery import build
    from apiclient.errors import HttpError
    error = "None"
except:
    error = "Import Error"

print(error)

from sqlalchemy import create_engine
import pandas as pd
import traceback
#import psycopg2

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, MessageAction, ImageSendMessage, TemplateSendMessage, ButtonsTemplate, FollowEvent, FlexSendMessage
)

app = Flask(__name__, static_folder='./templates')

#環境変数取得
LINE_CHANNEL_ACCESS_TOKEN = os.environ["LINE_CHANNEL_ACCESS_TOKEN"]
LINE_CHANNEL_SECRET = os.environ["LINE_CHANNEL_SECRET"]
GITHUB_ID = os.environ["Github_Token"]
USER = os.environ["User"]

#LINE_CHANNEL_ACCESS_TOKEN = "egG4K9fasMPMbaqnh7G7pln3omV7XCq9t5tcadwZHawCKq1qVQMEUpT8TzRlLdUpGpjxh2JkT5CpR+2LJFbDyBVQlvQi0gN0dJsn3e6iDQordeDqLEeGbvTlQW2ePpsiQSDIgEH5+3HSq669M8d9nAdB04t89/1O/w1cDnyilFU="
#LINE_CHANNEL_SECRET = "6a455d56489fea7ed9616d5cd4630926"
#GITHUB_ID = "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"
#USER = "https://raw.githubusercontent.com/H4011/kindaibot/master/userlist.txt"

line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(LINE_CHANNEL_SECRET)

"""
auth = HTTPBasicAuth()
id_list = {
    "user001": "password1111",
    "user002": "password1234"
}
@auth.get_password
def get_pw(id):
    if id in id_list:
        return id_list.get(id)
    return None
"""

def situmonn(word):
    word_list = ["教えて","何","なに","なんなん？","は？","なんやったっけ","なんやっけ"]
    tf = False
    for i in word_list:
        if i in word:
            tf = True
    return tf

def fukugou(word):
    result = ""
    for i in word.split(","):
        result += chr(int(i)-int(chr(53)))
    return ''.join(list(reversed(result)))

def jikanwari(AB, kamoku, ddow, ddow2, youbi = -1, jikan = -1, name = "unknow"):
    try:
        youbi = int(youbi)
    except:
        youbi = -1
    try:
        jikan = int(jikan)
    except:
        jikan = -1
    global AB_list
    if AB == "Aa" or AB == "Ab":
        AB_list = open('A.txt', 'r')
    elif AB == "Ba" or AB == "Bb":
        AB_list = open('B.txt', 'r')
    kamoku2 = AB_list.read()
    AB_list.close()
    kamoku2 = kamoku2.split("\n")
    kamoku3 = []
    kamoku4 = []
    kamoku5 = []
    for i in kamoku2:
        kamoku3.append(i.split(","))
    for i in kamoku3:
        for j in i:
            kamoku4.append(("+"+j).split("+"))
        kamoku5.append(kamoku4)
        kamoku4 = []
    you_jikannwari = [["","","","","","",""],["","","","","","",""],["","","","","","",""],["","","","","","",""],["","","","","","",""],["","","","","","",""],["","","","","","",""]]
    count = 0
    count2 = 0
    for i in kamoku.split(","):
        for j in i:
            try:
                you_jikannwari[count][count2] = kamoku5[count][count2][int(j)]
            except:
                you_jikannwari[count][count2] = ""
            count2 += 1
        count += 1
        count2 = 0
    result = ""
    youbi_list = ["月","火","水","木","金","土","KICS"]
    if(youbi == -1):
        count3 = 0
        result = name+"さんの時間割です。\nクラス："+AB+"\n\n"
        for i in you_jikannwari:
            count4 = 0
            if(count3 != 6):
                result += "【"+youbi_list[count3]+"曜日】\n"
            else:
                result += "【"+youbi_list[count3]+"】\n"
            result2 = ""
            result3 = ""
            for w in i:
                result2 += w
            for j in i:
                if(result2 == ""):
                    result3 += "授業はありません\n"
                    break
                elif(result2 != "" and j != '' and count3 != 6):
                    result3 += str(count4+1) + "時間目："+j+"\n"
                elif(result2 != "" and j == '' and count3 != 6):
                    result3 += str(count4+1) + "時間目：空き\n"
                elif(count3 == 6 and j != '' and result2 != ""):
                    result3 += "・"+j+"\n"
                count4 += 1
            result += result3+"\n"
            count3 += 1
        result = result[:-2]
    elif(jikan == -1 and 0 <= youbi <= 6):
        if(youbi != 6):
            count4 = 0
            result += name+"さんの"+youbi_list[youbi]+"曜日の時間割です。\nクラス："+AB+"\n\n"
            result2 = ""
            result3 = ""
            for i in you_jikannwari[youbi]:
                result2 += i
            for j in you_jikannwari[youbi]:
                if(result2 == ""):
                    result3 += "授業はありません\n"
                    break
                elif(result2 != "" and j != ''):
                    result3 += str(count4+1) + "時間目："+j+"\n"
                elif(result2 != "" and j == ''):
                    result3 += str(count4+1) + "時間目：空き\n"
                count4 += 1
            result += result3
        else:
            result += name+"さんが履修している"+youbi_list[youbi]+"です。\nクラス："+AB+"\n\n"
            result2 = ""
            result3 = ""
            for i in you_jikannwari[youbi]:
                result2 += i
            for j in you_jikannwari[youbi]:
                if(result2 == ""):
                    result3 += "授業はありません\n"
                    break
                elif(result2 != "" and j != ''):
                    result3 += "・"+j+"\n"
            result += result3
        result = result[:-1]
    elif(0 <= youbi <= 5 and 0 <= jikan <= 6):
        if(you_jikannwari[youbi][jikan] != ''):
            result = name+"さんの"+youbi_list[youbi]+"曜"+str(jikan+1)+"限目の科目は"+you_jikannwari[youbi][jikan]+"です。"
        else:
            result = name+"さんの"+youbi_list[youbi]+"曜"+str(jikan+1)+"限目の授業はありません。"
    elif(jikan == -1 and youbi == 7):
        if(ddow != 6):
            count4 = 0
            result += name+"さんの今日の時間割です。\nクラス："+AB+"\n\n"
            result2 = ""
            result3 = ""
            for i in you_jikannwari[ddow]:
                result2 += i
            for j in you_jikannwari[ddow]:
                if(result2 == ""):
                    result3 += "授業はありません\n"
                    break
                elif(result2 != "" and j != ''):
                    result3 += str(count4+1) + "時間目："+j+"\n"
                elif(result2 != "" and j == ''):
                    result3 += str(count4+1) + "時間目：空き\n"
                count4 += 1
            result += result3[:-1]
        else:
            result = "今日は日曜日なので授業はありません。"
    elif(jikan == -1 and youbi == 8):
        if(ddow2 != 6):
            count4 = 0
            result += name+"さんの明日の時間割です。\nクラス："+AB+"\n\n"
            result2 = ""
            result3 = ""
            for i in you_jikannwari[ddow2]:
                result2 += i
            for j in you_jikannwari[ddow2]:
                if(result2 == ""):
                    result3 += "授業はありません\n"
                    break
                elif(result2 != "" and j != ''):
                    result3 += str(count4+1) + "時間目："+j+"\n"
                elif(result2 != "" and j == ''):
                    result3 += str(count4+1) + "時間目：空き\n"
                count4 += 1
            result += result3[:-1]
        else:
            result = "明日は日曜日なので授業はありません。"
    else:
        if(ddow != 6):
            count4 = 0
            result += name+"さんの今日の時間割です。\nクラス："+AB+"\n\n"
            result2 = ""
            result3 = ""
            for i in you_jikannwari[ddow]:
                result2 += i
            for j in you_jikannwari[ddow]:
                if(result2 == ""):
                    result3 += "授業はありません\n"
                    break
                elif(result2 != "" and j != ''):
                    result3 += str(count4+1) + "時間目："+j+"\n"
                elif(result2 != "" and j == ''):
                    result3 += str(count4+1) + "時間目：空き\n"
                count4 += 1
            result += result3
        else:
            result = "日曜日なので授業はありません。"
    return result
    
@app.route("/templates/<path>", methods=["POST", "GET"])
def handle_t(path):
    pass
#    abort(403)

@app.route('/test', methods=["POST"])
def result_post():
    # POST送信の処理
    field = request.form["test"]
    a = open('test.txt', 'w')
    a.write(field)
    a.close()
    return ""

@app.route('/test2', methods=["GET"])
def result_post2():
    a = open('test.txt', 'r')
    b = a.read()
    a.close()
    return b

"""
@app.route("/teapot", methods=["POST", "GET"])
def handle_teapot():
    if request.method != 'GET':
        return { 'status' : 'I\'m a teapot.' }
    abort(418)

@app.route("/test", methods=["POST", "GET", "PUT", "DELETE"])
@auth.login_required
def handle_webhook3():
    return "Hello"

@app.errorhandler(401)
def page_not_found401(error):
    return render_template("401.html"), 401

def page_not_found403(error):
    url_403 = request.environ['PATH_INFO']
    if ".png" in url_403:
        sub = ".１２"
    else:
        sub = ""
    return render_template("403.html", sub=sub), 403

app.register_error_handler(403, page_not_found403)

@app.errorhandler(404)
def page_not_found404(error):
    return render_template("404.html"), 404

@app.errorhandler(405)
def page_not_found405(error):
    return render_template("405.html"), 405

def page_not_found410(error):
    return render_template('410.html'), 410

app.register_error_handler(410, page_not_found410)

def teapot(error):
    return render_template('418.html'), 418

app.register_error_handler(418, teapot)

@app.errorhandler(500)
def page_not_found500(error):
    return render_template("500.html"), 500

"""

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@app.route("/")
def hello():
    return "Hello, world!!"

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    try:
        #control_info = open('control.txt', 'r')
        #control_info2 = control_info.read()
        #control_info.close()
        #control = control_info2
        control = "True"
        #debug_info = open('debug_mode.txt', 'r')
        #debug_info2 = debug_info.read()
        #debug_info.close()
        #debug_mode = debug_info2
        dt_now = dt.datetime.now()
        dt_now2 = dt.datetime.now() + dt.timedelta(days=1)
        holiday = jp.is_holiday(dt.datetime.now())
        holiday2 = jp.is_holiday(dt.datetime.now() + dt.timedelta(days=1))
        dow = dt_now.strftime('%a')
        dow2 = dt_now2.strftime('%a')
        dow3 = dt_now.strftime('%a')
        dow4 = dt_now2.strftime('%a')
        dow = dow.replace('Mon','月').replace('Tue','火').replace('Wed','水').replace('Thu','木').replace('Fri','金').replace('Sat','土').replace('Sun','日')
        dow2 = dow2.replace('Mon','月').replace('Tue','火').replace('Wed','水').replace('Thu','木').replace('Fri','金').replace('Sat','土').replace('Sun','日')
        ddow = dow3.replace('Mon','0').replace('Tue','1').replace('Wed','2').replace('Thu','3').replace('Fri','4').replace('Sat','5').replace('Sun','6')
        ddow = int(ddow)
        ddow2 = dow4.replace('Mon','0').replace('Tue','1').replace('Wed','2').replace('Thu','3').replace('Fri','4').replace('Sat','5').replace('Sun','6')
        ddow2 = int(ddow2)
        day = dt_now.strftime('%Y年%m月%d日') + "(" + dow + ")"
        day2 = dt_now2.strftime('%Y年%m月%d日') + "(" + dow2 + ")"
        day3 = dt_now.strftime('%Y/%m/%d')
        h = int(dt_now.strftime('%H'))
        m = int(dt_now.strftime('%M'))
        time = dt_now.strftime('%H時%M分%S秒')
        time2 = dt_now.strftime('%H/%M/%S/')
        profile = line_bot_api.get_profile(event.source.user_id)
        Userid = str(event.source.user_id) #ユーザーのID
        User_Name = str(profile.display_name)
        url = USER
        html_text = requests.get(url).text
        soup = BeautifulSoup(html_text, 'html.parser')
        soup2 = str(soup).split("\n")
        User_tf = False
        AB = ""
        jikann = ""
        for i in soup2:
            w = i.split(" ")
            if len(w) == 3 and fukugou(w[0]) == Userid:
                User_tf = True
                AB = w[1]
                jikann = w[2]
                break
            elif len(w) != 3:
                continue

        try:
            if str(event.source.type) == "user":
                mode = "user"
            elif str(event.source.type) == "group":
                mode = "group"
            else:
                mode = "user"
        except:
            mode = "user"
        if "test " in event.message.text and control == "True" :
            """
            word = event.message.text
            error = "1"
            word = word.replace('test ','')
            error = "2"
            DATABASE_URL = os.environ.get('DATABASE_URL')
            error = "3"
            #engine = create_engine(DATABASE_URL, echo = False)
            error = "4"
            #df = pd.DataFrame([[day, time, word]], columns=['day', 'time', 'word'])
            error = "5"

            #df.to_sql('test', con = engine, if_exists='append')
            error = "6"
            with psycopg2.connect(DATABASE_URL) as conn:
                with conn.cursor() as curs:
                    curs.execute("INSERT INTO articles(time, word) VALUES(%s, %s)", (time, word))
            
            #word2 = engine.execute('SELECT * FROM test').fetchall()
            error = "7"
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=word))
            """
            pass
        elif "version" == event.message.text and control == "True" :
            replyText = "v1.0.0"
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=replyText))
        elif ("時間割" in event.message.text or ("授業" in event.message.text and "時間" not in event.message.text)) and situmonn(event.message.text) and "機能" not in event.message.text and "@判定除外" not in event.message.text and control == "True" :
            if ("今日" in event.message.text and User_tf and holiday == False):
                replyText = jikanwari(AB,jikann,ddow,ddow2,"7","",User_Name)
            elif ("明日" in event.message.text and User_tf and holiday2 == False):
                replyText = jikanwari(AB,jikann,ddow,ddow2,"8","",User_Name)
            elif ("曜" in event.message.text and User_tf):
                if("月曜" in event.message.text):
                    replyText = jikanwari(AB,jikann,ddow,ddow2,"0","",User_Name)
                elif("火曜" in event.message.text):
                    replyText = jikanwari(AB,jikann,ddow,ddow2,"1","",User_Name)
                elif("水曜" in event.message.text):
                    replyText = jikanwari(AB,jikann,ddow,ddow2,"2","",User_Name)
                elif("木曜" in event.message.text):
                    replyText = jikanwari(AB,jikann,ddow,ddow2,"3","",User_Name)
                elif("金曜" in event.message.text):
                    replyText = jikanwari(AB,jikann,ddow,ddow2,"4","",User_Name)
                elif("土曜" in event.message.text):
                    replyText = jikanwari(AB,jikann,ddow,ddow2,"5","",User_Name)
                elif("日曜" in event.message.text):
                    replyText = "日曜日の授業はありません。"
            elif (User_tf):
                replyText = jikanwari(AB,jikann,ddow,ddow2,"","",User_Name)
            elif holiday == True:
                replyText = day + "\n今日は祝日なので授業はありません！"
            elif holiday2 == True:
                replyText = day + "\n明日は祝日なので授業はありません！"
            else:
                replyText = "ユーザー登録がされていません"

            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=replyText))
        elif ("KICS" in event.message.text or "キックス" in event.message.text or "オンデマンド" in event.message.text) and situmonn(event.message.text) and "機能" not in event.message.text and "@判定除外" not in event.message.text and control == "True" :
            if (User_tf):
                replyText = jikanwari(AB,jikann,ddow,ddow2,"6","",User_Name)
            else:
                replyText = "ユーザー登録がされていません"

            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=replyText))
        elif "教えろ" in event.message.text and ("時間割" in event.message.text or "授業" in event.message.text or "機能" in event.message.text) and "@判定除外" not in event.message.text and "時間目" not in event.message.text and "限目" not in event.message.text and control == "True" :
            replyText = "無理です。"
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=replyText))
        elif "教えてくれてありがとう" in event.message.text and "@判定除外" not in event.message.text and "時間目" not in event.message.text and "限目" not in event.message.text and control == "True" :
            if(0 == random.randint(0,1)):
                replyText = "どういたしまして！"
                line_bot_api.reply_message(event.reply_token, TextSendMessage(text=replyText))
            else:
                replyText = "どいたま〜！"
                line_bot_api.reply_message(event.reply_token, TextSendMessage(text=replyText))
        elif "今何時" in event.message.text and "@判定除外" not in event.message.text and "時間目" not in event.message.text and "限目" not in event.message.text and control == "True" :
            replyText = time
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=replyText))
        elif "機能" in event.message.text and "教えて" in event.message.text and "@判定除外" not in event.message.text and "時間目" not in event.message.text and "限目" not in event.message.text and control == "True" :
            replyText = "時間割を教えることができます！"
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=replyText))
        elif "おはよ" in event.message.text and "時間割" not in event.message.text and "授業" not in event.message.text and "機能" not in event.message.text and "@判定除外" not in event.message.text and "時間目" not in event.message.text and "限目" not in event.message.text and control == "True" :
            if(0 == random.randint(0,1)):
                replyText = "おはよう〜！"
                line_bot_api.reply_message(event.reply_token, TextSendMessage(text=replyText))
            else:
                replyText = "おはよぉ...\n(( _ _ ))..zzzZZ"
                line_bot_api.reply_message(event.reply_token, TextSendMessage(text=replyText))
        elif ("こんにちは" in event.message.text or "こんちゃ" in event.message.text or "こんにちわ" in event.message.text) and "時間割" not in event.message.text and "授業" not in event.message.text and "機能" not in event.message.text and "@判定除外" not in event.message.text and "時間目" not in event.message.text and "限目" not in event.message.text and control == "True" :
            if(0 == random.randint(0,1)):
                replyText = "こんにちは〜"
                line_bot_api.reply_message(event.reply_token, TextSendMessage(text=replyText))
            else:
                replyText = "こんちゃ〜"
                line_bot_api.reply_message(event.reply_token, TextSendMessage(text=replyText))
        elif ("こんばんは" in event.message.text or "こんばんわ" in event.message.text) and "時間割" not in event.message.text and "授業" not in event.message.text and "機能" not in event.message.text and "@判定除外" not in event.message.text and "時間目" not in event.message.text and "限目" not in event.message.text and control == "True" :
            if(0 == random.randint(0,1)):
                replyText = "こんばんは！"
                line_bot_api.reply_message(event.reply_token, TextSendMessage(text=replyText))
            else:
                replyText = "こんばんは〜！！"
                line_bot_api.reply_message(event.reply_token, TextSendMessage(text=replyText))
        elif ("おやすみ" in event.message.text or "寝る" in event.message.text or "寝ます" in event.message.text) and "時間割" not in event.message.text and "授業" not in event.message.text and "機能" not in event.message.text and "@判定除外" not in event.message.text and "時間目" not in event.message.text and "限目" not in event.message.text and control == "True" :
            if(0 == random.randint(0,1)):
                replyText = "おやすみ！！\nまた、明日！"
                line_bot_api.reply_message(event.reply_token, TextSendMessage(text=replyText))
            else:
                replyText = "おやすみなさい〜！"
                line_bot_api.reply_message(event.reply_token, TextSendMessage(text=replyText))
        else:
            pass
                
    except:
        if control == "True":
            error_m = traceback.format_exc()
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=error_m))
        else:
            pass

if __name__ == "__main__":
    # app.run()
    port = int(os.getenv("PORT",5000))
    app.run(host="0.0.0.0", port=port)
