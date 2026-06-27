## 相关API

| API | 描述 |
| --- | --- |
| [ModifyDBInstanceSpec - 变更](api-rds-2014-08-15-modifydbinstancespec-postgresql.md) [RDS](api-rds-2014-08-15-modifydbinstancespec-postgresql.md) [实例](api-rds-2014-08-15-modifydbinstancespec-postgresql.md) | 调用 [ModifyDBInstanceSpec](api-rds-2014-08-15-modifydbinstancespec-postgresql.md) 接口，将实例系列升级为集群系列。您需要将 DBInstanceClass 参数取值修改为需要升级的集群系列实例规格， Category 参数取值修改为 Cluster ，其他参数请按需配置。 |
| [DescribeDBInstanceAttribute - 查询实例详情](api-rds-2014-08-15-describedbinstanceattribute-postgresql.md) | 验证升级结果：调用 [DescribeDBInstanceAttribute](api-rds-2014-08-15-describedbinstanceattribute-postgresql.md) 接口，查看 Category 参数取值是否为 Cluster。 如果为 Cluster ，则升级成功。 |

该文章对您有帮助吗？
反馈
