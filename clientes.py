#2. Gestión de Clientes: Registrar, actualizar y ver detalles de clientes,
#gestionar contactos.

import mysql.connector
from conectoDB import conectar

def ver_clientes(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT c.id_cliente,c.nombre,c.apellido,c.email,c.telefono,c.direccion FROM clientes c ORDER BY id_cliente")

    print("Lista de Clientes:\n")
    print(f"{'ID':<4} {'Nombre':<15} {'Apellido':<15} {'Email':<30} {'Teléfono':<15} {'Dirección':<30}")
    print("-" * 110)
    for (id_cliente, nombre, apellido, email, telefono, direccion) in cursor:
        print(f"{id_cliente:<4} {nombre:<15} {apellido:<15} {email:<30} {telefono:<15} {direccion:<30}")
    cursor.close()


def registrar_cliente(conn):
    cursor = conn.cursor()
    nombre = input("Ingrese el nombre del cliente: ")
    apellido = input("Ingrese el apellido del cliente: ")
    email = input("Ingrese el email del cliente: ")
    telefono = input("Ingrese el teléfono del cliente: ")
    id_cliente = int(input("Ingrese el ID del cliente: "))
    direccion = input("Ingrese la dirección del cliente: ")
    sql = "INSERT INTO clientes (id_cliente, nombre, apellido, email, telefono, direccion) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (id_cliente, nombre, apellido, email, telefono, direccion)
    cursor.execute(sql, values)
    conn.commit()
    print("Cliente agregado exitosamente.")
    cursor.close()

def actualizar_cliente(conn):
    cursor = conn.cursor()
    id_cliente = int(input("Ingrese el ID del cliente a actualizar: "))
    nombre = input("Ingrese el nuevo nombre del cliente: ")
    apellido = input("Ingrese el nuevo apellido del cliente: ")
    email = input("Ingrese el nuevo email del cliente: ")
    telefono = input("Ingrese el nuevo teléfono del cliente: ")
    direccion = input("Ingrese la nueva dirección del cliente: ")
    sql = "UPDATE clientes SET nombre = %s, apellido = %s, email = %s, telefono = %s, direccion = %s WHERE id_cliente = %s"
    values = (nombre, apellido, email, telefono, direccion, id_cliente)
    cursor.execute(sql, values)
    conn.commit()
    print("Cliente actualizado exitosamente.")
    cursor.close()

def eliminar_cliente(conn):
    cursor = conn.cursor()
    id_cliente_eliminar = int(input("Ingrese el ID del cliente a eliminar: "))
    sql = "DELETE from clientes WHERE id_cliente = %s"
    values = (id_cliente_eliminar,)
    cursor.execute(sql, values)
    conn.commit()
    print("Cliente eliminado exitosamente.")
    cursor.close()


