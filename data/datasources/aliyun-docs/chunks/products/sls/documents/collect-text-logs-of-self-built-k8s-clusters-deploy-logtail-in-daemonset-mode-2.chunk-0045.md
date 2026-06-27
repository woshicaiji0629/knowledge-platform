# 检查Pod状态 kubectl get po -n kube-system | grep loongcollector-ds
同时，日志服务会自动创建如下资源，可登录[日志服务控制台](https://sls.console.aliyun.com/)查看。

| 资源类型 | 资源名称 | 作用 |
| --- | --- | --- |
| Project | values.yaml 文件中自定义的 projectName 的值 | 资源管理单元，隔离不同业务日志。 |
| 机器组 | k8s-group-${cluster_id} | 日志采集节点集合。 |

重要
LoongCollector 组件中将不会创建名为config-operation-log的LogStore，若已创建的将不再写入日志。
