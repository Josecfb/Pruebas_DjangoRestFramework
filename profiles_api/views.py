import rest_framework
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers


class HeloApiView(APIView):
    """API view de prueba"""
    
    serializer_class=serializers.HelloSerializer
    
    def get(self, request, format=None):
        """returna lista de caracteristicas del APIview"""
        an_apiview = [
            'Usamos metodos HTTP como funciones (get, post, path, put, delete)',
            'Es similar a una vista tradicional de Djando',
            'Nos da mayor control sobre la lógica de nuestra aplicación',
            'Está mapeado manualmente a los URLs',
        ]
        
        return Response({'message':'Hello','an_apiview':an_apiview})

    def post(self, request):
        """Crea un mensaje con un nombre"""
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )