## 函数计算（FC）
设置告警通知渠道为函数计算（FC），则告警触发后，日志服务会调用您所创建的函数。
注意事项
只支持非HTTP函数。如果是HTTP函数，请使用自定义Webhook方式。
只支持以sls-ops-开头的函数。
前提条件
已经在阿里云函数计算服务中创建服务以及函数（仅支持非HTTP函数）。更多信息，请参见[快速创建函数](https://help.aliyun.com/zh/functioncompute/fc-2-0/create-a-function-in-the-function-compute-console#multiTask782)。
如果您使用的是RAM用户，需先授予该RAM用户AliyunFCReadOnlyAccess权限。
配置参数
选择函数计算（FC）时，需在行动组对话框中完成如下配置。具体操作，请参见[行动策略](create-an-action-policy.md)。

| 参数 | 说明 |
| --- | --- |
| 渠道 | 选择 函数计算(FC) 。 |
| 地域 | 选择您已创建的函数的所在地域。 |
| 服务 | 选择您已创建的函数计算服务。 |
| 版本/别名 | 选择服务的版本或别名，默认为 LATEST。 |
| 函数 | 选择您已创建的函数。仅支持以 sls-ops-开头的函数。 |
| 内容模板 | 告警通知的内容。日志服务根据您所选择的内容模板，发送告警通知的内容。 |
| 发送时段 | 告警通知的发送时间。更多信息，请参见 [通知发送时段机制](periods-for-sending-alert-notifications.md) 。 |

该文章对您有帮助吗？
反馈
