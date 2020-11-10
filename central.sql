-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 10-11-2020 a las 23:38:08
-- Versión del servidor: 10.4.14-MariaDB
-- Versión de PHP: 7.4.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `central`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `clientes`
--

CREATE TABLE `clientes` (
  `id_cliente` int(11) NOT NULL,
  `ci_cliente` int(11) NOT NULL,
  `nomb_cliente` varchar(50) NOT NULL,
  `numbcompras` int(11) NOT NULL,
  `direccion` varchar(80) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `clientes`
--

INSERT INTO `clientes` (`id_cliente`, `ci_cliente`, `nomb_cliente`, `numbcompras`, `direccion`) VALUES
(1, 123456, 'daniel', 0, 'La limpia dr Portillo\n'),
(2, 5689997, 'Luis Ortega', 0, 'Caracas\n'),
(3, 369888, 'Felipe', 0, 'adasdasasdasdadsa\n'),
(4, 69669669, 'Gonzalo Fernandez', 1, '\n'),
(5, 5665656, 'Daniel Phillips', 1, 'New york av california\n');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `empleados`
--

CREATE TABLE `empleados` (
  `id_empleado` int(11) NOT NULL,
  `ci_empleado` int(11) NOT NULL,
  `nomb_empleado` varchar(50) NOT NULL,
  `privilegios` varchar(15) NOT NULL,
  `numventas` int(11) NOT NULL,
  `Fecha_registro` datetime NOT NULL,
  `Fecha_ultima_sesion` datetime NOT NULL,
  `contraseña` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `empleados`
--

INSERT INTO `empleados` (`id_empleado`, `ci_empleado`, `nomb_empleado`, `privilegios`, `numventas`, `Fecha_registro`, `Fecha_ultima_sesion`, `contraseña`) VALUES
(4, 335689, 'lusi', 'normal', 2, '2020-11-04 19:47:58', '2020-11-04 19:47:58', '321');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `items`
--

CREATE TABLE `items` (
  `Codigo_items` bigint(13) NOT NULL,
  `id_producto` int(11) NOT NULL,
  `fecha_registro` datetime NOT NULL,
  `fecha_expedicion` datetime NOT NULL,
  `estado` varchar(30) NOT NULL,
  `cantidad` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `items`
--

INSERT INTO `items` (`Codigo_items`, `id_producto`, `fecha_registro`, `fecha_expedicion`, `estado`, `cantidad`) VALUES
(6565656, 1, '2020-10-27 22:38:47', '2020-10-31 00:00:00', 'disponible', 8),
(123456123, 2, '2020-10-27 20:14:12', '0000-00-00 00:00:00', '9', 1),
(565689897, 3, '2020-11-07 17:52:34', '2021-02-26 00:00:00', 'disponible', 32),
(2147483647, 3, '2020-11-09 23:34:31', '2020-11-13 00:00:00', 'disponible', 2),
(1234567891234, 1, '2020-11-09 23:48:57', '2020-11-11 00:00:00', 'disponible', 5),
(9876543219876, 2, '2020-11-09 23:56:41', '2020-11-20 00:00:00', 'disponible', 9);

--
-- Disparadores `items`
--
DELIMITER $$
CREATE TRIGGER `addprodu` AFTER INSERT ON `items` FOR EACH ROW UPDATE producto SET disponibilidad=disponibilidad + NEW.cantidad WHERE id_producto=new.id_producto
$$
DELIMITER ;
DELIMITER $$
CREATE TRIGGER `restprodu` AFTER UPDATE ON `items` FOR EACH ROW IF old.cantidad > new.cantidad THEN
UPDATE producto SET disponibilidad = disponibilidad - cantidad WHERE id_producto = new.id_producto;
ELSE
UPDATE producto SET disponibilidad = disponibilidad + cantidad WHERE id_producto = new.id_producto;
END IF
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `movitems`
--

CREATE TABLE `movitems` (
  `idmov` int(11) NOT NULL,
  `id_producto` int(11) NOT NULL,
  `n_factura` int(11) DEFAULT NULL,
  `id_ope` int(11) DEFAULT NULL,
  `accion` varchar(20) NOT NULL,
  `cantidad` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `movitems`
--

INSERT INTO `movitems` (`idmov`, `id_producto`, `n_factura`, `id_ope`, `accion`, `cantidad`) VALUES
(1, 2, 5, 0, 'Venta', 55),
(2, 2, 5, 0, 'Venta', 55),
(3, 2, 3, 0, 'Venta', 3),
(4, 2, 3, 0, 'Venta', 2),
(5, 3, 0, 1, 'Ingreso', 32),
(6, 3, 4, 0, 'Venta', 2),
(7, 3, 4, 0, 'Venta', 5),
(8, 3, 5, 0, 'Venta', 2),
(9, 1, 0, 3, 'Ingreso', 5),
(10, 2, 0, 4, 'Ingreso', 9);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `opeinventario`
--

CREATE TABLE `opeinventario` (
  `id_ope` int(11) NOT NULL,
  `id_empleado` int(11) NOT NULL,
  `descripcion` varchar(100) NOT NULL,
  `hora_ope` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `opeinventario`
--

INSERT INTO `opeinventario` (`id_ope`, `id_empleado`, `descripcion`, `hora_ope`) VALUES
(1, 4, 'Registro de item', '2020-11-07 17:52:36'),
(2, 4, 'Registro de item', '2020-11-09 23:34:31'),
(3, 4, 'Registro de item', '2020-11-09 23:48:57'),
(4, 4, 'Registro de item', '2020-11-09 23:56:41');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `producto`
--

CREATE TABLE `producto` (
  `id_producto` int(11) NOT NULL,
  `Nomb_producto` varchar(50) NOT NULL,
  `disponibilidad` int(11) NOT NULL,
  `precio` float NOT NULL,
  `Clasificacion` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `producto`
--

INSERT INTO `producto` (`id_producto`, `Nomb_producto`, `disponibilidad`, `precio`, `Clasificacion`) VALUES
(1, 'Pepsi 1.5L', 30, 0, 'Snacks'),
(2, 'Mayonesa Mavesa 250Ml', 9, 12.5, 'Salsas y encurtidos'),
(3, 'Helado EFE chocolate intenso', 34, 50, 'Refrigerados'),
(4, 'Caja kellogs 350gr', 0, 35.5, 'Snacks'),
(5, 'Zucaritas 350gr', 0, 35.5, 'Snacks');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ventas`
--

CREATE TABLE `ventas` (
  `nfactura` int(11) NOT NULL,
  `id_empleado` int(11) NOT NULL,
  `id_cliente` int(11) NOT NULL,
  `tipopago` varchar(20) NOT NULL,
  `monto` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `ventas`
--

INSERT INTO `ventas` (`nfactura`, `id_empleado`, `id_cliente`, `tipopago`, `monto`) VALUES
(1, 4, 1, 'Debito', 25),
(2, 4, 1, 'Debito', 50),
(3, 4, 1, 'Debito', 62.5),
(4, 4, 5, 'Debito', 350),
(5, 4, 4, 'Efectivo', 100);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `clientes`
--
ALTER TABLE `clientes`
  ADD PRIMARY KEY (`id_cliente`),
  ADD UNIQUE KEY `ci_cliente` (`ci_cliente`);

--
-- Indices de la tabla `empleados`
--
ALTER TABLE `empleados`
  ADD PRIMARY KEY (`id_empleado`),
  ADD UNIQUE KEY `ci_empleado` (`ci_empleado`),
  ADD UNIQUE KEY `contraseña` (`contraseña`);

--
-- Indices de la tabla `items`
--
ALTER TABLE `items`
  ADD PRIMARY KEY (`Codigo_items`) USING BTREE;

--
-- Indices de la tabla `movitems`
--
ALTER TABLE `movitems`
  ADD PRIMARY KEY (`idmov`);

--
-- Indices de la tabla `opeinventario`
--
ALTER TABLE `opeinventario`
  ADD PRIMARY KEY (`id_ope`);

--
-- Indices de la tabla `producto`
--
ALTER TABLE `producto`
  ADD PRIMARY KEY (`id_producto`);

--
-- Indices de la tabla `ventas`
--
ALTER TABLE `ventas`
  ADD PRIMARY KEY (`nfactura`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `clientes`
--
ALTER TABLE `clientes`
  MODIFY `id_cliente` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `empleados`
--
ALTER TABLE `empleados`
  MODIFY `id_empleado` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `movitems`
--
ALTER TABLE `movitems`
  MODIFY `idmov` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `opeinventario`
--
ALTER TABLE `opeinventario`
  MODIFY `id_ope` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `producto`
--
ALTER TABLE `producto`
  MODIFY `id_producto` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `ventas`
--
ALTER TABLE `ventas`
  MODIFY `nfactura` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
