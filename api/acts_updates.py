"""
    Makes a dictionary with
        ACT names as keys and the list
            of all its "updated versions with year" tuples as values
            """
            
from env import ENV

def get_all_versions_of_all_acts():

    ACT_TO_ALL_YEARS = dict()
    with open("{}/{}".format(ENV["DATASET_PATH"], 'actlist.txt'))  as f:   

        for line in f.readlines():
            line = line.strip()
            Act_name, year = line[:-4], line[-4:]
            Act_name = Act_name.strip()

            Act_name = Act_name.strip()
            if Act_name in ACT_TO_ALL_YEARS:
                ACT_TO_ALL_YEARS[Act_name].append((year, Act_name,))
            else:
                ACT_TO_ALL_YEARS[Act_name] = []
                ACT_TO_ALL_YEARS[Act_name].append((year, Act_name,))

    ACT_RECENT_YEARS = {}

    '''
        Groups amendments of act together into the primary act
            Ex. act = ABC Act & another_act = ABC Amendment 1 Act. 
                As act is in another_act, it is the parent of another_act and hence the code
        '''
    for act in ACT_TO_ALL_YEARS:
        ACT_RECENT_YEARS[act] = []
        for another_act in ACT_TO_ALL_YEARS:
            if another_act.find(act) == 0:

                [ACT_RECENT_YEARS[act].append(x)
                for x in ACT_TO_ALL_YEARS[another_act]]      

    return ACT_TO_ALL_YEARS
