PATH = os.path.join('base_class', 'act.json')
file = open(PATH, 'r')
act_list = json.loads(file.read())
acts = [act_data[0] for act_data in act_list]

query = input("Enter Act name : ")
