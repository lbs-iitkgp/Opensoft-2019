'''
    Helper function to get the judgement for a case, given its Indlaw SC id
    '''

from get_judgements import get_all_judgements

if __name__ == "__main__":
    CASE = '2014 Indlaw SC 351'
    #Example
    RESULT = get_all_judgements(CASE)
    print(RESULT)
