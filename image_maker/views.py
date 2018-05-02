from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import Raw_data, Imag
# Create your views here.

def main_page(request, slug1, slug2):
	p = Raw_data()
	p.parse(slug1, slug2)
	desc = p.row_desc + "\n\n" + p.row_link
	v = Imag()
	v.create(p.row_image, p.row_title)
	return render(request, 'image_maker/index.html', {"desc": desc})
