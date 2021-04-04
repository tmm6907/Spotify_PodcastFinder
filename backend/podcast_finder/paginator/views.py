from django.shortcuts import render
from django.views import generic
from django.core.paginator import Paginator
from spotify_api.models import Show

# Create your views here.
class PodcastListView(generic.ListView):
    model = Show
    paginate_by = 25
    template_name = 'paginator/pagination.html'  
    queryset = Show.objects.all()