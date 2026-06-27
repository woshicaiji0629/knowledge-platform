## 常见问题
Q：云盘版RDS MySQL实例存储空间手动缩容一般闪断多久？
A：会造成15秒的闪断。闪断过程中，与数据库、账号、网络等相关的大部分操作都无法执行，请尽量在业务低峰期执行缩容操作，并确保应用具备重连机制，重连机制需要在您的应用程序中设置。
Q：SSD云盘版RDS MySQL实例如何缩容？
A：SSD云盘版实例暂不支持缩容，且目前[SSD](../apsaradb-rds-for-mysql/standard-ssds-are-no-longer-available-for-purchase-for-some-rds-instances.md)[云盘已停止售卖](../apsaradb-rds-for-mysql/standard-ssds-are-no-longer-available-for-purchase-for-some-rds-instances.md)。您可以将SSD云盘升级到ESSD云盘后，再参见本文操作进行缩容。
