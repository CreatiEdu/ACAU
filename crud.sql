-- Agregar nuevos usuarios
INSERT INTO usuarios (usuario, nombre, contrasena, id_rol) 
VALUES 
  ('Carlos', 'Carlos Martínez', 'carlosPass123', 2),
  ('Laura', 'Laura González', 'lauraSecure99', 1),
  ('Pedro', 'Pedro Ramírez', 'pedroPassword', 2);

-- Cambiar rol de Alejandro a estandar
UPDATE usuarios SET id_rol = 2 WHERE id_usuario = 4;

-- Ver todos los usuarios con sus roles
SELECT *
FROM usuarios
LEFT JOIN roles r ON u.id_rol = r.id_rol;

-- Buscar usuarios por nombre
SELECT * FROM usuarios WHERE nombre LIKE '%Fernandez%';

-- Borrar usuarios por nombre
DELETE * FROM usuarios WHERE nombre LIKE '%Fernandez%';

