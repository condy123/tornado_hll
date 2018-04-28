import pymongo

mg = pymongo.MongoClient('127.0.0.1', 27017)

datas = [
        {'_id':1, 'data':12},
        {'_id':2, 'data':22},
        {'_id':3, 'data':'cc'}
    ]
print(mg.db['test'].insert(datas))