## 执行巡检
登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。
在集群列表页面，单击目标集群名称，然后在左侧导航栏，选择安全管理>配置巡检。
可选：按照页面提示安装并升级巡检组件。
巡检组件security-inspector本身不计费，但会占用您的Pod资源。组件介绍及变更记录，请参见[security-inspector](../../product-overview/security-inspector.md)。
执行巡检。
重要
请在业务低峰期执行巡检操作。
默认巡检所有支持的检查项，您可以在配置巡检页面右上方，单击巡检配置，然后配置巡检时执行的检查项。更多信息，请参见[检查项](use-the-inspection-feature-to-detect-security-risks-in-the-workloads-of-an-ack-cluster.md)。
立即执行：在配置巡检页面右上方，单击立即执行巡检。
定期执行：在配置巡检页面右上方，单击巡检配置，然后选中定期巡检，并配置巡检周期。
等待巡检完成后，在巡检详情页签，单击巡检结果对应操作列中的详情，查看检查结果。
