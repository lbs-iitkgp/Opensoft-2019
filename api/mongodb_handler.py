import pymongo
import encode_helper as encoder

LEGAL_CLIENT = pymongo.MongoClient("mongodb://localhost:27017/")
LEGAL_DATABASES = LEGAL_CLIENT["LKG_extended_data_base"]


def encode(item):
    """
    Encodes all dictionary keys
    """
    encoded_dict = {}
    for key, val in item.items():
        encoded_dict[encoder.custom_encode(key)] = val

    return encoded_dict


def decode(item):
    """
    Decodes all dictionary keys
    """
    decoded_dict = {}
    for key, val in item.items():
        decoded_dict[encoder.custom_decode(key)] = val

    return decoded_dict


def write_all(data, coll_name):
    """
    Writes all data into the mongodb database
    """
    collection = LEGAL_DATABASES[coll_name]
    ids = []
    for item in data:
        encoded_dict = encode(item)
        ids.append(collection.insert_one(encoded_dict))

    return ids


def read_all(coll_name, **filters):
    """
    Reads all data from the mongodb database
    """
    collection = LEGAL_DATABASES[coll_name]
    encoded_filters = encode(filters)
    collections = []
    for item in collection.find(encoded_filters, {'_id': 0}):
        collections.append(decode(item))

    if len(collections) > 1 or len(collections) == 0:
        return collections
    else:
        return collections[0]
