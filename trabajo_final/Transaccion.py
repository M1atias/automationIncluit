import random

class Transaccion:
    def __init__(self, dni_cliente, tipo_movimiento, monto_movimiento, estado, nombre_comercio):
        self.__transaccion_id = random.randrange(1,99999999)
        self.__dni_cliente = dni_cliente
        self.__tipo_movimiento = tipo_movimiento
        self.__estado = estado
        self.__nombre_comercio = nombre_comercio
        self.__monto_movimiento = monto_movimiento

    def verificar_mov(self):
        if self.__monto_movimiento < 100000:
            return 'El movimiento no requiere justificación'
        else:
            return 'Se debe solicitar documentación que requiera la justificación del movimiento'



    def __str__(self):
        return f"Transacción: [transaccion._id {self.__transaccion_id},\n" \
               f"dni:{self.__dni_cliente},\n" \
               f"tipo_movimiento: {self.__tipo_movimiento}\n" \
               f"monto_movimiento:{self.__monto_movimiento}\n" \
               f"estado: {self.__estado},\n" \
               f"nombre_comercio: {self.__nombre_comercio}]"