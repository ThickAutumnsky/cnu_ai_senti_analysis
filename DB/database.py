from pymongo import MongoClient

# crud 작업:DAO(data acess object)만듬
# 게시글 -> boarddao.py
# 회원 ->memberdao.py

# member
#   create
#   update
#   delte
#   read

# goods
#   create
#   read
#   update
#   delete

# dashboard


# 1.connection (공통, common)


def db_con():
    client = MongoClient('127.0.0.1', 27017)  #mongodb 찾아감
    db = client['movie']                    #database 선택
    collection = db.get_collection('review')     #collection 선택
    return collection

# 2. review save(create)


def create_review(data):
    data = {"msg": "mongodb data test"}
    collection = db_con()
    # collection.insert_one(data)  # 1 data save


# 3. review read(read)


def read_review():
    collection = db_con()
