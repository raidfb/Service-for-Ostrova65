# from func_db import get_section_from_id, get_output_info_sections
#
# def index(request):
#     sections = get_output_info_sections()
#
#     html_list = f'<ul>'
#
#     for info in sections:
#         info_str = f'{info["id"]} | {info["short_name"]} | {info["address"]} | {info["age"]}'
#         html_list += f'<li>{info_str} ---> <a href="section/{info["id"]}">Подробнее</a></li>'
#
#     html_list += f'</ul>'
#
#     return render(request, 'page60406555.html', {'section' : html_list})
#
#
# def section(request, section_id):
#
#     section = get_section_from_id(section_id)
#
#
#     name = section["name"]
#     ovz = section["ovz"]
#     hours = section["hours"]
#     age_min = section["age_min"] // 12
#     age_max = section["age_max"] // 12
#     direction_name = section["direction_name"]
#     organization_name = section["organization_name"]
#     address = section["address"]
#     certified = section["certified"]
#     commercial = section["commercial"]
#     meaningful = section["meaningful"]
#     general = section["general"]
#     preprofessional = section["preprofessional"]
#
#
#     list_html = (f'<ul>'
#                  f'<li>{name}</li>'
#                  f'<li>{ovz}</li>'
#                  f'<li>Академические часы: {hours}</li>'
#                  f'<li>Возраст: с {age_min} до {age_max}</li>'
#                  f'<li>{direction_name}</li>'
#                  f'<li>Организатор: {organization_name}</li>'
#                  f'<li>Адресс: {address}</li>'
#                  f'</ul>')
#
#     return render(request, 'index.html', {'section' : list_html})