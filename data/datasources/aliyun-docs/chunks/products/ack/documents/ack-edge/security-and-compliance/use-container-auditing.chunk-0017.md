## 关闭容器内部操作审计功能
可通过卸载ack-advanced-audit组件关闭容器内部操作审计功能。
重要
关闭容器内部操作审计功能，不会删除自动创建的advaudit-${cluster_id}日志库，需要登录[日志服务控制台](https://sls.console.aliyun.com)手动删除该日志库，请参见[停止计费/删除](../../../../sls/documents/manage-a-logstore.md)[Logstore](../../../../sls/documents/manage-a-logstore.md)。
登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。
在集群列表页面，单击目标集群名称，然后在左侧导航栏，单击组件管理。
在组件管理页面，搜索ack-advanced-audit组件，单击组件右下方的卸载，按照页面提示完成卸载。
