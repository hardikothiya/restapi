from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """ Hello Api"""

    def get(self, request, format=None):

        an_apiview = [
        'Hy 1',
        'hy 2',
        'hy 3'
        ]

        return Response({'message': 'hello', 'an_apiview': an_apiview})
