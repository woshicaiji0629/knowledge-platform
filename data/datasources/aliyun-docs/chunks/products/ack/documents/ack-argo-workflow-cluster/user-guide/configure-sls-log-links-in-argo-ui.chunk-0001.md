## 操作步骤
登录[容器](https://csnew.console.aliyun.com/#/next/argowf)[Argo](https://csnew.console.aliyun.com/#/next/argowf)[工作流集群控制台](https://csnew.console.aliyun.com/#/next/argowf)，单击目标集群名称。
在左侧导航栏选择配置管理，单击workflow controller配置（YAML）。
替换下方模板中的clusterid为集群ID，region为集群所在地域（例如：cn-hangzhou），然后在编辑workflow controller配置页面，填入YAML文件中data部分：
NAMESPACE: 当前工作流 / Pod / 事件源（Event Source） / 传感器（Sensor）所在的 Kubernetes 命名空间。
NAME: 当前工作流 / Pod / 事件源 / 传感器的名称。
${status.startedAt}: 工作流 / Pod 的开始时间戳，格式为2021-01-01T10:35:56Z。
${status.finishedAt}: 工作流 / Pod 的结束时间戳，格式为2021-01-01T10:35:56Z。
如果工作流或 Pod 仍在运行，该变量的值将为null。
links:| # Adds a button to the workflow page. E.g. linking to you logging facility. - name: Workflow Logs scope: workflow url: https://sls.console.aliyun.com/lognext/project/k8s-log-{clusterid}/logsearch/workflow-controller-{clusterid}?slsRegion={region}&queryTimeType=3&queryString=NAME# Adds a button next to the pod. E.g. linking to you logging facility but for the pod only. - name: Pod Logs scope: pod url: https://sls.console.aliyun.com/lognext/project/k8s-log-{clusterid}/logsearch/workflow-logstore?slsRegion={region}&queryTimeType=3&queryString=_pod_name_=NAMEand _namespace_=NAMESPACE
在工作流集群中重启A
