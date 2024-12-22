import sqlite3
import json

with open('data.json', 'r', encoding='utf8') as f:
    sections = json.load(f)

for section in sections:
    section_id = section['id']
    section_name = section['name']
    section_short_name = section['short_name']
    section_keywords = ''
    for i in section['keywords']:
        section_keywords += i
        section_keywords += ' '
    section_form = section['form']
    section_ovz = section['ovz']
    if section_ovz == 1:
        section_zab = ''
        for i in section['zab']:
            section_zab += i
            section_zab += ' '
    else:
        section_zab = None
    section_mun_id = section['mun_id']
    section_operator_id = section['operator_id']
    section_organization_id = section['organization_id']
    section_hours = section['hours']
    if section['location']:
        section_locations_lat = section['location']['lat']
        section_locations_lon = section['location']['lon']
    else:
        section_locations_lat = None
        section_locations_lon = None
    section_age_min= section['age_min']
    section_age_max = section['age_max']
    section_years = section['years']
    section_direction_id = section['direction']['id']
    section_direction_name = section['direction']['name']
    section_image = section['image']
    section_organization_name = section['organization_name']
    if section['address']:
        section_address = section['address']['name']
    else:
        section_address = None
    section_certified = section['reestrs']['certified']
    section_commercial = section['reestrs']['commercial']
    section_meaningful = section['reestrs']['meaningful']
    section_general = section['reestrs']['general']
    section_preprofessional = section['reestrs']['preprofessional']

    con = sqlite3.connect('service_db.db')
    cur = con.cursor()

    cur.execute(f'INSERT INTO sections '
                f'(id, name, short_name, keywords, form, ovz, zab, mun_id, operator_id, organization_id, hours, '
                f'location_lat, location_lon, age_min, age_max, years, direction_id, direction_name, image, '
                f'organization_name, address, certified, commercial, meaningful, general, preprofessional) '
                f'VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                (section_id, section_name, section_short_name, section_keywords, section_form, section_ovz, section_zab,
                 section_mun_id, section_operator_id, section_organization_id, section_hours, section_locations_lat,
                section_locations_lon, section_age_min, section_age_max, section_years, section_direction_id,
                section_direction_name, section_image, section_organization_name, section_address, section_certified,
                section_commercial, section_meaningful, section_general, section_preprofessional))
    con.commit()