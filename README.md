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

El modelo respeta las primeras tres formas normales:

---

Ejemplos:

- En `productos`, la categoría no almacena su nombre, sino su ID → No se repite información.
- En `ordenes`, toda la información del cliente está en `clientes`.
- En `detalles_orden`, no se guarda el nombre del producto, solo su precio histórico.


---

# 3. Operaciones en cascada, transacciones,manejo de errores,indices y procedimientos almacenados

El modelo cuenta con todos los mencionados anteriormente para garantizar la consistencia de los datos en operaciones críticas, prevenir errores de consistencia, manejar operaciones complejas y mejorar el rendimiento de las consultas mas frecuentes (en este caso realizamos indice unicamente para productos).



