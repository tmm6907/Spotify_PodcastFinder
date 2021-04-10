
from .query import query
from .tasks import search_shows

#Global Variables
OFFSET_LIMIT = 900

# Create your views here.
def search_handler(request):
    search_list = query
    for item in search_list:
        offset = 0
        while offset<=OFFSET_LIMIT:
            search_shows(item, offset)
            offset+=50
            search_shows(item, offset)
            offset+=50
            
    

