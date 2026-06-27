## 自定义角色授权（跨账号）
对跨阿里云账号下的不同日志库或指标库进行告警监控时，您可以通过自定义角色实现告警监控。例如在阿里云账号A中创建告警，监控阿里云账号B下的日志库或指标库。
在阿里云账号B进行以下操作：
[创建可信实体为阿里云服务的](../../ram/documents/user-guide/create-a-ram-role-for-a-trusted-alibaba-cloud-service.md)[RAM](../../ram/documents/user-guide/create-a-ram-role-for-a-trusted-alibaba-cloud-service.md)[角色](../../ram/documents/user-guide/create-a-ram-role-for-a-trusted-alibaba-cloud-service.md)，其中受信服务请选择日志服务。
修改RAM角色的信任策略。具体操作，请参见[修改](../../ram/documents/user-guide/edit-the-trust-policy-of-a-ram-role.md)[RAM](../../ram/documents/user-guide/edit-the-trust-policy-of-a-ram-role.md)[角色的信任策略](../../ram/documents/user-guide/edit-the-trust-policy-of-a-ram-role.md)。
重要
请根据实际情况替换阿里云账号A的ID。您可以在[账号中心](https://account.console.aliyun.com/v2/#/basic-info/index)中查看阿里云账号ID。
{ "Statement": [ { "Action": "sts:AssumeRole", "Effect": "Allow", "Principal": { "Service": [ "阿里云账号A的ID@log.aliyuncs.com", "log.aliyuncs.com" ] } } ], "Version": "1" }
创建一个自定义权限策略，其中在脚本编辑页签，请使用以下脚本替换配置框中的原有内容。具体操作，请参见[通过脚本编辑模式创建自定义权限策略](../../ram/documents/create-a-custom-policy.md)。
重要
将配置框中的原有脚本替换为如下内容。其中，Project名称需根据实际情况替换。如果您想要更细粒度的授权，例如只允许在指定Project下创建监控规则，则可以在下述策略的Resource中指定具体的Project，例如acs:log:*:*:project/my-project。
