-- MySQL dump 10.16  Distrib 10.2.14-MariaDB, for Linux (x86_64)
--
-- Host: 127.0.0.1    Database: dev
-- ------------------------------------------------------
-- Server version	10.2.14-MariaDB-10.2.14+maria~jessie

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Dumping data for table `agency`
--

LOCK TABLES `agency` WRITE;
/*!40000 ALTER TABLE `agency` DISABLE KEYS */;
/*!40000 ALTER TABLE `agency` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `agencyareas`
--

LOCK TABLES `agencyareas` WRITE;
/*!40000 ALTER TABLE `agencyareas` DISABLE KEYS */;
/*!40000 ALTER TABLE `agencyareas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `agencycurrencys`
--

LOCK TABLES `agencycurrencys` WRITE;
/*!40000 ALTER TABLE `agencycurrencys` DISABLE KEYS */;
/*!40000 ALTER TABLE `agencycurrencys` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `agencyindustrys`
--

LOCK TABLES `agencyindustrys` WRITE;
/*!40000 ALTER TABLE `agencyindustrys` DISABLE KEYS */;
/*!40000 ALTER TABLE `agencyindustrys` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `agencyinveststages`
--

LOCK TABLES `agencyinveststages` WRITE;
/*!40000 ALTER TABLE `agencyinveststages` DISABLE KEYS */;
/*!40000 ALTER TABLE `agencyinveststages` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `agencyrounds`
--

LOCK TABLES `agencyrounds` WRITE;
/*!40000 ALTER TABLE `agencyrounds` DISABLE KEYS */;
/*!40000 ALTER TABLE `agencyrounds` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `agencytags`
--

LOCK TABLES `agencytags` WRITE;
/*!40000 ALTER TABLE `agencytags` DISABLE KEYS */;
/*!40000 ALTER TABLE `agencytags` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `area`
--

LOCK TABLES `area` WRITE;
/*!40000 ALTER TABLE `area` DISABLE KEYS */;
INSERT INTO `area` VALUES ('fa666e1e-e6a9-4505-bf4a-81f96f775d8e','上海'),('a17890cf-5921-4082-b301-7f411791acbf','北京'),('a92831e5-2fc4-40bd-bc93-a817d0da719c','广州'),('f38ae4c2-0643-4527-9a2a-296c8b8311cd','深圳');
/*!40000 ALTER TABLE `area` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `capitalproperty`
--

LOCK TABLES `capitalproperty` WRITE;
/*!40000 ALTER TABLE `capitalproperty` DISABLE KEYS */;
INSERT INTO `capitalproperty` VALUES ('418935ff-f72a-4a13-8caa-c73269c4d2f5','FOF'),('6a0e748b-83c4-4504-a018-1cf1b49654c4','上市企业'),('398a50d5-88e7-4fe5-a490-e93763166795','券商'),('0c452088-3700-47c3-a46f-a442919fb9eb','私募股权'),('dbb634f8-078f-4e47-a296-d7f57e11209d','银行'),('073527af-b17a-4e51-ac86-5a2dfbb4e017','非上市企业');
/*!40000 ALTER TABLE `capitalproperty` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `capitaltype`
--

LOCK TABLES `capitaltype` WRITE;
/*!40000 ALTER TABLE `capitaltype` DISABLE KEYS */;
INSERT INTO `capitaltype` VALUES ('9d39a942-bb5c-4bae-aa71-9d502f67f147','合资'),('33ba41bd-4d52-4051-820f-6b5fa1189fd0','外资'),('e071c3c0-8767-4b5a-9a09-64f251793666','本土');
/*!40000 ALTER TABLE `capitaltype` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `currency`
--

LOCK TABLES `currency` WRITE;
/*!40000 ALTER TABLE `currency` DISABLE KEYS */;
INSERT INTO `currency` VALUES ('1e603e8c-1ba6-4471-84f4-c508e654afda','人民币'),('fdc8f860-69f5-47d0-980c-b2ccfdea87bd','人民币+美元'),('744106f7-4a44-4251-81e0-15a665d3def6','美元');
/*!40000 ALTER TABLE `currency` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `industry`
--

LOCK TABLES `industry` WRITE;
/*!40000 ALTER TABLE `industry` DISABLE KEYS */;
INSERT INTO `industry` VALUES ('0402c812-0db9-49f5-b490-b1ba956f2f2f','文娱',NULL,'Industry'),('1d3bb1be-5daa-4292-af7f-97ccd81e81d2','教育',NULL,'Industry'),('4bd03976-ac5e-4adb-8011-ff6f344bebbf','大数据','74649c5b-643d-4bc2-a8c9-b570ec3c5f9f','SegmentIndustry'),('4fae6c8e-973f-49ad-ace6-b8a5e2720b91','金融',NULL,'Industry'),('74649c5b-643d-4bc2-a8c9-b570ec3c5f9f','互联网',NULL,'Industry'),('8687ba81-e8ec-4ea2-8cb3-854503f17bc0','体育',NULL,'Industry'),('96b43613-419c-4962-a3ce-8691ba0f0dc2','云计算','74649c5b-643d-4bc2-a8c9-b570ec3c5f9f','SegmentIndustry'),('e4f5fc5d-e1f9-47bb-961b-ea7cfc7ffd74','O2O','74649c5b-643d-4bc2-a8c9-b570ec3c5f9f','SegmentIndustry');
/*!40000 ALTER TABLE `industry` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `investstage`
--

LOCK TABLES `investstage` WRITE;
/*!40000 ALTER TABLE `investstage` DISABLE KEYS */;
INSERT INTO `investstage` VALUES ('d3ca96f0-ed13-4933-9b6d-d59ec329274d','初创期'),('9d486954-d105-4d32-8891-49bbfda07444','成熟期'),('78f8b46a-0602-492f-8c80-61797e4d3506','成长期'),('0f1897a9-92a8-485b-9df7-41ae21f55593','种子期');
/*!40000 ALTER TABLE `investstage` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `round`
--

LOCK TABLES `round` WRITE;
/*!40000 ALTER TABLE `round` DISABLE KEYS */;
INSERT INTO `round` VALUES ('a8ba33b0-cb84-4d65-823d-e3295ed93412','A轮'),('2afa5556-5bdd-4cb1-a504-115a8b2d87b8','B轮'),('b7b6ae38-19e0-453b-bf26-071950eeac19','C轮'),('dae2765b-7c45-4e9c-882d-4e80d53a6db3','D轮'),('f8aa5a1e-b4e4-459f-af37-f98efb66467f','F轮'),('4838b42c-6fdd-469a-8e5e-64c54edfdbff','Post-IPO'),('8a57b590-1e84-4ba7-939f-b021a66dcd9c','Pre-IPO'),('17420c17-6ebf-4791-82e5-5abd6ec416b2','天使轮');
/*!40000 ALTER TABLE `round` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `stageproperty`
--

LOCK TABLES `stageproperty` WRITE;
/*!40000 ALTER TABLE `stageproperty` DISABLE KEYS */;
INSERT INTO `stageproperty` VALUES ('b427026c-9ae0-4927-b92a-c03fc3b004a0','PE'),('943abef9-bafa-4d3f-9df1-f657911c4832','VC'),('a8a12e11-c96e-43e4-ae4a-8d373a68e3bc','VC+PE');
/*!40000 ALTER TABLE `stageproperty` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `tag`
--

LOCK TABLES `tag` WRITE;
/*!40000 ALTER TABLE `tag` DISABLE KEYS */;
INSERT INTO `tag` VALUES ('e446cd2f-b5da-4979-a069-42ed62a6ca15','人工智能'),('f7b4b566-b791-4254-a25f-318811af16a2','区块链');
/*!40000 ALTER TABLE `tag` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-05-11 19:26:33
