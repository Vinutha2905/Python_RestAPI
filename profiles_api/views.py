from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """TEST API VIEW"""

    def get(self, request, format=None):
        """Returns a list of API features"""
        an_apiview=[
            'Uses HTTP methods as function (get,post, put, delete, patch)'
            'Is Similar to a traditional Django View'
            'Gives you the most control over your application logic'
            'Is mapped manually to the URLs'
        ]

        return Response({'message':'Hello', 'an_apiview': an_apiview})
