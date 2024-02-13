-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 19, 2022 at 01:22 PM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.1.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `gamco_hospital_management`
--

-- --------------------------------------------------------

--
-- Table structure for table `appointment`
--

CREATE TABLE `appointment` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `age` int(10) NOT NULL,
  `address` varchar(255) NOT NULL,
  `phone_num` varchar(50) NOT NULL,
  `time_in` varchar(255) NOT NULL,
  `time_out` varchar(255) NOT NULL,
  `total_spent` int(100) NOT NULL,
  `status` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `appointment`
--

INSERT INTO `appointment` (`id`, `name`, `age`, `address`, `phone_num`, `time_in`, `time_out`, `total_spent`, `status`) VALUES
(4, 'glenn', 20, '988324324', '0', '12:04 PM', '3:30 PM', 0, 'Active'),
(5, 'glenn', 20, '9089581281', '0', '12:08 PM', '5:08 PM', 0, 'Active'),
(6, 'glenn', 20, 'matina', '0', '12:10 PM', '3:00 PM', 0, 'Active'),
(7, 'glenn', 21, 'matina', '0', '12:12 PM', '5:00 PM', 0, 'Active'),
(8, 'glenn', 25, 'matina crossing', '2147483647', '12:16 PM', '5:00 PM', 0, 'Active'),
(9, 'glenn', 20, 'matina crossing aplaya', '09089581281', '12:17 PM', '3:00 PM', 0, 'Active'),
(10, 'glenn', 20, 'matina', '0999523314', '2022-12-10 12:25:00', '2022-12-10 16:25:00', 0, 'Active'),
(11, 'marcy', 28, 'maa', '0983495032', '2022-12-10 12:27 PM', '2022-12-10 5:00 PM', 0, 'Active'),
(12, 'Marie', 22, 'airport', '0908957823', '2022-12-10 12:29 PM', '2022-12-10 6:30 PM', 0, 'Active'),
(13, 'Hanz', 22, 'Samal', '098349351', '2022-12-10 5:40 PM', '2022-12-13 6:00 PM', 0, 'Inactive'),
(14, 'aj', 19, 'maa', '0987768291', '2022-12-14 10:55 PM', '2022-12-15 11:00 AM', 0, 'Active'),
(15, 'boyong', 20, 'maharlika', '09978377821', '2022-12-14 11:00 PM', '2022-12-15 11:00 AM', 0, 'Active'),
(16, 'moduk', 20, 'chambogwan', '098393901', '2022-12-14 11:02 PM', '2022-12-15 11:02 PM', 0, 'Active'),
(17, 'master', 20, 'matina', '02948248429', '2022-12-14 11:04 PM', '2022-12-15 11:04 PM', 0, 'Active'),
(18, 'marikit', 20, 'kwkwr', '09348384384', '2022-12-14 11:05 PM', '2022-12-15 10:05 AM', 0, 'Active'),
(22, 'cris', 30, 'purkok', '09822727281', '2022-12-19 12:15 PM', '2022-12-20 1:00 PM', 24, 'Active'),
(23, 'gand', 20, 'bayabas', '0929323021', '2022-12-15 4:20 PM', '2022-12-16 3:20 PM', 23, 'Inactive'),
(24, 'barney', 22, 'kidapawan', '0938378291', '2022-12-17 6:29 PM', '2022-12-18 5:00 PM', 22, 'Inactive'),
(25, 'lilis', 39, 'matina', '987861272733', '2022-12-19 1:03 PM', '2022-12-20 2:30 PM', 25, 'Active'),
(26, 'lilia', 29, 'crossing', '0399359359', '2022-12-19 1:08 PM', '2022-12-20 2:08 PM', 25, 'Inactive'),
(27, 'melvz', 24, 'tibungco', '0394934091', '2022-12-19 1:35 PM', '2022-12-20 1:35 PM', 24, 'Active');

-- --------------------------------------------------------

--
-- Table structure for table `patient_doc`
--

CREATE TABLE `patient_doc` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `age` int(6) NOT NULL,
  `address` varchar(255) NOT NULL,
  `privilages` varchar(255) NOT NULL,
  `status` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `patient_doc`
--

