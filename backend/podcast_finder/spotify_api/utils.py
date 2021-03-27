from requests import Request
from rest_framework.response import Response
from rest_framework import status
from background_task import background

@background
def get_show_handler(id):
    url = Request('GET', 'https://api.spotify.com/v1/shows/{id}', params= {
    }).prepare().url
    return Response({'url':url}, status=status.HTTP_200_OK)