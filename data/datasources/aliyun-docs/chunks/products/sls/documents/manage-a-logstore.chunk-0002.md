### 适用范围与权限
权限须知（可展开）
使用阿里云主账号登录，默认拥有所有操作权限，可直接对LogStore进行相关操作。
使用RAM用户登录，请根据需要向主账号使用者申请如下两种日志服务的系统策略。
AliyunLogFullAccess：管理日志服务的权限。
AliyunLogReadOnlyAccess：只读访问日志服务的权限。
当系统策略无法满足您的需求，您可以参考下表通过[创建自定义权限策略](../../ram/documents/create-a-custom-policy.md)实现精细化权限管理。

| 操作 | 所需权限 |
| --- | --- |
| 管理 LogStore | log:ListProject log:GetAcceleration log:ListDomains log:GetLogging log:ListTagResources log:GetProject log:ListLogStores log:*LogStore log:*Index log:ListShards log:GetLogStoreHistogram log:GetLogStoreContextLogs |
| 查询 LogStore | log:ListProject log:GetAcceleration log:ListDomains log:GetLogging log:ListTagResources log:GetProject log:ListLogStores log:GetLogStore log:GetLogStoreHistogram log:GetIndex log:CreateIndex log:UpdateIndex log:ListShards log:GetLogStoreContextLogs |
