## 在日志库页面通过查询语句查看
在容器内审计日志查询页面，通过查询语句查看详细的审计日志记录。
登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。
在集群列表页面，单击目标集群名称，然后在左侧导航栏，选择安全管理>审计。
在审计页面单击容器审计页签，然后单击容器内审计日志查询页签。
在输入框中输入查询和分析语句。
查询进入某个Pod的容器后执行的命令操作审计日志：输入* and k8s.pod.namespace: <namespace> and k8s.pod.name: <pod_name>，将<namespace>替换为Pod所在的命名空间，<pod_name>替换为Pod的名称。
查询执行指定程序的操作审计日志：输入* and process.name: <name>，将<name>替换为待查找的程序名称。
更多查询统计方式，请参见[日志服务查询分析方法](../../../../sls/documents/log-search-overview.md)。
设置查询分析的时间范围，然后单击查询/分析，查看分析结果。
