import mysql.connector
from conectoDB import conectar

#1. Gestión de Productos: Agregar, actualizar, ver o eliminar productos,
#incluyendo categorías y niveles de stock.
def ver_productos(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT p.id_producto, p.nombre, p.precio, p.stock, c.nombre as nombre_categoria FROM productos p JOIN categorias c ON p.id_categoria = c.id_categoria ORDER BY p.id_producto")
    #encabezado
    print("Lista de Productos:\n")
    print(f"{'ID':<4} {'Nombre':<25} {'Precio':>10} {'Stock':>7} {'Categoría':<15}")
    print("-" * 65)

    #filas
    for (id_producto, nombre, precio, stock, nombre_categoria) in cursor:
        print(f"{id_producto:<4} {nombre:<25} {precio:>10.2f} {stock:>7} {nombre_categoria:<15}")
    cursor.close()

def agregar_producto(conn):
    cursor = conn.cursor()
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    stock = int(input("Ingrese el stock del producto: "))
    id_categoria = int(input("Ingrese el ID de la categoría del producto: "))
    id_producto = int(input("Ingrese el ID del producto: "))
    sql = "INSERT INTO productos (id_producto, nombre, precio, stock, id_categoria) VALUES (%s, %s, %s, %s, %s)"
    values = (id_producto, nombre, precio, stock, id_categoria)
    cursor.execute(sql, values)
    conn.commit()
    print("Producto agregado exitosamente.")
    cursor.close()

def actualizar_producto(conn):
    cursor = conn.cursor()
    id_producto = int(input("Ingrese el ID del producto a actualizar: "))
    nombre = input("Ingrese el nuevo nombre del producto: ")
    precio = float(input("Ingrese el nuevo precio del producto: "))
    stock = int(input("Ingrese el nuevo stock del producto: "))
    sql = "UPDATE productos SET nombre = %s, precio = %s, stock = %s WHERE id_producto = %s"
    values = (nombre, precio, stock, id_producto)
    cursor.execute(sql, values)
    conn.commit()
    print("Producto actualizado exitosamente.")
    cursor.close()

def eliminar_producto(conn):
    cursor = conn.cursor()
    id_producto = int(input("Ingrese el ID del producto a eliminar: "))
    sql = "DELETE FROM productos WHERE id_producto = %s"
    values = (id_producto,)
    cursor.execute(sql, values)
    conn.commit()
    print("Producto eliminado exitosamente.")
    cursor.close()
    



