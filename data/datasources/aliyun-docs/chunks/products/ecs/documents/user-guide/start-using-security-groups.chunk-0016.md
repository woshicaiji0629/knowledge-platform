### 删除安全组
警告
删除安全组是一个不可逆的操作，将永久删除安全组下所有规则。在执行删除操作前，请确保备份相关配置。
控制台
前往[ECS](https://ecs.console.aliyun.com/securityGroup)[控制台-安全组](https://ecs.console.aliyun.com/securityGroup)，在目标安全组的操作栏单击删除。
在删除安全组对话框中，确认信息后，单击确定。
如果安全组没有关联的ECS实例和弹性网卡，在删除安全组对话框中仍提示不可删除时，可以单击尝试强制删除。
API
调用[DeleteSecurityGroup](../developer-reference/api-ecs-2014-05-26-deletesecuritygroup.md)，删除安全组。
安全组在以下场景时无法删除：
已关联ECS实例或弹性网卡时无法删除，需先将其移除。
被其他安全组规则授权，需先删除授权规则。
[托管安全组](managed-security-groups.md)仅支持查看，不可删除。
开启了删除保护，请先关闭删除保护，然后再尝试操作。如果无法关闭删除保护则无法删除安全组。
在使用[DeleteSecurityGroup](../developer-reference/api-ecs-2014-05-26-deletesecuritygroup.md)接口删除安全组时返回错误码InvalidOperation.DeletionProtection，或使用控制台删除安全组看到类似删除保护的提示时，说明该安全组开启了删除保护功能。
