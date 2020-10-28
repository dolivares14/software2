-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 28-10-2020 a las 04:32:56
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
(1, 27511125, 'dan', 'admin', 0, '2020-10-20 00:17:13', '2020-10-20 00:17:13', '123dan'),
(3, 335689, 'lusi', 'normal', 0, '2020-10-27 16:57:16', '2020-10-27 16:57:16', '321');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `items`
--

CREATE TABLE `items` (
  `Codigo_items` int(11) NOT NULL,
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
(568984, 2020, '2020-12-31 00:00:00', '0000-00-00 00:00:00', '7', 1),
(6565656, 1, '2020-10-27 22:38:47', '2020-10-31 00:00:00', 'disponible', 8),
(123456123, 2020, '2020-10-27 20:14:12', '0000-00-00 00:00:00', '9', 1);

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
(1, 'Coca-cola 2l', 25, 45.5, 'Bebidas'),
(2, 'Mayonesa Mavesa 250Ml', 0, 12.5, 'Salsas y encurtidos');

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
  ADD PRIMARY KEY (`Codigo_items`);

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
  MODIFY `id_cliente` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `empleados`
--
ALTER TABLE `empleados`
  MODIFY `id_empleado` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `movitems`
--
ALTER TABLE `movitems`
  MODIFY `idmov` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `opeinventario`
--
ALTER TABLE `opeinventario`
  MODIFY `id_ope` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `producto`
--
ALTER TABLE `producto`
  MODIFY `id_producto` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `ventas`
--
ALTER TABLE `ventas`
  MODIFY `nfactura` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
