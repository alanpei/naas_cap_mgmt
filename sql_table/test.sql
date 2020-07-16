/*
SQLyog Ultimate v13.1.1 (64 bit)
MySQL - 5.7.30 : Database - capmgmt_nuage
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`capmgmt_nuage` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `capmgmt_nuage`;

/*Table structure for table `es_storage` */

DROP TABLE IF EXISTS `es_storage`;

CREATE TABLE `es_storage` (
  `es_id` tinyint(2) NOT NULL,
  `storage_total` float DEFAULT NULL,
  `storage_used` float DEFAULT NULL,
  PRIMARY KEY (`es_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `es_storage` */

insert  into `es_storage`(`es_id`,`storage_total`,`storage_used`) values 
(1,14,4);

/*Table structure for table `idc_cpu_cap` */

DROP TABLE IF EXISTS `idc_cpu_cap`;

CREATE TABLE `idc_cpu_cap` (
  `idc_pod_id` tinyint(2) NOT NULL,
  `idc_pod_name` char(10) DEFAULT NULL,
  `cpu_total` smallint(4) DEFAULT NULL,
  `cpu_used` smallint(4) DEFAULT NULL,
  PRIMARY KEY (`idc_pod_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `idc_cpu_cap` */

insert  into `idc_cpu_cap`(`idc_pod_id`,`idc_pod_name`,`cpu_total`,`cpu_used`) values 
(1,'KIDC',50,20);

/*Table structure for table `nfv_cpu_cap` */

DROP TABLE IF EXISTS `nfv_cpu_cap`;

CREATE TABLE `nfv_cpu_cap` (
  `nfv_pod_id` tinyint(2) NOT NULL,
  `nfv_pod_name` char(10) DEFAULT NULL,
  `cpu_total` smallint(4) DEFAULT NULL,
  `cpu_used` smallint(4) DEFAULT NULL,
  PRIMARY KEY (`nfv_pod_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `nfv_cpu_cap` */

insert  into `nfv_cpu_cap`(`nfv_pod_id`,`nfv_pod_name`,`cpu_total`,`cpu_used`) values 
(1,'Hood2',200,130);

/*Table structure for table `nsg_licenses` */

DROP TABLE IF EXISTS `nsg_licenses`;

CREATE TABLE `nsg_licenses` (
  `vsd_id` tinyint(2) NOT NULL,
  `lic_total` smallint(4) DEFAULT NULL,
  `lic_used` smallint(4) DEFAULT NULL,
  PRIMARY KEY (`vsd_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `nsg_licenses` */

insert  into `nsg_licenses`(`vsd_id`,`lic_total`,`lic_used`) values 
(1,6000,3000);

/*Table structure for table `vsc_esxi_cap` */

DROP TABLE IF EXISTS `vsc_esxi_cap`;

CREATE TABLE `vsc_esxi_cap` (
  `vsc_pod_id` tinyint(1) NOT NULL,
  `vsc_pod_name` char(8) DEFAULT NULL,
  `host_count` tinyint(2) DEFAULT NULL,
  `vsc_count` tinyint(2) DEFAULT NULL,
  `vsc_cap` tinyint(3) DEFAULT NULL,
  PRIMARY KEY (`vsc_pod_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `vsc_esxi_cap` */

insert  into `vsc_esxi_cap`(`vsc_pod_id`,`vsc_pod_name`,`host_count`,`vsc_count`,`vsc_cap`) values 
(1,'Barlow',11,30,70),
(2,'Hood',11,30,70);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
