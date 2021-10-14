from django.http import response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers

class HelloAPIview(APIView):                   #Va a ser la clase de un APIview de prueba

    #serializers_class=serializers.Helloserilizers   #Test API 

    def get(self, request, format=None):       #Retornar lista de caracteristicas del APIView
        an_apiview=[
            'Usamos metodos HTTP como funciones (get, post, path, put, delete)',
            'Es similar a una vista tradicional de Django',
            'Nos da el mayor control sobre la logica nuestra aplicacion',
            'esta mapeado manualmente a los URL',
        ]

        return Response({'mesage': 'Hello', 'an_apiview': an_apiview})

    """def post(self, request):                    #Create a message with our name
        serializers=self.serializers_class(data=request.data)
        if serializers.is_valid():
           name=serializers._validated_data.get('name')             #that name comes from serializer name
           message=f'Hello {name}'
           return Response({'message': message})
        else:
           return Response(
               serializers.error,
               status=status.HTTP_400_BAD_REQUEST
           ) """