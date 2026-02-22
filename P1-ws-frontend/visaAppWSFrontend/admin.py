from django.contrib import admin
#from . models import Tarjeta , Pago

# Register your models here.
#@admin . register ( Tarjeta )
class TarjetaAdmin ( admin . ModelAdmin ) :
    list_display = ( 'numero' , 'nombre' , 'fechaCaducidad' )

# Register Voto model
#@admin . register ( Pago )
class PagoAdmin ( admin . ModelAdmin ):
    list_display = ( 'idComercio' , 'idTransaccion' , 'importe' , 'tarjeta' , 'marcaTiempo' , 'codigoRespuesta' )