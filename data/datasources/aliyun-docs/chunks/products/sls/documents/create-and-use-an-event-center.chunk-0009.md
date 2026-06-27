## 步骤二：创建K8s事件中心实例
说明
创建K8s事件中心后，日志服务自动在目标Project中生成一个名为k8s-event的LogStore，并生成相关联的仪表盘等。
登录[日志服务控制台](https://sls.console.aliyun.com)。
在日志应用区域的智能运维页签中，单击K8S事件中心。
在事件中心管理页面，单击页面右上角的添加。
在创建事件中心面板，配置相关参数，然后单击下一步。
如果选择已有Project，则从Project下拉框中选择已创建的Project，用于管理K8s事件中心相关资源（LogStore、仪表盘等）。
如果选择从容器服务选择K8s集群，则从K8s集群下拉框中选择已创建的K8s集群。通过此方式创建K8s事件中心，日志服务默认创建一个名为k8s-log-{cluster-id}的Project，用于管理K8s事件中心相关资源（LogStore、仪表盘等）。
