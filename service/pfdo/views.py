from django.shortcuts import render
from .func_db import get_section_from_id, get_search_names_sections

def index(request):
    section = get_search_names_sections()



    return render(request,'index.html', {'section' : section})