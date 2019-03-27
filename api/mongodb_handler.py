import pymongo


LEGAL_CLIENT = pymongo.MongoClient("mongodb://localhost:27017/")
LEGAL_DATABASES = LEGAL_CLIENT["LKG_extended_data_base"]


def write_all(data, coll_name):
    collection = LEGAL_DATABASES[coll_name]
    ids = []
    for item in data:
        ids.append(collection.insert_one(item))

    return ids


def read_all(coll_name, **filters):
    collection = LEGAL_DATABASES[coll_name]
    return collection.find(filters, {'_id': 0})
