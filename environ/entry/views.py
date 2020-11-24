from django.http import HttpResponse 
from django.shortcuts import render


def home_view(request, *args, **kwargs):
	print(args, kwargs)
	print(request.user)
	return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
	return render(request, "contact.html", {})

def about_view(request, *args, **kwargs):
	my_context = {
		"title": "The work I do",
		"this is true": True, 
		"my_number": 123,
		"my_list": [900, 4567, 1342, "Abc"],
		"my_html": "<h1>hello world</h1>"
	}
	return render(request, "about.html", my_context)

def projects_view(request, *args, **kwargs):
	return render(request, "projects.html", {})

def search_view(request, *args, **kwargs):
	return render(request, "search.html", {})

def events_view(request, *args, **kwargs):
	return render(request, "events.html", {})
