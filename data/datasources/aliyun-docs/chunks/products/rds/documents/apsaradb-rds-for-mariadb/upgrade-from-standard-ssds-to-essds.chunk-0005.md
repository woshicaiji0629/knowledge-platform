## 常见问题
Q：变更配置时，是否会影响线上业务？
A：请参见[影响](../apsaradb-rds-for-mysql/upgrade-the-storage-type-of-an-apsaradb-rds-for-mysql-instance-from-standard-ssds-to-essds.md)。
Q：变更存储类型后，实例的地址会变化吗？
A：实例的连接地址（如rm-bpxxxxx.mysql.rds.aliyuncs.com）不会变化，但是对应的IP地址可能会变化。建议在应用程序中使用连接地址，而不是IP地址。
