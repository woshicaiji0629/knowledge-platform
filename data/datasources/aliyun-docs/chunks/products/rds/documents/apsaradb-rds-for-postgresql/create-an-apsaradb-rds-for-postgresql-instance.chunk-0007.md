nstances.md) 。 | 创建实例时，存储类型选择云盘，选中 [云盘加密](../apsaradb-rds-for-mysql/configure-the-disk-encryption-feature-for-an-apsaradb-rds-for-mysql-instance.md) 并设置密钥后重试。 |

创建RDS PostgreSQL实例时，售卖页报错SLR不存在，用户需要先创建SLR。如何解决？
首次创建RDS PostgreSQL实例时，您需要单击售卖页SLR授权配置项右侧的按钮，去授权服务关联角色（[AliyunServiceRoleForRdsPgsqlOnEcs](../developer-reference/service-linked-roles.md)），允许RDS服务通过该角色完成弹性网卡的挂载动作，进而打通网络链路，该授权不会产生任何相关费用。
