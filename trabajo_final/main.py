from trabajo_final.Transaccion import Transaccion


def opciones():
    op = int(input("1- Listar transacciones\n"
                   "2- Verificar justificación de mov \n"
                   "3- Imprimir transacciones mayor a $100.000\n"
                   "4- Sumar los montos de todas las transacciones de tipo consumo\n"
                   "5- Agregar transaccion\n"
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
            for t in transacciones:
                print(t)
        elif opcion == 2:
            for t in transacciones:
                print(t.verificar_mov())
        elif opcion == 3:
            for t in transacciones:
                if t.monto_mov > 100000:
                    print(t)
        elif opcion == 4:
            total = 0
            for t in transacciones:
                if t.tipo_mov == 'CONSUMO':
                    total +=t.monto_mov
            print('El monto total es: $', total)

        # Este opción se plantea en el curso la ultima clase
        elif opcion == 5:
            dni = int(input("Ingrese DNI del cliente: "))
            tipo_mov = input("Ingrese el tipo de movimiento:")
            monto = float(input("Ingrese el monto de la transaccion: "))
            estado = input("Ingrese estado: ")
            local = input("Ingrese el nombre del comercio: ")

            transaccion = Transaccion(dni,tipo_mov,monto,estado,local)
            transacciones.append(transaccion)

        opcion = opciones()


main()