from django.urls import path, include
from . import views

from .apiviews import SchoolList, SchoolDetail

app_name='school'
urlpatterns = [
	path('', views.IndexView.as_view(), name='index'),
	path('results/', views.search, name='search'), 
	path('<int:pk>/', views.DetailView.as_view(), name='detail'),
	path('add/', views.add1, name='add1'),
	path('deleteMarked/', views.deleteMarked, name='deleteMarked'),
	path('<int:school_id>/edit/', views.edit, name='edit'),
	path("api/schools/", SchoolList.as_view(), name="schools_list"),
	path("api/schools/<int:pk>/", SchoolDetail.as_view(), name="school_detail")
	
]
