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
from encode_helper import custom_encode, custom_decode

# Year, State, no.of sections ## Make serial id as key add act
acts_ka_data = acts_separated.acts_data_miner()
acts_ka_data_encoded = {}
s_acts_ka_data = []

for x in acts_ka_data:
    for phew in acts_ka_data[x]:
        # phew.append(x)
        # var = str(phew[0])
        # phew.pop(0)
        s_acts_ka_data.append(phew)

print(json.dumps(s_acts_ka_data, indent=4))

for x in s_acts_ka_data:
    # x_binari = x.encode("utf-8")
    
    
#     print(json.dumps(s_acts_ka_data[x], indent = 2))
    # print("Yo")
    for k in x.keys():
        acts_ka_data_encoded[custom_encode(str(k))] = x[k]

# with open(acts.json, r) as acts_ka_file:
#     acts_ka_data = json.loads(acts_ka_file.read())
# print(json.dumps(acts_ka_data, indent=4))
# with open(cases.json, r) as cases_ka_file:
#     cases_ka_data = json.loads(cases_ka_file.read())


legal_client = pymongo.MongoClient("mongodb://localhost:27017/")
legal_db = legal_client["LKG_extended_data_base"]
acts_collection = legal_db["acts_ka_db"]
cases_collection = legal_db["cases_ka_db"]

x = acts_collection.insert_one(acts_ka_data_encoded)

# y = mycol.insert_one(cases_ka_data)
