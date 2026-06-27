## 常见问题
Q：云盘版RDS PostgreSQL实例存储空间缩容一般闪断多久？
A：缩容会造成30秒的闪断，闪断过程中，与数据库、账号、网络等相关的大部分操作都无法执行，请尽量在业务低峰期执行缩容操作。请确保应用具备重连机制，重连机制需要在您的应用程序中设置。
Q：SSD云盘的RDS PostgreSQL实例如何缩容？
A：SSD云盘已停止售卖，暂不支持缩容，您可以将SSD云盘升级到ESSD云盘后，再进行缩容。更多信息，请参见[【停售/下线】部分](../apsaradb-rds-for-mysql/standard-ssds-are-no-longer-available-for-purchase-for-some-rds-instances.md)[RDS](../apsaradb-rds-for-mysql/standard-ssds-are-no-longer-available-for-purchase-for-some-rds-instances.md)[实例不再提供](../apsaradb-rds-for-mysql/standard-ssds-are-no-longer-available-for-purchase-for-some-rds-instances.md)[SSD](../apsaradb-rds-for-mysql/standard-ssds-are-no-longer-available-for-purchase-for-some-rds-instances.md)[云盘售卖](../apsaradb-rds-for-mysql/standard-ssds-are-no-longer-available-for-purchase-for-some-rds-instances.md)。
