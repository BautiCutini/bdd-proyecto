from conectoDB import conectar
from colorama import init, Fore, Style, Back
from productos import ver_productos, agregar_producto, actualizar_producto, eliminar_producto
from clientes import ver_clientes, registrar_cliente, actualizar_cliente, eliminar_cliente
from funciones import mostrar_ordenes_cliente, productos_mas_vendidos, producto_mas_vendido, limpiar_pantalla, modificar_valor_producto,crear_orden
import os
init(autoreset=True)

def test():
    conn = conectar()
    if conn is None:
        print("No se pudo conectar a la base de datos.")
        return
    while True:
        limpiar_pantalla()
        print(Fore.RED + "\n--- Sistema de Ventas en Linea ---")
        print(Fore.YELLOW +"\nSeleccione una opción para probar:")
        print(Fore.YELLOW +"1. Ver Productos")
        print(Fore.YELLOW +"2. Agregar Producto")
        print(Fore.YELLOW +"3. Actualizar Producto")
        print(Fore.YELLOW +"4. Eliminar Producto")
        print(Fore.YELLOW +"5. Ver Clientes")
        print(Fore.YELLOW +"6. Registrar Cliente")
        print(Fore.YELLOW +"7. Actualizar Cliente")
        print(Fore.YELLOW +"8. Eliminar Cliente")
        print(Fore.YELLOW +"9. Mostrar Órdenes de un Cliente")
        print(Fore.YELLOW +"10. Lista De Productos Más Vendidos")
        print(Fore.YELLOW +"11. Producto Más Vendido")
        print(Fore.YELLOW +"12. Modificar Valor de un Producto")
        print(Fore.YELLOW +"13. Crear Orden")
        print(Fore.YELLOW +"0. Salir")
        opcion = int(input("Ingrese el número de la opción: "))
        if not isinstance(opcion, int) or opcion < 0 or opcion > 13 or opcion == "":
            print("Por favor ingrese un número válido entre 0 y 13.")
            continue
        

        if opcion == 1:
            limpiar_pantalla()
            ver_productos(conn)
            input(Fore.RED + "Presione ENTER para volver al menu...")
        elif opcion == 2:
            limpiar_pantalla()
            agregar_producto(conn)
            input(Fore.RED + "Presione ENTER para volver al menu...")
        elif opcion == 3:
            limpiar_pantalla()
            actualizar_producto(conn)
            input(Fore.RED + "Presione ENTER para volver al menu...")
        elif opcion == 4:
            limpiar_pantalla()
            eliminar_producto(conn)
            input(Fore.RED + "Presione ENTER para volver al menu...")
        elif opcion == 5:
            limpiar_pantalla()
            ver_clientes(conn)
            input(Fore.RED + "Presione ENTER para volver al menu...")
        elif opcion == 6:
            limpiar_pantalla()
            registrar_cliente(conn)
            input(Fore.RED + "Presione ENTER para volver al menu...")
        elif opcion == 7:
            limpiar_pantalla()
            actualizar_cliente(conn)
            input(Fore.RED + "Presione ENTER para volver al menu...")
        elif opcion == 8:
            limpiar_pantalla()
            eliminar_cliente(conn)
            input(Fore.RED + "Presione ENTER para volver al menu...")
        elif opcion == 9:
            limpiar_pantalla()
            mostrar_ordenes_cliente(conn)
            input(Fore.RED + "Presione ENTER para volver al menu...")
        elif opcion == 10:
            limpiar_pantalla()
            productos_mas_vendidos(conn)
            input(Fore.RED + "Presione ENTER para volver al menu...")
        elif opcion == 11:
            limpiar_pantalla()
            producto_mas_vendido(conn)
            input(Fore.RED + "Presione ENTER para volver al menu...")
        elif opcion == 12:
            limpiar_pantalla()
            modificar_valor_producto(conn)
            input(Fore.RED + "Presione ENTER para volver al menu...")
        elif opcion == 13:
            limpiar_pantalla()
            crear_orden(conn)
            input(Fore.RED + "Presione ENTER para volver al menu...")
        elif opcion == 0:
            limpiar_pantalla()
            print(Fore.RED + "Saliendo del sistema de pruebas...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":

    test()
