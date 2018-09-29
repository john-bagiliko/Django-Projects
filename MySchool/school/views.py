"""
By: Bagiliko John
Year: 2018
""" 
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import School
from django.views import generic
from .forms import AddSchoolForm
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import Q
from rest_framework import viewsets
from .serializers import SchoolSerializer
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator



class IndexView(generic.ListView):
	template_name = 'school/index.html'
	context_object_name = 'school_list'
	paginate_by = 7

	def get_queryset(self): 
		return School.objects.all()

	
class DetailView(generic.DetailView):
	model=School
	template_name = 'school/detail.html'
	


def add1(request):
	form = AddSchoolForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance=form.save(commit=False)
		instance.save()
	context = {
	"form": form,
	}
	return render(request, 'school/add.html', context)
	return redirect('school:index')


def search(request):
	template='school/search.html'
	query=request.GET.get('mysearch')
	results=School.objects.filter(Q(name__icontains=query))
	context = {'results': results}
	return render(request, template, context)
	

def deleteMarked(request):
	School.objects.filter(marked__exact=True).delete()
	return render(request, 'school/detail.html')
		


def edit(request, school_id):
	school=get_object_or_404(School, pk=school_id)
	if request.method == "POST":
		form=AddSchoolForm(request.POST, request.FILES, instance=school)
		if form.is_valid:
			new_school = form.save(commit=False)
			new_school.save()
			return redirect('school:index')

	else:
		form = AddSchoolForm(instance=school)
		template='school/add.html'
		context = {'form': form}
		return render(request, template, context) 


