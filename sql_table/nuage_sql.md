# Nuage Database Creation
### NSG License
```sql
CREATE TABLE `nsg_licenses` (
  `vsd_id` tinyint(2) NOT NULL,
  `lic_total` smallint(4) DEFAULT NULL,
  `lic_used` smallint(4) DEFAULT NULL,
  PRIMARY KEY (`vsd_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8
```
### ES Storage Mount Point
```sql
CREATE TABLE `es_storage` (
  `es_id` tinyint(2) NOT NULL,
  `storage_total` float DEFAULT NULL,
  `storage_used` float DEFAULT NULL,
  PRIMARY KEY (`es_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8
```

### NFV CPU Capacity
```sql
CREATE TABLE `nfv_cpu_cap` (
  `nfv_pod_id` tinyint(2) NOT NULL,
  `nfv_pod_name` char(10) DEFAULT NULL,
  `cpu_total` smallint(4) DEFAULT NULL,
  `cpu_used` smallint(4) DEFAULT NULL,
  PRIMARY KEY (`nfv_pod_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8
```

### VSC ESXi Capacity
```sql
CREATE TABLE `vsc_esxi_cap` (
  `vsc_pod_id` tinyint(1) NOT NULL,
  `vsc_pod_name` char(8) DEFAULT NULL,
  `host_count` tinyint(2) DEFAULT NULL,
  `vsc_count` tinyint(2) DEFAULT NULL,
  `vsc_cap` tinyint(3) DEFAULT NULL,
  PRIMARY KEY (`vsc_pod_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8
```

### IDC CPU Capacity
```sql
CREATE TABLE `idc_cpu_cap` (
  `idc_pod_id` tinyint(2) DEFAULT NULL,
  `idc_pod_name` char(10) DEFAULT NULL,
  `cpu_total` float DEFAULT NULL,
  `cpu_used` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8
```