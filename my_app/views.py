from django.views.generic import TemplateView, ListView, CreateView
from django.template.loader import get_template
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import SearchForm
from .forms import ResultsForm
from search_ontology import run_ontology_search
import json


# def index(request):
#   # return HttpResponse("Hello, world. You're at the my_app index.")
#   t = get_template('template.html')
#   html = t.render()
#   return HttpResponse(html)

def index(request):
	# if this is a POST request we need to process the form data
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		# print(request.POST)
		form = ResultsForm(request.POST)
		# check whether it's valid:
		if form.is_valid():
			data = request.POST
			# print(type(data)) # django dictionary
			data = dict(data.lists())
			# print(type(data)) # dictionary
			results = run_ontology_search(data)
			print(results['compound'])
			# results = pretty_json(results)
			# print(len(results))

			# process the data in form.cleaned_data as required
			# ...
			# redirect to a new URL:
			# return HttpResponseRedirect('/search_results/')
			return render(request, 'results.html', { 'data': data, 'results': results })

	# if a GET (or any other method) we'll create a blank form
	else:
		form = SearchForm()
		return render(request, 'search.html', {'form': form})

def pretty_json(value):
  return json.dumps(value, indent=4)