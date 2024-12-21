import sqlite3 as sql3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "service_db.db")


def get_section_from_id(section_id):        # Получение секции из базы данных по идентификатору
    con = sql3.connect(db_path)
    cur = con.cursor()

    cur.execute(f'SELECT * FROM sections WHERE id = {section_id}')
    section_db = cur.fetchall()[0]

    section = {"id": section_db[0], "name": section_db[1], "short_name": section_db[2], "keywords": section_db[3],
               "form" : section_db[4], "ovz" : section_db[5], "zab" : section_db[6], "mun_id" : section_db[7], "operator_id" : section_db[8],
               "organization_id" : section_db[9], "hours" : section_db[10], "location_lat" : section_db[11], "location_lon" : section_db[12],
               "age_min" : section_db[13], "age_max" : section_db[14], "years" : section_db[15], "direction_id" : section_db[16],
               "direction_name" : section_db[17], "image" : section_db[18], "organization_name" : section_db[19], "address": section_db[20],
               "certified" : section_db[21], "commercial" : section_db[22], "meaningful" : section_db[23], "general" : section_db[24],
               "preprofessional" : section_db[25]}

    return section


def get_all_sections():         # Получение списка всех секций из базы данных
    con = sql3.connect(db_path)
    cur = con.cursor()

    cur.execute(f'SELECT * FROM sections')
    sections_all_db = cur.fetchall()
    sections = []

    for element in sections_all_db:
        section = {}
        sections.append(section)
    return sections


def get_search_names_sections():        # Получение списка параметров секций для поиска
    con = sql3.connect(db_path)
    cur = con.cursor()

    cur.execute(f'SELECT id, name, short_name, keywords FROM sections')
    search_names_db = cur.fetchall()

    search_names = []
    for element in search_names_db:
        search = {'id' : element[0], 'name' : element[1], 'short_name' : element[2], 'keyword' : element[3]}
        search_names.append(search)

    return search_names


def get_output_info_sections():
    con = sql3.connect(db_path)
    cur = con.cursor()

    cur.execute(f'SELECT id, short_name, address, age_min, age_max FROM sections')
    section_db = cur.fetchall()

    infos = []
    for element in section_db:
        age = f'{element[3] // 12} - {element[4] // 12}'
        info = {'id' : element[0], 'short_name' : element[1], 'address' : element[2], 'age' : age}
        infos.append(info)

    return infos



get_output_info_sections()