## 自建MySQL账号
-- 创建迁移专用账号（dts_user和Your_Password123需修改为您自己的数据库账号和密码） CREATE USER 'dts_user'@'%' IDENTIFIED BY 'Your_Password123'; -- 授予SELECT权限（用于结构迁移、全量迁移） GRANT SELECT ON *.* TO 'dts_user'@'%'; -- 授权增量迁移所需额外权限 GRANT REPLICATION CLIENT, REPLICATION SLAVE, SHOW VIEW ON *.* TO 'dts_user'@'%'; -- 允许DTS创建心跳表，用于推进Binlog位点，监控增量同步延迟 GRANT CREATE ON *.* TO 'dts_user'@'%'; FLUSH PRIVILEGES;
