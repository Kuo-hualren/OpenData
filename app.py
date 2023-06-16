# import requests
import time
import os
import json
from flask import Flask, render_template, url_for, redirect, session, request
from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate   要用記得要解掉註解
from datetime import datetime
import bcrypt
import functools
import itertools

url = 'https://www.twtainan.net/data/attractions_zh-tw.json'
# url = 'https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json'
# url = "https://opengov.tainan.gov.tw/OpenApi/api/service/GetJsonLd/63da41fb-a3a1-4a88-b070-34eeb24d7c60"
# url = "https://www.twtainan.net/data/shops_zh-tw.json"

# requessst=requests.get(url, headers={
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
# })                
# # print(requessst.text)
# root = requessst.json()
# root = json.loads(requessst.text)
# for i in root:
#     print(i['ar'])


# 要用記得要解掉註解
# requessst=requests.get(url, headers={
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
# })                
# print(request.text)
# root = requessst.json()
# rd = requessst.content[3:].decode('utf-8')
# root = json.loads(rd)

# with request.urlopen(url) as response:
    # data = json.load(response)
    # print(data)

# address_list = []
# for station in root:
#     ad = station['address']
#     address_list+=[ad]
# address_list.append(ad)
# # print(address_list)



# district_list = []
# for station in root:
#     dis = station['district']
#     district_list+=[dis]
# district_list.append(dis)
# # print(district_list)
    


# name_list = []
# for station in root:
#     na = station['name']
#     name_list+=[na]
# name_list.append(na)
# # print(name_list)



# opentime_list = []
# for station in root:
#     ot = station['open_time']
#     opentime_list+=[ot]
# opentime_list.append(ot)
# # print(opentime_list)
  


# cate_list = []
# for station in root:

#     if len(station['category']) == 0:
#         category="None"
#         # print(category)
#         cate_list+=[category]
#     else:
#         # print(station['category'][0])
#         category = station['category'][0]
#         # print(category)
#         cate_list+=[category]
# cate_list.append(category)
# # print(cate_list)

  
# codes = ["101","102","103"]
# students = ["James","Noah","Olivia"]
# grades = ["65","75","80"]
# teach = ["89","56","74"]
# bitch = ["sdf","hgf","drhnb"]

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///Blog.db"
db = SQLAlchemy(app)
# migrate = Migrate(app,db)  #要用記得要解掉註解

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text,nullable=False)
    author = db.Column(db.String(20), nullable=False, default='N/A')
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    aname = db.Column(db.String(100), nullable=True)
    opentime = db.Column(db.String(200), nullable=True)
    # email = db.Column(db.String(40), nullable=False)
    # password = db.Column(db.String(30), nullable=False)

    def __repr__(self):
        return 'Blog' + str(self.id)

# for a,b,c,d,e in itertools.zip_longest(address_list,district_list,name_list,opentime_list,cate_list):
#     # print(a,b,c,d,e)
#     new_post = Blog(title=a, content=b, author=c, aname=d, opentime=e)
#     db.session.add(new_post)
#     db.session.commit()

@app.route('/')
def index():
    # -------------------add-----------------#(盡量不要寫在@app.route裡面)
    # for a,b,c,d,e in itertools.zip_longest(address_list,district_list,name_list,opentime_list,cate_list):
    #     print(a,b,c,d,e)

    #     new_post = Blog(title=a, content=b, author=c, aname=d, opentime=e)
    #     db.session.add(new_post)
    #     db.session.commit()
    # ------------------------------------------#

    # -------------------delete-----------------#(盡量不要寫在@app.route裡面)
    # query = Blog.query.all()
    # print(query)
    # for i in query:
    #     print(i)
    #     db.session.delete(i)
    #     db.session.commit()
    #-------------------------------------------# 

    page = request.args.get('page', 1 ,type=int)
    query = Blog.query.order_by(Blog.date_posted).paginate(page, 20, False)
    # print(query)
     
    return render_template('bike_list.html', query=query)
                                            #  ,data = root 可能有需要用到

# query = Blog.query.all()
# query = Blog.query.filter_by(title=sname).all()
# for i in query:
    # print(i)
# print(query)  


port = int(os.getenv('PORT', 8080))   
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)




        