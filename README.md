# Proyecto Sistema de Ventas en Linea

Este documento describe el diseño de la base de datos implementada para el sistema de ventas en línea, donde justifico las decisiones tomadas respecto a la estructura, normalización, integridad, restricciones, procedimientos,etcetera. El diseño se encuentra normalizado hasta 3NF, cumpliendo con los requerimientos de la materia.

---

El sistema gestiona:
- **Productos**
- **Clientes**
- **Órdenes de compra**
- **Detalles de órdenes**
- **Categorías de productos**

Se definieron las siguientes entidades principales:
### ✔ *1. Categorías*
Agrupa los productos y permite clasificarlos.  
**Clave primaria:** `id_categoria`.

### ✔ *2. Productos*
Representa cada producto disponible para la venta.  
Incluye precio, stock y la categoría a la que pertenece.  
**Clave primaria:** `id_producto`.  
**FK:** `id_categoria`.

### ✔ *3. Clientes*
Contiene los datos del cliente (nombre, apellido, email, etc.).  
**Clave primaria:** `id_cliente`.

### ✔ *4. Órdenes*
Representa el encabezado de una venta realizada por un cliente.  
**Clave primaria:** `id_orden`.  
**FK:** `id_cliente`.

### ✔ *5. Detalles de orden*
Contiene cada producto asociado a una orden, junto con cantidad y precio.  
**Clave primaria compuesta:** (`id_orden`, `id_producto`).  
**FKs:** `id_orden`, `id_producto`.

---

# 2. Normalización (hasta 3NF)

El modelo fue construido aplicando las primeras tres formas normales:

---

## ✔ **1NF – Primera Forma Normal**
- No existen atributos multivaluados ni compuestos.
- Todas las columnas son atómicas.
- No existen listas dentro de un campo.
- Los detalles de una orden se manejan en una tabla independiente (`detalles_orden`) en lugar de almacenar múltiples productos dentro de un mismo registro de orden.

---

## ✔ **2NF – Segunda Forma Normal**
Para las tablas con **clave primaria simple**, no existen dependencias parciales.  
Para la tabla **detalles_orden**, cuya clave es compuesta:

- Los atributos `cantidad` y `precio_unitario` dependen de *ambos* campos de la clave (`id_orden`, `id_producto`), por lo que no violan 2NF.
- No existe ningún atributo que dependa solo de una parte de la clave.

---

## ✔ **3NF – Tercera Forma Normal**
No hay dependencias transitivas.

Ejemplos:

- En `productos`, la categoría no almacena su nombre, sino su ID → No se repite información.
- En `ordenes`, toda la información del cliente está en `clientes`.
- En `detalles_orden`, no se guarda el nombre del producto, solo su precio histórico.

Eliminar transitividades evita redundancia y asegura consistencia en todo el sistema.

---

# 3. Integridad Referencial y Operaciones en Cascada

El modelo utiliza claves foráneas con reglas de actualización y borrado, manteniendo coherencia en los datos:

### ✔ Productos → Categorías
```sql
ON UPDATE CASCADE
ON DELETE RESTRICT

