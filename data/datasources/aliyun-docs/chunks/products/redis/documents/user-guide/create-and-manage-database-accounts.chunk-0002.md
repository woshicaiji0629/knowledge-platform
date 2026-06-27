## 操作步骤
访问[实例列表](https://kvstore.console.aliyun.com/Redis/instance/cn-hangzhou)，在上方选择地域，然后单击目标实例ID。
在左侧导航栏，单击账号管理。
单击页面右侧的创建账号。
在弹出的对话框中，设置账号信息。

| 配置 | 说明 |
| --- | --- |
| 账号类型 | 本地账号 ：表示您需要额外记录该账号口令，或在应用代码中通过明文配置数据库账号口令。 KMS 托管账号 ：通过 [KMS](../../../kms/documents/key-management-service/product-overview/what-is-key-management-service-1.md) 托管实例的账号密码，应用程序将无需配置静态数据库账号口令，应用程序访问实例时，调用相关 KMS 接口获取实例账号和口令信息，更多信息请参见 [通过](../use-cases/use-kms-to-manage-redis-credentials.md) [KMS](../use-cases/use-kms-to-manage-redis-credentials.md) [托管实例密码凭证](../use-cases/use-kms-to-manage-redis-credentials.md) 。 |
| 账号 | 账号名需满足以下条件： 以英文字母开头，由小写英文字母、数字或下划线（_）组成。 长度不超过 35 个字符。 不能为 [Redis](create-and-manage-database-accounts.md) [账号名保留字](create-and-manage-database-accounts.md) 。 |
| 权限设置 | 设置该账号所拥有的权限： 只读 ：仅拥有读取数据的权限，不允许修改数据。 读写 ：拥有读、写以及删除数据的权限。 |
| 密码 | 设置该账号的密码，需满足以下条件： 由大写英文字母、小写英文字母、数字、特殊字符中的至少三种组成，特殊字符为： !@#$%^&*()+-=_ 长度为 8~32 个字符。 |
| 确认密码 | 再次输入密码进行确认。 |
| 备注 （可选） | 账号的备注信息，需满足以下条件： 以英文字母或中文开头，且不能以 http:// 或 https:// 开头。 由英文字母、中文、数字、下划线（_）或短划线（-）组成。 长度为 2~256 字符。 |
