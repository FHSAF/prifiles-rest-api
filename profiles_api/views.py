from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from profiles_api import serializers


class HelloApiView(APIView):
    """Test API vIEW"""

    serializer_class = serializers.HelloSerializer

    def get(self, request, fromat=None):
        """returns a list of APIView freatues"""
        an_apiview = [
            'Use HTTP methods as function (get, post, pathc, put, delete',
            'Is mapped manually to URLs',
        ]
        return Response({"message": "Hello", "an_piview": an_apiview})

    def post(self, request):
        """ Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({"message": message})

        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """ Handle updating and object"""
        return Response({"method": "PUT"})

    def patch(self, request, pk=None):
        """ Handle Partial update"""
        return Response({"Method": 'patch'})

    def delete(self, request, pk=None):
        """ Delete an object"""
        return Response({"Method": "delete"})
