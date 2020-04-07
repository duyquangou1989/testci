from django.shortcuts import render
# Create your views here.
#from django.views.generic import TemplateView
from django.views.generic import ListView
from .models import Posts

class DashboardView(ListView):
	model = Posts
	template_name = 'home.html'
	context_object_name = 'all_posts_list'