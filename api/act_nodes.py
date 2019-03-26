from base_class.legal_graph import LegalKnowledgeGraph 
from env import ENV

def act_add(j):
    filename = "{}/actlist.txt".format(ENV["DATASET_PATH"])
    with open(filename) as f:
        for line in f.readlines():
            line = line.strip()
            print(line)
            j.add_act(line)
    return(j)
