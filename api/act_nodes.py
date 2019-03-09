from  legal_graph import LegalKnowledgeGraph 

def act_add(j):
    filename = 'actlist.txt'
    with open(filename) as f:
        for line in f.readlines():
            line = line.strip()
            print(line)
            j.add_act(line)
    return(j)


