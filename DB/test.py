# 몽고디비 연결

from pymongo import mongo_client
from  database import create_review

# DB_HOST : connect mongodb -> ip port
# DB_id : accound id
# DB_PW : PW

#         connect( ip + port )
# python -------------- mongodb

# 127.0.0.1 무조건 내컴퓨터 ip

# port number:
# ssh: 22
# http : 80
# mariadb : 3386
# mongodb : 27017

# dbms: database management system
# db: database = data storage
# DB:Shop
# collection member goods order post

# client = mongo_client('127.0.0.1',"27017")
# db = client['movie']    # space in mongodb
# collection = db.get_collection('review')
#
# data = {"msg":"mongodb data test"}
#
# collection.insert(data) # 1 data save

create_review()
