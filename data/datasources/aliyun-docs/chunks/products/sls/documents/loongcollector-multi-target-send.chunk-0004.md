### 场景一：同文件内不同类型日志的分类存储
本场景将演示如何将同一个日志文件中的普通服务日志和审计日志分发到两个具有不同存储周期的日志库。
在配置管理页面，单击创建Logtail配置。
在快速数据接入弹窗中，单击单行 - 文本日志卡片的立即接入。
机器组配置，配置完成后单击下一步。
使用场景：主机场景
安装环境：ECS
选择机器组：选择目标主机所在的机器组并添加到应用机器组。如目标主机尚未安装LoongCollector，请参考[配置机器组（安装](host-text-log-collection-auto-install.md)[LoongCollector）](host-text-log-collection-auto-install.md)完成机器组配置。
Logtail配置，配置完成后单击下一步。
配置名称：自定义采集配置名称，在其所属Project内必须唯一。创建成功后，无法修改。
输入配置
文件路径：日志采集的路径。
Linux：以“/”开头，如/data/mylogs/**/*.log，表示/data/mylogs目录下所有后缀名为.Log的文件。
Windows：以盘符开头，如C:\Program Files\Intel\**\*.Log。
最大目录监控深度：文件路径中通配符**匹配的最大目录深度。默认为0，表示只监控本层目录。
处理配置
日志样例：单击添加日志样例，样例内容如下：其中包含action字段的为审计日志。
2025-10-28 11:22:21 INFO User test deleted a record | action=DELETE 2025-10-28 11:22:21 INFO Cache refreshed 2025-10-28 11:22:22 INFO User guest attempted unauthorized access | action=ACCESS_DENIED 2025-10-28 11:22:23 INFO Connected to database 2025-10-28 11:22:23 INFO User admin logged in | action=LOGIN 2025-10-28 11:22:24 INFO Connected to database 2025-10-28 11:22:25 INFO User guest attempted unauthorized access | action=ACCESS_DENIED 2025-10-28 11:22:26 INFO User test deleted a record | action=DELETE 2025-10-28 11:22:26 INFO Cache refreshed 2025-10-28 11:22:29
