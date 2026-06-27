## 内置角色授权
对同一个阿里云账号的不同日志库和时序库进行告警监控时，使用内置角色授权。
在高级配置页签中，将授权方式配置为内置角色。如果是首次配置，需要使用阿里云主账号[按照页面提示完成授权](https://ram.console.aliyun.com/role/authorization?request=%7B%22Services%22%3A%5B%7B%22Service%22%3A%22Log%22%2C%22Roles%22%3A%5B%7B%22RoleName%22%3A%22AliyunSLSAlertMonitorRole%22%2C%22TemplateId%22%3A%22AliyunSLSAlertMonitorRole%22%7D%5D%7D%5D%2C%22ReturnUrl%22%3A%22https%3A%2F%2Fsls.console.aliyun.com%2Flognext%2Fproject%2Flog-service-1984268643269815-cn-wulanchabu%2Falertcenter%22%7D)。授权后，日志服务将创建名称为AliyunSLSAlertMonitorRole的RAM角色，日志服务将扮演此角色以读取源日志库中的数据。单击高级配置页签，在授权方式下拉框中选择内置角色。
