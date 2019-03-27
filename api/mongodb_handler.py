import pymongo


LEGAL_SESSION = pymongo.MongoClient("mongodb://localhost:27017/")
LEGAL_DATABASES = LEGAL_SESSION["LKG_extended_data_base"]


def write_all(data, db_name):
    db = LEGAL_DATABASES[db_name]
    ids = []
    for item in data:
        ids.append(db.insert_one(item))

    return ids
