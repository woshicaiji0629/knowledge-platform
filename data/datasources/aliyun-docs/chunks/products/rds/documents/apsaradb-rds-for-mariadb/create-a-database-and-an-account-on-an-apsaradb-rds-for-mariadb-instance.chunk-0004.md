## 创建数据库
访问[RDS](https://rdsnext.console.aliyun.com/rdsList/basic)[实例列表](https://rdsnext.console.aliyun.com/rdsList/basic)，在上方选择地域，然后单击目标实例ID。
在左侧导航栏中，选择数据库管理。
单击创建数据库。
设置以下参数。

| 参数 | 说明 |
| --- | --- |
| 数据库（DB）名称 | 以字母开头，以字母或数字结尾； 由小写字母、数字、下划线或中划线组成； 长度为 2~64 个字符。 |
| 支持字符集 | 数据库的字符集。 |
| 授权账号 | 选中需要访问本数据库的账号。本参数可以留空，在创建数据库后再 [修改或重置账号权限](modify-the-permissions-of-a-standard-account-on-an-apsaradb-rds-for-mariadb-instance.md) 。 说明 此处只会显示 普通账号 ，因为高权限账号拥有所有数据库的所有权限，不需要授权。 |
| 备注说明 | 非必填。用于备注该数据库的相关信息，便于后续数据库管理，最多支持 256 个字符。 |

单击创建。
