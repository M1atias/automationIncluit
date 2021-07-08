from trabajo_final.Transaccion import Transaccion


def opciones():
    op = int(input("1- Listar transacciones\n"
                   "2- Verificar justificación de mov \n"
                   "3- Imprimir transacciones mayor a $100.000\n"
                   "4- Sumar los montos de todas las transacciones de tipo consumo\n"
                   "0- Salir\n"
                   "Ingrese opción: "))
    return op

def main():
    transaccion_a = Transaccion(45990339, 'CONSUMO', 2000, 'RECHAZADO', 'MUSIMUNDO')
    transaccion_b = Transaccion(45990339, 'CONSUMO', 2000, 'APROBADO', 'MUSIMUNDO')
    transaccion_c = Transaccion(30949303, 'CASH_IN', 50000, 'APROBADO', 'PAGOFACIL')
    transaccion_d = Transaccion(30949303, 'CASH_OUT', 300000, 'APROBADO', 'PAGOFACIL')

    transacciones = [transaccion_a,transaccion_b,transaccion_c,transaccion_d]

    opcion= opciones()

    while opcion != 0:
        if opcion == 1:
            for transaccion in transacciones:
                print(transaccion)
        opcion = opciones()


main()