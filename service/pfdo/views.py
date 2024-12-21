from django.shortcuts import render
from .func_db import get_section_from_id, get_search_names_sections, get_output_info_sections

def index(request):
    sections = get_output_info_sections()

    html_list = f'<ul>'

    for info in sections:
        info_str = f'{info["id"]} | {info["short_name"]} | {info["address"]} | {info["age"]}'
        html_list += f'<li>{info_str}</li>'

    html_list += f'</ul>'

    return render(request,'index.html', {'section' : html_list})