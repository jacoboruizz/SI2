# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# author: rmarabini
"Interface with the dataabse"
import requests
from django.conf import settings


def verificar_tarjeta(tarjeta_data):
    """ Check if the tarjeta is registered 
    :param tarjeta_dict: dictionary with the tarjeta data
                       (as provided by TarjetaForm)
    :return True or False if tarjeta_data is not valid
    """
    api_url = f"{settings.RESTAPIBASEURL}tarjeta/"
    
    try:
        response = requests.post(api_url, json=tarjeta_data)
        
        return response.status_code == 200
    except Exception as e:
        return False


def registrar_pago(pago_dict):
    """ Register a payment in the database
    :param pago_dict: dictionary with the pago data (as provided by PagoForm)
      plus de tarjeta_id (numero) of the tarjeta
    :return new pago info if succesful, None otherwise
    """
    api_url = f"{settings.RESTAPIBASEURL}pago/"
    
    try:
        response = requests.post(api_url, json=pago_dict)
        
        if response.status_code == 200:
            return response.json()
        return None
    except Exception as e:
        print(f"Error conexión: {e}")
        return None


def eliminar_pago(idPago):
    """ Delete a pago in the database
    :param idPago: id of the pago to be deleted
    :return True if succesful,
     False otherwise
     """
    api_url = f"{settings.RESTAPIBASEURL}pago/{idPago}"
    response = requests.delete(api_url)

    if response.status_code == 200:
        return True
    return False


def get_pagos_from_db(idComercio):
    """ Gets pagos in the database correspondint to some idComercio
    :param idComercio: id of the comercio to get pagos from 
    :return list of pagos found
     """
    api_url = f"{settings.RESTAPIBASEURL}comercio/{idComercio}"
    response = requests.get(api_url)

    if response.status_code == 200:
        return response.json()
    return []
    
