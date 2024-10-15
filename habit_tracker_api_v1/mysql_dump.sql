-- MySQL dump 10.13  Distrib 8.0.37, for Linux (x86_64)
--
-- Host: localhost    Database: track_habits_db
-- ------------------------------------------------------
-- Server version	8.0.37-0ubuntu0.22.04.3

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `accounts_customuser`
--

DROP TABLE IF EXISTS `accounts_customuser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounts_customuser` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `email` varchar(80) NOT NULL,
  `username` varchar(150) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_customuser`
--

LOCK TABLES `accounts_customuser` WRITE;
/*!40000 ALTER TABLE `accounts_customuser` DISABLE KEYS */;
INSERT INTO `accounts_customuser` VALUES (1,'pbkdf2_sha256$600000$KqK5tUIFenHMXr81CTCj8X$1ejsjKwn+6eI75BlIcxZXWyi7xN059fzEN8fWTnU1cM=','2024-10-14 19:34:38.382143',1,'','',1,1,'2024-10-12 08:16:17.892679','admin@app.com','default_username'),(2,'pbkdf2_sha256$600000$LR1Z6WMHkBYqOABsoxlLyt$10xsRRl7jZ2ONUL/4ZoqnkxpSBZd3pc+f1okuyRuc9c=',NULL,0,'','',0,1,'2024-10-12 08:19:00.065940','eabm@gmail.com','eabm'),(3,'pbkdf2_sha256$600000$Ep6WGgFyYsVZokCsTYQahv$VIVTRbon2e2llRPiC03PBmsFgbMFTMMOsJjdnxULFpw=',NULL,0,'','',0,1,'2024-10-12 08:19:15.889067','sno@gmail.com','sno'),(4,'pbkdf2_sha256$600000$hl3dqF69hNSM2GTBfgEho6$kFZdtUG7llbOjNMV3TRx91z/5OHptDQ48xjy9v+DAuE=',NULL,0,'','',0,1,'2024-10-12 08:19:35.381746','meybm@gmail.com','meybm'),(5,'pbkdf2_sha256$600000$GC2Mtko7iZ32gRFEuAq0Kb$eO+SmC6QOY4V+c/Xu+CjLj/IxTYdgFHdzFdigIbrkeE=',NULL,0,'','',0,1,'2024-10-14 19:36:08.023026','lioneljbmensah@gmail.com','jayb');
/*!40000 ALTER TABLE `accounts_customuser` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `accounts_customuser_groups`
--

DROP TABLE IF EXISTS `accounts_customuser_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounts_customuser_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `customuser_id` bigint NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `accounts_customuser_groups_customuser_id_group_id_c074bdcb_uniq` (`customuser_id`,`group_id`),
  KEY `accounts_customuser_groups_group_id_86ba5f9e_fk_auth_group_id` (`group_id`),
  CONSTRAINT `accounts_customuser__customuser_id_bc55088e_fk_accounts_` FOREIGN KEY (`customuser_id`) REFERENCES `accounts_customuser` (`id`),
  CONSTRAINT `accounts_customuser_groups_group_id_86ba5f9e_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_customuser_groups`
--

