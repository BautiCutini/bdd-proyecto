import os
from colorama import Fore
import mysql.connector
from conectoDB import conectar

#3. Procesamiento de Órdenes: Mostrar las órdenes pedidas por un cliente
#dado.
def mostrar_ordenes_cliente(conn):
    cursor = conn.cursor()
    id_cliente = int(input("Ingrese el ID del cliente: "))
    cursor.execute("""
        SELECT o.id_orden, o.fecha, p.id_producto, p.nombre, od.cantidad, (od.cantidad * p.precio) AS total_precio
        FROM ordenes o
        JOIN detalles_orden od ON o.id_orden = od.id_orden
        JOIN productos p ON od.id_producto = p.id_producto
        WHERE o.id_cliente = %s
        ORDER BY o.id_orden
    """, (id_cliente,))

    #encabezado
    print(f"\nÓrdenes del Cliente ID {id_cliente}:\n")
    print(f"{'ID Orden':<10} {'Fecha':<12} {'ID Prod':<8} {'Nombre Producto':<30} {'Cant':<6} {'Precio Total':>12}")
    print("-" * 80)

    #filas
    for (id_orden, fecha, id_producto, nombre_producto, cantidad, total_precio) in cursor:
        print(f"{id_orden:<10} {str(fecha):<12} {id_producto:<8} {nombre_producto:<30} {cantidad:<6} {total_precio:>12.2f}")

    cursor.close()


#4. Búsquedas Avanzadas: Recuperar productos o clientes con filtros (e.g.,
#productos más vendidos).
def productos_mas_vendidos(conn):
    cursor = conn.cursor()
    sql = "SELECT p.id_producto,p.nombre, SUM(od.cantidad) AS total_vendido FROM productos p JOIN detalles_orden od ON p.id_producto = od.id_producto GROUP BY p.id_producto, p.nombre ORDER BY total_vendido DESC"
    cursor.execute(sql)
    #encabezado
    print("\nProductos más vendidos:\n")
    print(f"{'ID Producto':<12} {'Nombre Producto':<30} {'Total Vendido':>15}")
    print("-" * 60)
    #filas
    for (id_producto, nombre_producto, total_vendido) in cursor:
        print(f"{id_producto:<12} {nombre_producto:<30} {total_vendido:>15}")
    cursor.close()
    

#5. Reporte de productos más vendidos: Generar un reporte del producto
#más vendido indicando la cantidad total pedida de ese producto.
def producto_mas_vendido(conn):
    cursor  = conn.cursor()
    sql = """
    SELECT p.id_producto, p.nombre, SUM(od.cantidad) AS total_vendido
    FROM productos p
    JOIN detalles_orden od ON p.id_producto = od.id_producto
    GROUP BY p.id_producto, p.nombre
    ORDER BY total_vendido DESC
    LIMIT 1
    """
    cursor.execute(sql)
    resultado = cursor.fetchone()

    print("\nProducto más vendido:\n")
    if resultado:
        id_producto, nombre_producto, total_vendido = resultado
        print(f"\n{'ID Producto':<15}{'Nombre':<30}{'Total Vendido':>15}")
        print("-" * 60)
        print(f"{id_producto:<15}{nombre_producto:<30}{total_vendido:>15}")

    else:
        print("No se encontraron ventas.")
    cursor.close()



#6. Modificiación de valor de un producto: Modificar las órdenes de un
#producto dado para ajustarse una cierta cantidad máxima.
def modificar_valor_producto(conn):
    cursor = conn.cursor()
    id_producto = int(input("Ingrese el ID del producto a modificar: "))
    nueva_cantidad = int(input("Ingrese la nueva cantidad máxima permitida: "))
    sql = "UPDATE detalles_orden SET cantidad = LEAST(cantidad, %s) WHERE id_producto = %s"
    values = (nueva_cantidad, id_producto)
    cursor.execute(sql, values)
    conn.commit()
    print("Cantidad máxima del producto actualizada exitosamente.")
    cursor.close()

#utilizo procedimiento de SQL para crear orden
def crear_orden(conn):
    id_cliente = int(input("Ingrese el ID del cliente para la orden: "))
    id_producto = int(input("Ingrese el ID del producto a ordenar: "))
    cantidad = int(input("Ingrese la cantidad a ordenar: "))

    cursor = conn.cursor()
    try:
        cursor.callproc('crear_orden', [id_cliente, id_producto, cantidad])
        conn.commit()
        print("Orden creada exitosamente.")
    except mysql.connector.Error as err:
        print(f"Error al crear la orden: {err}")
    finally:
        cursor.close()

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')