## 控制台
删除前清理
无关联资源：
在弹性计算、存储服务、安全、数据库等多种阿里云云产品开通日志分析服务，会在日志服务控制台自动创建对应的Project和LogStore。如果不需要云产品日志，需要在对应云产品控制台关闭日志分析服务。确保Project与其他阿里云服务无关联。
无计费依赖：Project若为付费类型（如存储包、预留实例），需先退订或释放资源。
删除步骤
备份重要数据（可选）
LogStore数据备份：若Project中包含需保留的日志数据，需通过SLS的[下载日志](download-logs.md)功能提前导出。
配置信息备份：记录Project名称、存储容量、访问控制等关键配置，避免删除后信息丢失。
执行Project删除
在Project列表中，单击目标Project对应的删除。
出现ProjectDeletionNotAllowe的处理方法
故障现象：删除 Project 时，系统提示ProjectDeletionNotAllowed错误。
原因：Project 已开启删除保护功能。删除保护是防止 Project 被意外删除的安全机制，开启后无法通过控制台或 API 直接删除 Project。
解决方法：需先关闭删除保护，然后再执行删除操作。
登录[日志服务控制台](https://sls.console.aliyun.com)，在 Project 列表区域单击目标 Project。在 Project 页面的项目概览-基础信息中，找到删除保护开关，将其关闭。
在删除Project面板中，输入Project名称并选择删除原因，然后单击确定。
警告
删除Project后，其管理的所有日志数据及配置信息都会被释放，不可恢复。在删除Project前请慎重确认，避免数据丢失。
确认操作：阅读提示后，输入Project名称进行二次确认。
若目标Project已开启Project回收站功能，您可在Project列表的回收站Project中查看，Project进入回收站后，默认保存7天，在此期间您可以选择恢复或者彻底删除。
删除后状态确认
删除操作是异步执行的，提交删除请求后，Project 会在后台逐步清理。若删除后再次尝试删除同一 Project 时提示"Project 不存在"，通常表示该 Project 已成功删除。
建议访问[日志服务控制台](https://sls.console.aliyun.com/lognext/profile)，在 Project 列表中查看目标 Project 是否已消失。若列表为空，则代表该地域的 Project 资源已全部清理。
若已开启回收站功能，还需在回收站Project列表中确认目标 Project 是否已被彻底删除或恢复。