LOCK TABLES `accounts_customuser_groups` WRITE;
/*!40000 ALTER TABLE `accounts_customuser_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `accounts_customuser_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `accounts_customuser_user_permissions`
--

DROP TABLE IF EXISTS `accounts_customuser_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounts_customuser_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `customuser_id` bigint NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `accounts_customuser_user_customuser_id_permission_9632a709_uniq` (`customuser_id`,`permission_id`),
  KEY `accounts_customuser__permission_id_aea3d0e5_fk_auth_perm` (`permission_id`),
  CONSTRAINT `accounts_customuser__customuser_id_0deaefae_fk_accounts_` FOREIGN KEY (`customuser_id`) REFERENCES `accounts_customuser` (`id`),
  CONSTRAINT `accounts_customuser__permission_id_aea3d0e5_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_customuser_user_permissions`
--

LOCK TABLES `accounts_customuser_user_permissions` WRITE;
/*!40000 ALTER TABLE `accounts_customuser_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `accounts_customuser_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add content type',4,'add_contenttype'),(14,'Can change content type',4,'change_contenttype'),(15,'Can delete content type',4,'delete_contenttype'),(16,'Can view content type',4,'view_contenttype'),(17,'Can add session',5,'add_session'),(18,'Can change session',5,'change_session'),(19,'Can delete session',5,'delete_session'),(20,'Can view session',5,'view_session'),(21,'Can add habit',6,'add_habit'),(22,'Can change habit',6,'change_habit'),(23,'Can delete habit',6,'delete_habit'),(24,'Can view habit',6,'view_habit'),(25,'Can add user',7,'add_customuser'),(26,'Can change user',7,'change_customuser'),(27,'Can delete user',7,'delete_customuser'),(28,'Can view user',7,'view_customuser'),(29,'Can add Token',8,'add_token'),(30,'Can change Token',8,'change_token'),(31,'Can delete Token',8,'delete_token'),(32,'Can view Token',8,'view_token'),(33,'Can add token',9,'add_tokenproxy'),(34,'Can change token',9,'change_tokenproxy'),(35,'Can delete token',9,'delete_tokenproxy'),(36,'Can view token',9,'view_tokenproxy'),(37,'Can add habit log',10,'add_habitlog'),(38,'Can change habit log',10,'change_habitlog'),(39,'Can delete habit log',10,'delete_habitlog'),(40,'Can view habit log',10,'view_habitlog');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `authtoken_token`
--

DROP TABLE IF EXISTS `authtoken_token`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `authtoken_token` (
  `key` varchar(40) NOT NULL,
  `created` datetime(6) NOT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`key`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `authtoken_token_user_id_35299eff_fk_accounts_customuser_id` FOREIGN KEY (`user_id`) REFERENCES `accounts_customuser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `authtoken_token`
--

LOCK TABLES `authtoken_token` WRITE;
/*!40000 ALTER TABLE `authtoken_token` DISABLE KEYS */;
INSERT INTO `authtoken_token` VALUES ('27b3ba274ce953300c98eaf260e738e9f6363536','2024-10-14 19:36:08.897952',5),('4f09b376521490287136fbb5268496edcdfb1d0c','2024-10-12 08:19:16.442814',3),('7680ad5ee69b19433695af66f63d97afbcc760a8','2024-10-12 08:19:00.793245',2),('77c177ebce32fb30a9d676ecb245d304bcd29d20','2024-10-12 08:19:36.065680',4);
/*!40000 ALTER TABLE `authtoken_token` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_accounts_customuser_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_accounts_customuser_id` FOREIGN KEY (`user_id`) REFERENCES `accounts_customuser` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (7,'accounts','customuser'),(1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(8,'authtoken','token'),(9,'authtoken','tokenproxy'),(4,'contenttypes','contenttype'),(6,'habits','habit'),(10,'habits','habitlog'),(5,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2024-10-12 08:15:40.671936'),(2,'contenttypes','0002_remove_content_type_name','2024-10-12 08:15:40.862670'),(3,'auth','0001_initial','2024-10-12 08:15:41.961889'),(4,'auth','0002_alter_permission_name_max_length','2024-10-12 08:15:42.136527'),(5,'auth','0003_alter_user_email_max_length','2024-10-12 08:15:42.155599'),(6,'auth','0004_alter_user_username_opts','2024-10-12 08:15:42.178235'),(7,'auth','0005_alter_user_last_login_null','2024-10-12 08:15:42.209153'),(8,'auth','0006_require_contenttypes_0002','2024-10-12 08:15:42.220067'),(9,'auth','0007_alter_validators_add_error_messages','2024-10-12 08:15:42.252851'),(10,'auth','0008_alter_user_username_max_length','2024-10-12 08:15:42.281658'),(11,'auth','0009_alter_user_last_name_max_length','2024-10-12 08:15:42.305113'),(12,'auth','0010_alter_group_name_max_length','2024-10-12 08:15:42.358253'),(13,'auth','0011_update_proxy_permissions','2024-10-12 08:15:42.385368'),(14,'auth','0012_alter_user_first_name_max_length','2024-10-12 08:15:42.409184'),(15,'accounts','0001_initial','2024-10-12 08:15:43.563008'),(16,'accounts','0002_customuser_username_alter_customuser_email','2024-10-12 08:15:44.149288'),(17,'admin','0001_initial','2024-10-12 08:15:44.661826'),(18,'admin','0002_logentry_remove_auto_add','2024-10-12 08:15:44.726933'),(19,'admin','0003_logentry_add_action_flag_choices','2024-10-12 08:15:44.767397'),(20,'authtoken','0001_initial','2024-10-12 08:15:45.209193'),(21,'authtoken','0002_auto_20160226_1747','2024-10-12 08:15:45.296267'),(22,'authtoken','0003_tokenproxy','2024-10-12 08:15:45.307604'),(23,'habits','0001_initial','2024-10-12 08:15:45.812712'),(24,'habits','0002_remove_habit_completed_count_remove_habit_target_and_more','2024-10-12 08:15:47.371714'),(25,'habits','0003_habit_author','2024-10-12 08:15:47.731046'),(26,'habits','0004_remove_habit_author_remove_habit_reminder_time_and_more','2024-10-12 08:15:48.293168'),(27,'sessions','0001_initial','2024-10-12 08:15:48.424257'),(28,'habits','0005_habitlog','2024-10-13 08:39:53.872190'),(29,'accounts','0003_alter_customuser_username','2024-10-13 17:55:04.504248'),(30,'habits','0006_alter_habitlog_unique_together','2024-10-13 17:55:04.631584');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('3sycnhdnty8jr38e369b74tfdvr2r14v','.eJxVjEEOwiAQRe_C2pAptBRcuvcMZIYZpGpoUtqV8e7apAvd_vfef6mI21ri1mSJE6uz6tTpdyNMD6k74DvW26zTXNdlIr0r-qBNX2eW5-Vw_w4KtvKtrcfe9OLH7A0PwTnqu2QhIQF4a9CScQIIAZwbJRvOLB37EPKYiIas3h_OmjgD:1t0Qpy:6jVrMgQdm0LLjS8918FFlOBa48D5Ezt0dTbtWUKMRNg','2024-10-28 19:34:38.398235'),('ew1aw1rjptyt5262c3zrh32hcvgvodj1','.eJxVjEEOwiAQRe_C2pAptBRcuvcMZIYZpGpoUtqV8e7apAvd_vfef6mI21ri1mSJE6uz6tTpdyNMD6k74DvW26zTXNdlIr0r-qBNX2eW5-Vw_w4KtvKtrcfe9OLH7A0PwTnqu2QhIQF4a9CScQIIAZwbJRvOLB37EPKYiIas3h_OmjgD:1szuEo:pg2e1b6OP1EH0ydWbWD7S1BvVdFg7TyFnEL16Xx_FLk','2024-10-27 08:46:06.736953');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `habits_habit`
--

DROP TABLE IF EXISTS `habits_habit`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `habits_habit` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `description` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `start_date` date NOT NULL,
  `frequency` varchar(10) NOT NULL,
  `streak` int NOT NULL,
  `user_id` bigint NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `end_date` date DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `habits_habit_user_id_0cd069d6_fk_accounts_customuser_id` (`user_id`),
  CONSTRAINT `habits_habit_user_id_0cd069d6_fk_accounts_customuser_id` FOREIGN KEY (`user_id`) REFERENCES `accounts_customuser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `habits_habit`
--

LOCK TABLES `habits_habit` WRITE;
/*!40000 ALTER TABLE `habits_habit` DISABLE KEYS */;
INSERT INTO `habits_habit` VALUES (1,'Study Session','Keeping track of your thoughts and goals.','2024-10-12 12:44:04.095343','2024-11-01','daily',0,2,1,'2024-10-12 12:44:04.104135','2024-12-01'),(2,'Healthy Eating','A stretching routine to stay flexible.','2024-10-12 12:44:04.439065','2024-10-28','daily',0,2,1,'2024-10-12 12:44:04.439310','2024-11-27'),(3,'Reading','Ensuring you get adequate sleep each night.','2024-10-12 12:44:04.515531','2024-10-20','daily',0,2,1,'2024-10-12 12:44:04.515799','2024-11-19'),(4,'Morning Exercise','A stretching routine to stay flexible.','2024-10-12 12:44:04.652430','2024-11-09','weekly',1,2,1,'2024-10-13 08:44:22.509890','2025-01-04'),(5,'Drinking Water','Daily meditation for mindfulness.','2024-10-12 12:44:04.781032','2024-10-18','daily',0,2,1,'2024-10-12 12:44:04.781209','2024-11-17'),(6,'Sleep Early','Ensuring you get adequate sleep each night.','2024-10-12 12:44:04.838198','2024-10-14','weekly',0,2,1,'2024-10-12 12:44:04.838366','2024-12-09'),(7,'Yoga','A stretching routine to stay flexible.','2024-10-12 12:44:04.944749','2024-10-12','daily',0,2,1,'2024-10-12 12:44:04.945122','2024-11-11'),(8,'Study Session','Keeping track of your thoughts and goals.','2024-10-12 12:44:04.981001','2024-11-05','weekly',0,2,1,'2024-10-12 12:44:04.981217','2024-12-31'),(9,'Sleep Early','A stretching routine to stay flexible.','2024-10-12 12:44:05.023253','2024-10-29','weekly',0,2,1,'2024-10-12 12:44:05.023491','2024-12-24'),(10,'Meditation','A study session to improve skills and knowledge.','2024-10-12 12:44:05.065643','2024-10-31','daily',1,2,1,'2024-10-13 09:24:29.605215','2024-11-30'),(11,'Healthy Eating','Ensuring you get adequate sleep each night.','2024-10-12 12:44:05.100935','2024-11-01','weekly',0,4,1,'2024-10-12 12:44:05.101140','2024-12-27'),(12,'Yoga','A daily routine to improve mental and physical health.','2024-10-12 12:44:05.139898','2024-10-30','daily',0,4,1,'2024-10-12 12:44:05.140116','2024-11-29'),(13,'Meditation','A daily routine to improve mental and physical health.','2024-10-12 12:44:05.183876','2024-10-31','weekly',0,4,1,'2024-10-12 12:44:05.184115','2024-12-26'),(14,'Drinking Water','A study session to improve skills and knowledge.','2024-10-12 12:44:05.236226','2024-11-07','weekly',0,4,1,'2024-10-12 12:44:05.236468','2025-01-02'),(15,'Journaling','Keeping track of your thoughts and goals.','2024-10-12 12:44:05.316231','2024-10-21','daily',0,4,1,'2024-10-12 12:44:05.316445','2024-11-20'),(16,'Journaling','A daily routine to improve mental and physical health.','2024-10-12 12:44:05.354567','2024-11-07','daily',0,4,1,'2024-10-12 12:44:05.354794','2024-12-07'),(17,'Morning Exercise','Daily yoga for mental and physical relaxation.','2024-10-12 12:44:05.446640','2024-11-05','daily',0,4,1,'2024-10-12 12:44:05.447081','2024-12-05'),(18,'Yoga','A stretching routine to stay flexible.','2024-10-12 12:44:05.503106','2024-10-14','weekly',0,4,1,'2024-10-12 12:44:05.503366','2024-12-09'),(19,'Healthy Eating','Keeping track of your thoughts and goals.','2024-10-12 12:44:05.534684','2024-10-13','weekly',0,4,1,'2024-10-12 12:44:05.534912','2024-12-08'),(20,'Drinking Water','A stretching routine to stay flexible.','2024-10-12 12:44:05.581999','2024-10-19','daily',0,4,1,'2024-10-12 12:44:05.582186','2024-11-18'),(21,'Morning Exercise','Daily meditation for mindfulness.','2024-10-12 12:44:05.619439','2024-10-28','weekly',0,3,1,'2024-10-12 12:44:05.619701','2024-12-23'),(22,'Study Session','Focusing on personal development through reading.','2024-10-12 12:44:05.652463','2024-10-12','daily',0,3,1,'2024-10-12 12:44:05.652728','2024-11-11'),(23,'Sleep Early','Focusing on personal development through reading.','2024-10-12 12:44:05.727549','2024-10-26','weekly',0,3,1,'2024-10-12 12:44:05.727860','2024-12-21'),(24,'Journaling','Daily yoga for mental and physical relaxation.','2024-10-12 12:44:05.856717','2024-10-29','weekly',0,3,1,'2024-10-12 12:44:05.857324','2024-12-24'),(25,'Drinking Water','A study session to improve skills and knowledge.','2024-10-12 12:44:05.955658','2024-10-30','daily',0,3,1,'2024-10-12 12:44:05.955917','2024-11-29'),(26,'Yoga','A daily routine to improve mental and physical health.','2024-10-12 12:44:05.993503','2024-10-23','weekly',0,3,1,'2024-10-12 12:44:05.993673','2024-12-18'),(27,'Journaling','Focusing on personal development through reading.','2024-10-12 12:44:06.053867','2024-11-06','weekly',0,3,1,'2024-10-12 12:44:06.054033','2025-01-01'),(28,'Yoga','Staying hydrated by drinking water regularly.','2024-10-12 12:44:06.087559','2024-10-17','daily',0,3,1,'2024-10-12 12:44:06.087760','2024-11-16'),(29,'Stretching','A daily routine to improve mental and physical health.','2024-10-12 12:44:06.122261','2024-10-28','weekly',0,3,1,'2024-10-12 12:44:06.122498','2024-12-23'),(30,'Drinking Water','A study session to improve skills and knowledge.','2024-10-12 12:44:06.163942','2024-11-09','weekly',0,3,1,'2024-10-12 12:44:06.164117','2025-01-04'),(31,'Morning Pages','Writing morning pages daily.','2024-10-14 19:41:55.014454','2024-10-15','daily',0,5,1,'2024-10-14 19:41:55.027833','2024-11-14'),(32,'10 Minute Meditation','Daily 10-minute meditation.','2024-10-14 19:42:48.742130','2024-10-15','daily',0,5,1,'2024-10-14 19:42:48.806950','2024-11-14'),(33,'Cycle for 20 mins','20-minute cycling session daily.','2024-10-14 19:43:02.588660','2024-10-15','daily',0,5,1,'2024-10-14 19:43:02.613786','2024-11-14'),(34,'Daily Bible Meditation','Daily meditation on the Bible.','2024-10-14 19:43:12.787425','2024-10-15','daily',0,5,1,'2024-10-14 19:43:12.797483','2024-11-14'),(35,'100 days of Podcast','Listening to a podcast every day for 100 days.','2024-10-14 19:43:27.397962','2024-10-15','daily',0,5,1,'2024-10-14 19:43:27.459055','2024-11-14'),(36,'2 hour Coding session','Daily 2-hour coding practice.','2024-10-14 19:43:39.544310','2024-10-15','daily',0,5,1,'2024-10-14 19:43:39.605758','2024-11-14'),(37,'30 Minutes Read (Atomic Habits)','Reading Atomic Habits for 30 minutes daily.','2024-10-14 19:43:55.856459','2024-10-15','daily',0,5,1,'2024-10-14 19:43:55.877552','2024-11-14'),(38,'Track Expense','Daily tracking of expenses.','2024-10-14 19:44:12.970187','2024-10-15','daily',0,5,1,'2024-10-14 19:44:13.034908','2024-11-14'),(39,'100 days of Code','Daily coding session for 100 days.','2024-10-14 19:44:22.709362','2024-10-15','daily',0,5,1,'2024-10-14 19:44:22.719750','2024-11-14'),(40,'Kiss Family','Showing affection to family members daily.','2024-10-14 19:44:30.779882','2024-10-15','daily',0,5,1,'2024-10-14 19:44:30.835344','2024-11-14');
/*!40000 ALTER TABLE `habits_habit` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `habits_habitlog`
--

DROP TABLE IF EXISTS `habits_habitlog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `habits_habitlog` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `log_date` date NOT NULL,
  `status` varchar(20) NOT NULL,
  `note` longtext,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `habit_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `habits_habitlog_habit_id_log_date_a39a98b4_uniq` (`habit_id`,`log_date`),
  CONSTRAINT `habits_habitlog_habit_id_2cc59f74_fk_habits_habit_id` FOREIGN KEY (`habit_id`) REFERENCES `habits_habit` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `habits_habitlog`
--

LOCK TABLES `habits_habitlog` WRITE;
/*!40000 ALTER TABLE `habits_habitlog` DISABLE KEYS */;
INSERT INTO `habits_habitlog` VALUES (1,'2024-10-13','completed','This was well done','2024-10-13 08:44:22.498093','2024-10-13 08:44:22.498134',4),(2,'2024-10-13','completed','Meditation Done','2024-10-13 09:24:29.526704','2024-10-13 09:24:29.526755',10);
/*!40000 ALTER TABLE `habits_habitlog` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-10-15 13:33:38
