## 准备工作
由于阿里云账号（主账号）拥有资源的所有权限，其AccessKey一旦泄露风险巨大，所以建议您使用满足最小化权限需求的RAM用户的AccessKey。获取方法请参见[创建](../../../ram/documents/user-guide/create-an-accesskey-pair.md)[AccessKey](../../../ram/documents/user-guide/create-an-accesskey-pair.md)。
给RAM用户授予操作云服务器ECS和专有网络VPC相关资源的权限。本文提供的示例代码需要创建实例、VPC、交换机等资源，建议授予以下权限：

| 云产品 | 授予权限 |
| --- | --- |
| 专有网络 VPC | 本示例选择系统策略：AliyunVPCFullAccess |
| 云服务器 ECS | 本示例选择系统策略：AliyunECSFullAccess |