INSERT INTO `patient_doc` (`id`, `name`, `age`, `address`, `privilages`, `status`) VALUES
(13, 'Angelo', 19, 'Balya', 'Patient', 'Inactive'),
(14, 'le', 29, 'bajaede', 'Doctor', 'Active'),
(15, 'Marie', 22, 'Purok 8', 'Doctor', 'Inactive'),
(18, 'Marie', 22, 'Purok 8', 'Patient', 'Inactive'),
(19, 'hanz', 20, 'ubalde', 'Patient', 'Active'),
(20, '123', 123, '123', 'Patient', 'Active'),
(21, '103', 10, '102', 'Patient', 'Active'),
(22, '10', 19, '10', 'Patient', 'Active'),
(23, 'aw', 0, 'we', 'Patient', 'Active'),
(24, 'glaw', 0, 'kawe', 'Patient', 'Active'),
(25, 'raymond', 20, 'calinan', 'Patient', 'Active'),
(26, 'bernard', 20, 'agdao', 'Patient', 'Active'),
(27, 'Johnley', 20, 'Malagos', 'Patient', 'Active'),
(28, 'Joshua', 20, 'Bajada', 'Patient', 'Active'),
(31, 'Aj', 20, 'Maa', 'Patient', 'Active'),
(32, 'jaira', 2, 'skyal', 'Patient', 'Active'),
(33, 'kyla', 20, 'biao', 'Patient', 'Inactive'),
(34, 'hanzy', 30, 'samal', 'Patient', 'Active'),
(35, 'whity', 30, 'samalz', 'Patient', 'Active'),
(36, 'killer', 24, 'KAL', 'Doctor', 'Active'),
(37, 'glenn', 0, 'kwrkwr', 'Patient', 'Active'),
(38, 'benel', 20, 'baliok', 'Patient', 'Active'),
(39, 'melvz', 24, 'tibungco', 'Patient', 'Active'),
(40, 'melz', 24, 'tibungo', 'Patient', 'Active');

-- --------------------------------------------------------

--
-- Table structure for table `pay_bills`
--

CREATE TABLE `pay_bills` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `hours` int(255) NOT NULL,
  `pay` int(255) NOT NULL,
  `total` int(255) NOT NULL,
  `transition` int(255) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `pay_bills`
--

INSERT INTO `pay_bills` (`id`, `name`, `hours`, `pay`, `total`, `transition`) VALUES
(1, 'Bernard', 8, 7000, 6400, 600),
(2, 'janle', 12, 9000, 9600, 0),
(3, 'janle', 12, 25000, 9600, 15400),
(4, 'glenn', 12, 1000, 9600, 0),
(5, 'yoda', 12, 9000, 9600, 0),
(6, 'yoddda', 12, 15000, 9600, 5400),
(7, 'yodase', 12, 15000, 9600, 5400),
(8, 'gand', 23, 2000, 18400, 0),
(9, 'alma', 23, 1000, 18400, 0),
(10, 'qwerte', 13, 100, 10400, 0),
(11, 'ramon', 12, 50, 9600, 0),
(12, 'hehe', 12, 15000, 9600, 5400),
(13, 'marites', 12, 100, 9600, 0),
(14, 'mader', 12, 100, 9600, 0),
(15, 'watchiki', 12, 100, 9600, 0),
(16, 'dangu', 12, 100, 9600, 0),
(17, 'Zach', 8, 10000, 6400, 3600),
(19, 'barney', 22, 20000, 17600, 2400),
(20, 'nathan', 20, 15000, 7000, 8000),
(21, 'don', 24, 20000, 8400, 11600),
(22, 'macis', 24, 24000, 8400, 15600),
(23, 'melvz', 24, 20000, 8400, 11600);

-- --------------------------------------------------------

--
-- Table structure for table `register_log`
--

CREATE TABLE `register_log` (
  `id` int(11) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `register_log`
--

INSERT INTO `register_log` (`id`, `username`, `password`) VALUES
(1, 'bernard29', 'bernard'),
(2, 'bernard29', 'bernard'),
(3, 'glenn', '18'),
(4, 'gande', '12'),
(5, 'bernad29', 'bernard'),
(6, 'wewin', '123'),
(7, 'alma', '123'),
(8, 'barney', '123'),
(9, 'kyle', '123'),
(10, 'melz', '123'),
(11, 'melvz', '123');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `appointment`
--
ALTER TABLE `appointment`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `patient_doc`
--
ALTER TABLE `patient_doc`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `pay_bills`
--
ALTER TABLE `pay_bills`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `register_log`
--
ALTER TABLE `register_log`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `appointment`
--
ALTER TABLE `appointment`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- AUTO_INCREMENT for table `patient_doc`
--
ALTER TABLE `patient_doc`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

--
-- AUTO_INCREMENT for table `pay_bills`
--
ALTER TABLE `pay_bills`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT for table `register_log`
--
ALTER TABLE `register_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
