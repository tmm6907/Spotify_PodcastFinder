from django.shortcuts import render
from django.views import generic
from django.core.paginator import Paginator
from finder.models import Podcast

# Create your views here.
class PodcastListView(generic.ListView):
    model = Podcast
    paginate_by = 3
    template_name = 'paginator/pagination.html'  
    context_object_name = 'objects'
    queryset = Podcast.objects.all()