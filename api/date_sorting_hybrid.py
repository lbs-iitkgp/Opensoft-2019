import spacy
import os
import re

MONTHS_LIST = ['January', 'February', 'March', 'April',
               'May', 'June', 'July', 'August', 'September',
               'October', 'November', 'December']

# Regex list for different date formats
REGEX_LIST = [
    r'([0-9]|[0-9]{2})-([0-9]|[0-9]{2})-([0-9]{4})',    # dd-mm-yyyy
    '([0-9]|[0-9]{2})(.{2})( of |\s+)(' + '|'.join(MONTHS_LIST) + '),(\s+)([0-9]{4})'   # eg. 29th October, 1982
]


def validate(date):
    '''
    Check if the date extracted is valid or not and processes it accordingly
    :param date: the date string
    :return: A tuple with processed date and its validity
    '''
    # true if two hifens and last four are digits
    # else month name should be included
    # remove the if present
    if date.count('-') == 2 and date[-4:].isnumeric():
        return date, True

    month_found = False
    for month in MONTHS_LIST:
        if month in date:
            month_found = True
            break

    if not month_found or not date[-4:].isnumeric():
        return None, False

    date = date.replace('the', '')
    return date, True


def find_dates_spacy(section, nlp):
    '''
    Extracts date using spacy
    :param section: the section of the case
    :return: A list of tuple (each element has the date extracted and its strat position)
    '''
    if not nlp:
      return []
    dates = []
    doc = nlp(section)
    for ent in doc.ents:
        if ent.label_ == "DATE":
            date, is_valid = validate(ent.text)
            if is_valid:
                dates.append((date.strip(), ent.start_char))

    return dates


def find_dates_regex(section):
    '''
    Extracts date using regex
    :param section: the section of the case
    :return: a list of tuple (each element has the date and its start position)
    '''

    dates = []
    # check if date of any given format is present
    date1 = re.search(REGEX_LIST[0], section)
    date2 = re.search(REGEX_LIST[1], section)
    if date1:
        dates.append(('-'.join(date1.groups()), date1.start()))
    if date2:
        dates.append((''.join(date2.groups()), date2.start()))

    return dates
 

def get_timelines(file_path, nlp=None):
    '''
    Extracts dates from each section of the case file using regex and nlp
    :param file_path: the path to the case file_path
    :param nlp: the nlp vocabulary using spacy (default is None)
    :return: a list of tuple (each element has a date and the section)
    '''
    file = open(file_path, 'r')
    # Section - Paragraph starting with numbered bullets
    # Extracts a list of sections from the case
    # section_list - Stores list of sections of cases
    # section - list of lines in a section
    # section_started - to check if section has been started
    section_list = []
    section = []
    section_started = False
    for line in file.readlines():
        # check if line starts with numbers
        match = re.search('(\d+)\.\s', line)
        if not match and not section_started:
            continue
        elif match and match.start() == 0:
            # Add all previous lines to the section list
            section_list.append(''.join(section))
            section = [line]
            section_started = True
        else:
            # Add the line to the section
            section.append(line)

    section_list.append(''.join(section))
    section_list = section_list[1:]

    file.close()

    # Extract dates from the sections
    final_list = []
    last_date = 'start-case'
    for section in section_list:

        # find dates using both spacy and regex
        dates = find_dates_regex(section) + find_dates_spacy(section, nlp)

        # sort the dates according to its start position
        dates.sort(key=lambda x: x[1])

        # last date of the previous section will be used if no date is found in that section
        final_date = last_date
        if len(dates) > 0:
            # new date is the first date of that section
            final_date = dates[0][0]
            # update last date
            last_date = dates[len(dates)-1][0]

        final_list.append((final_date, section))

    return final_list
  
# Uncomment to test script
# file_path = os.path.join(os.getcwd(), 'All_FT', '1953_M_3.txt')
# print(get_timelines(file_path, spacy.load('en')))
