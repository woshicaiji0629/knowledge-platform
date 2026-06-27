## （可选）步骤三：查看详细日志记录
如果您有自定义查询、分析审计日志的需求，可以进入日志服务管理控制台查看详细的日志记录。
说明
ACK托管集群集群的API Server审计日志在日志服务中对应的日志库数据默认保存时间为30天，ACK专有集群对应的默认保存时间为365天。如需修改日志的默认保存时间，请参见[管理](../../../../sls/documents/manage-a-logstore.md)[LogStore](../../../../sls/documents/manage-a-logstore.md)。
登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。
在集群列表页面，单击目标集群名称，然后在左侧导航栏，选择集群信息。
单击基本信息页签，单击日志服务 Project对应的Project ID，然后在Project列表区域，单击名为audit-${clustered}的日志库（Logstore）。
在集群创建过程中，指定的日志Project中会自动添加一个名为audit-${clustereid}的日志库。
重要
审计日志的Logstore默认已经配置好索引。请勿修改索引，以免报表失效。
在输入框中输入查询和分析语句，并配置查询分析的时间范围，例如最近15分钟，然后单击查询/分析，查看查询分析结果。
常见的审计日志搜索方式如下：
查询某一RAM用户的操作记录：输入RAM用户ID，单击查询/分析。
查询某一资源的操作：输入集群计算、网络、存储、访问控制资源的名称，单击查询/分析。
过滤掉系统组件的操作，输入NOT user.username: node NOT user.username: serviceaccount NOT user.username: apiserver NOT user.username: kube-scheduler NOT user.username: kube-controller-manager，然后单击查询/分析。
更多查询、统计方式，请参见[日志服务查询分析方法](../../../../sls/documents/log-search-overview.md)。
