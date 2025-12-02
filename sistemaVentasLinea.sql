CREATE DATABASE IF NOT EXISTS sistemaVentasLinea;
use sistemaVentasLinea;

-- creo tablas
CREATE TABLE productos (
id_producto INT PRIMARY KEY,
nombre VARCHAR(50) NOT NULL,
precio DECIMAL (10,2) NOT NULL,
stock INT NOT NULL,
id_categoria INT NOT NULL,
FOREIGN KEY (id_categoria) REFERENCES categorias(id_categoria)
	ON UPDATE CASCADE
    ON DELETE RESTRICT
);

CREATE TABLE clientes (
id_cliente INT PRIMARY KEY,
nombre VARCHAR(50) NOT NULL,
apellido VARCHAR(50) NOT NULL,
email VARCHAR (100) UNIQUE NOT NULL,
telefono VARCHAR(20) NOT NULL,
direccion VARCHAR (50) NOT NULL
);

CREATE TABLE categorias (
id_categoria INT PRIMARY KEY,
nombre VARCHAR(50) UNIQUE
);

CREATE TABLE ordenes(
id_orden INT PRIMARY KEY,
fecha DATE NOT NULL,
id_cliente INT NOT NULL,
FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)
	ON UPDATE CASCADE
    ON DELETE RESTRICT
);

CREATE TABLE detalles_orden(
id_orden INT NOT NULL,
id_producto INT NOT NULL,
cantidad INT NOT NULL,
precio_unitario DECIMAL(10,2) NOT NULL,
FOREIGN KEY (id_orden) REFERENCES ordenes(id_orden)
	ON UPDATE CASCADE
    ON DELETE CASCADE,
FOREIGN KEY (id_producto) REFERENCES productos (id_producto)
	ON UPDATE CASCADE
    ON DELETE RESTRICT,
PRIMARY KEY (id_orden,id_producto)
);

-- inserts generados por IA y chequeados
INSERT INTO categorias (id_categoria, nombre) VALUES
(1, 'Electrónica'),
(2, 'Indumentaria'),
(3, 'Hogar'),
(4, 'Deportes'),
(5, 'Oficina'),
(6, 'Juguetería'),
(7, 'Librería'),
(8, 'Cocina'),
(9, 'Jardinería'),
(10, 'Accesorios');

INSERT INTO productos (id_producto, nombre, precio, stock, id_categoria) VALUES
(1, 'Mouse Gamer RGB',        8000.00,  50, 1),
(2, 'Teclado Mecánico',      22000.00,  30, 1),
(3, 'Auriculares Bluetooth', 15000.00,  40, 1),
(4, 'Remera Oversize Negra',  6000.00, 100, 2),
(5, 'Pantalón Jogger',       12000.00,  80, 2),
(6, 'Taza Cerámica Blanca',   3000.00, 200, 3),
(7, 'Lámpara LED Escritorio', 7000.00,  45, 3),
(8, 'Cuaderno A5 Rayado',     1500.00, 150, 7),
(9, 'Botella Térmica 1L',     9000.00,  60, 5),
(10,'Mochila Urbana',        18000.00,  40, 10);

INSERT INTO clientes (id_cliente, nombre, apellido, email, telefono, direccion) VALUES
(1, 'Juan',  'Pérez',      'juan.perez@example.com',     '1111-1111', 'Calle 1 123'),
(2, 'Ana',   'García',     'ana.garcia@example.com',     '2222-2222', 'Calle 2 456'),
(3, 'Luis',  'López',      'luis.lopez@example.com',     '3333-3333', 'Calle 3 789'),
(4, 'Carla', 'Suarez',     'carla.suarez@example.com',   '4444-4444', 'Calle 4 321'),
(5, 'María', 'Giménez',    'maria.gimenez@example.com',  '5555-5555', 'Calle 5 654'),
(6, 'Pedro', 'Martínez',   'pedro.martinez@example.com', '6666-6666', 'Calle 6 987'),
(7, 'Lucía', 'Rojas',      'lucia.rojas@example.com',    '7777-7777', 'Calle 7 135'),
(8, 'Sofía', 'Díaz',       'sofia.diaz@example.com',     '8888-8888', 'Calle 8 246'),
(9, 'Diego', 'Fernández',  'diego.fernandez@example.com','9999-9999', 'Calle 9 579'),
(10,'Flor',  'Romero',     'flor.romero@example.com',    '1010-1010','Calle 10 802');


INSERT INTO ordenes (id_orden, fecha, id_cliente)
SELECT
    (c.id_cliente - 1) * 10 + n AS id_orden,
    DATE_ADD('2025-01-01', INTERVAL n-1 DAY) AS fecha,
    c.id_cliente
FROM clientes c
JOIN (
    SELECT 1 AS n UNION ALL
    SELECT 2 UNION ALL
    SELECT 3 UNION ALL
    SELECT 4 UNION ALL
    SELECT 5 UNION ALL
    SELECT 6 UNION ALL
    SELECT 7 UNION ALL
    SELECT 8 UNION ALL
    SELECT 9 UNION ALL
    SELECT 10
) nums
ORDER BY id_orden;

INSERT INTO detalles_orden (id_orden, id_producto, cantidad, precio_unitario)
SELECT
    o.id_orden,
    ((o.id_orden - 1) MOD 10) + 1 AS id_producto,
    ((o.id_orden - 1) MOD 5) + 1 AS cantidad,
    p.precio AS precio_unitario
FROM ordenes o
JOIN productos p 
      ON p.id_producto = ((o.id_orden - 1) MOD 10) + 1
ORDER BY o.id_orden;

-- indice
CREATE INDEX idx_productos_nombre
ON productos (nombre);

-- procedimiento
DELIMITER $$
CREATE PROCEDURE crear_orden(
	IN p_id_cliente INT,
    IN p_id_producto INT,
    IN p_cantidad INT
)
BEGIN
	DECLARE v_precio DECIMAL(10,2);
    DECLARE v_stock INT;
    DECLARE v_nuevo_id_orden INT;
    
    START TRANSACTION;
    
    SELECT precio,stock
    INTO v_precio,v_stock
    FROM productos
    WHERE id_producto = p_id_producto
    FOR UPDATE;
    
    -- valido
    IF v_precio IS NULL THEN
		ROLLBACK;
        SIGNAL SQLSTATE '45000'
			SET message_text = 'stock insuficiente';
	END IF;
    
    SELECT IFNULL(MAX(id_orden) +1,1)
    INTO v_nuevo_id_orden
    FROM ordenes;
    
    INSERT INTO ordenes (id_orden, fecha, id_cliente)
    VALUES (v_nuevo_id_orden, CURDATE(), p_id_cliente);
    
    INSERT INTO detalles_orden (id_orden, id_producto, cantidad, precio_unitario)
    VALUES (v_nuevo_id_orden, p_id_producto, p_cantidad, v_precio);
    
    -- ACTUALIZO STOCK
	UPDATE productos
    SET stock = stock - p_cantidad
    WHERE id_producto = p_id_producto;
    
    COMMIT;
END$$

DELIMITER ;

-- pruebo procedimiento 
CALL crear_orden(1,1,2);
    
    
    







