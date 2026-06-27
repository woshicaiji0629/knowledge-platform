## 注意事项
TDE的开启粒度为实例级别，不支持Key（键）或DB（库）粒度的控制。
TDE加密对象为数据落盘文件（即RDB备份文件，如dump.rdb）。
TDE所使用的密钥，由[密钥管理服务](../../../kms/documents/key-management-service/support/what-is-key-management-service.md)[KMS](../../../kms/documents/key-management-service/support/what-is-key-management-service.md)（Key Management Service）统一生成和管理，云数据库 Tair（兼容 Redis）不提供加密所需的密钥和证书。
[实例回收站](manage-instances-in-the-recycle-bin.md)不支持恢复已开启TDE的实例。
