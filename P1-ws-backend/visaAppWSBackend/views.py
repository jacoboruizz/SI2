from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import TarjetaSerializer, PagoSerializer
from django.forms.models import model_to_dict
from .models import Tarjeta, Pago
from rest_framework import status
from django.http import Http404
from . import pagoDB 

class TarjetaView(APIView):
    def post(self, request):

        if pagoDB.verificar_tarjeta(request.data):
            return Response({'message': 'Datos encontrados en la base de datos'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Datos no encontrados en la base de datos'}, 
                            status=status.HTTP_404_NOT_FOUND)

class PagoView(APIView):
    def post(self, request):
        try:
            pago = pagoDB.registrar_pago(request.data)

            if pago is None:
                return Response({'message': 'Error al registrar pago.'}, 
                                status=status.HTTP_404_NOT_FOUND)

            pago_dict = model_to_dict(pago)
            return Response(pago_dict, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({'message': 'Petición incorrecta (Bad Request). Revisa los datos enviados.'}, 
                            status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id_pago):
        
        if pagoDB.eliminar_pago(id_pago):
            return Response({'message': 'Pago eliminado correctamente'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'El pago no existe y por tanto no es posible borrarlo.'}, 
                            status=status.HTTP_404_NOT_FOUND)

class ComercioView(APIView):
    def get(self, request, idComercio):
        
        pagos = pagoDB.get_pagos_from_db(idComercio)
        
        if not pagos.exists():
            return Response({'message': 'No existen pagos asociados al comercio solicitado'}, 
                            status=status.HTTP_404_NOT_FOUND)
        
        
        serializer = PagoSerializer(pagos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)