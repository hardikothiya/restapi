from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers


class HelloApiView(APIView):
    """ Hello Api"""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):

        an_apiview = [
        'Hy 1',
        'hy 2',
        'hy 3'
        ]

        return Response({'message': 'hello', 'an_apiview': an_apiview})

    def post(self, request):
        """ HEllo msg with name """

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f"hello {name}"
            return Response({'message': message})

        else:
            return Response(
            serializer.errors,
            status= status.HTTP_400_BAD_REQUEST
            )


    def put(self, request, pk=None):
        """ Update the object"""
        return Response({'method' : 'put'})

    def patch(self, request, pk=None):
        """partially  Update the object"""
        return Response({'method' : 'patch'})

    def delete(self, request, pk=None):
        """ delete the object"""
        return Response({'method' : 'delete'})
