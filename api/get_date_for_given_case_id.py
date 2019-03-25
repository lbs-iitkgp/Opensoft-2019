'''
    Helper Function which returns the date for a case given its Indlaw SC ID
    '''
from get_dates import get_year_from_case

if __name__ == "__main__":
    CASE = '1987 Indlaw SC 28467'   #Example
    RESULT = get_year_from_case(CASE)
    print(RESULT)
