from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API vIEW"""

    def get(self, request, fromat=None):
        """returns a list of APIView freatues"""
        an_apiview = [
            'Use HTTP methods as function (get, post, pathc, put, delete',
            'Is mapped manually to URLs',
        ]
        return Response({"message": "Hello", "an_piview": an_apiview})
