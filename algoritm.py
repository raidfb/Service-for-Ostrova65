from func_db import get_search_names_sections, get_search_age_sections, get_filter_directions_sections

def find_name(sections, prompt):
    search_ids = []

    for section in sections:
        string = section['short_name'] + section['name'] + section['keyword']
        if prompt.lower() in string.lower():
            search_ids.append(section['id'])
        else:
            continue

    return search_ids


def find_age(sections, prompt):
    search_ids = []
    for section in sections:
        if prompt >= section['age_min'] and prompt <= section['age_max']:
            search_ids.append(section['id'])

    return search_ids


def filter_directions(sections, prompt):
    search_ids = []
    for section in sections:
        if prompt.lower() in section['direction_name'].lower():
            search_ids.append(section['id'])

    return search_ids

# print(find_name(get_search_names_sections(), 'каллиграфия'))
# print(find_age(get_search_age_sections(), 14))
# print(filter_directions(get_filter_directions_sections(), 'Техническая'))