# ==============================================================================|
# TO DO :                                                                       |
# ==============================================================================|
# Acts :Serial_id, name, to state/year, act_file.name, Page rank score          |
# Acts ka updated versions: Serial_id1 to Serial_id2                            |
# ==============================================================================|
# Judge :serial_id, ka Name, No.of cases, Page rank score                       |
# ==============================================================================|
# Cases :serial_id, file name , indlaw /judgement/  date /title, Page rank score|
# ==============================================================================|
import json
import pymongo
import base64
import acts_separated
from encode_helper import enkode, dekode

# Year, State, no.of sections ## Make serial id as key add act
acts_ka_data = acts_separated.acts_data_miner()
acts_ka_data_encoded = {}
s_acts_ka_data = {}
for x in acts_ka_data:
    for phew in acts_ka_data[x]:
        phew.append(x)
        var = str(phew[0])
        phew.pop(0)
        s_acts_ka_data[var] = phew

# print(json.dumps(s_acts_ka_data, indent = 4))

for x in s_acts_ka_data:
    # x_binari = x.encode("utf-8")
    x = str(x)
    print(s_acts_ka_data[x])
    # print("Yo")
    acts_ka_data_encoded[enkode(x)] = s_acts_ka_data[x]

# with open(acts.json, r) as acts_ka_file:
#     acts_ka_data = json.loads(acts_ka_file.read())
# print(json.dumps(acts_ka_data, indent=4))
# with open(cases.json, r) as cases_ka_file:
#     cases_ka_data = json.loads(cases_ka_file.read())


mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")
mongo_db = mongo_client["LKG_extended_data_base"]
mongo_col1 = mongo_db["acts_ka_db"]
mongo_col2 = mongo_db["cases_ka_db"]

x = mongo_col1.insert_one(acts_ka_data_encoded)

# y = mycol.insert_one(cases_ka_data)
