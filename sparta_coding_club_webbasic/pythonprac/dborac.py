from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

# 코딩 시작
# insert / find/ update/ delete

db.users.delete_one({'name':'bobby'})