## 使用模板变量丰富通知内容
您在配置内容模板时，可在标题或消息内容中添加模板变量。日志服务发送告警通知时，会将消息内容和标题中的模板变量替换为真实值。例如{{ alert.project }}替换为实际的Project名称。
每次产生告警时，系统自动生成告警上下文信息，存储于Results字段中。Results字段中的子字段都可作为模板变量。更多信息，请参见[内容模板语法（新版）](syntax-for-new-alert-templates.md)和[内容模板变量说明（新版）](variables-in-new-alert-templates.md)。
