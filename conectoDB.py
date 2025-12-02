#conexionbase de datos
import mysql.connector

def conectar():
    try:
        mybd = mysql.connector.connect(
            host="localhost",
            port = 3306,
            user="root",
            password="root",
            database="sistemaVentasLinea"
        )
        if mybd.is_connected():
            print("Conexion exitosa a la base de datos")
            return mybd
    except mysql.connector.Error as err:
        print(f"Error al conectar a la base de datos: {err}")
        return None
    return None

