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


class IndexView(generic.ListView):
	template_name = 'school/index.html'
	context_object_name = 'school_list'

	def get_queryset(self): 
		"""Return the last five published questions."""
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
	template='school/index.html'
	query=request.GET.get('q')
	results=School.objects.filter(Q(name__icontains=query))
	return render(request, template)


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




#######################################################
class SchoolView(viewsets.ModelViewSet):
	queryset = School.objects.all()
	serializer_class = SchoolSerializer