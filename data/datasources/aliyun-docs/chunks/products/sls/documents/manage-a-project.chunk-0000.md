## 什么是Project
项目（Project）是日志服务的资源管理单元，用于资源隔离和控制。
Project中可包含LogStore、MetricStore和机器组等资源，同时它也是您访问日志服务资源的入口。建议使用不同的Project管理不同的应用、产品或项目中的数据。具体说明如下：
组织、管理不同的LogStore或MetricStore：在实际使用中，您可能需要使用日志服务采集及存储不同项目、产品或者环境的日志。您可以把不同项目、产品或者环境中的日志分类管理在不同Project中，便于后续的日志消费、导出或者分析。
用于访问控制隔离：您可以为RAM用户授予指定Project的操作权限。
提供日志服务资源的访问入口：日志服务为每个Project配置一个独立的访问入口。该访问入口支持通过网络写入、读取及管理日志。关于访问入口的更多信息，请参见[服务接入点](developer-reference/api-sls-2020-12-30-endpoint.md)。
权限须知（可展开）
若您使用阿里云主账号登录，默认拥有所有操作权限，可直接对Project进行相关操作。
若您使用RAM用户登录，请根据需要向主账号使用者申请如下两种日志服务的系统策略。
AliyunLogFullAccess：管理日志服务的权限。
AliyunLogReadOnlyAccess：只读访问日志服务的权限。
当系统策略无法满足您的需求，您可以参考下表通过[创建自定义权限策略](../../ram/documents/create-a-custom-policy.md)实现精细化权限管理。
