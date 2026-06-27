# 检查Pod状态 kubectl get po -n kube-system | grep loongcollector-ds
返回结果示例：
loongcollector-ds-gnmnh 1/1 Running 0 63s
若组件未成功启动（非Running）:
检查配置：请确认values.yaml配置项是否正确。
检查镜像：通过如下命令查看Events确认容器镜像是否成功拉取。
kubectl describe pod loongcollector-ds -n kube-system
组件安装成功后，日志服务会自动创建如下资源，您可登录[日志服务控制台](https://sls.console.aliyun.com/)查看。

| 资源类型 | 资源名称 | 作用 |
| --- | --- | --- |
| Project | values.yaml 文件中自定义的 projectName 的值 | 资源管理单元，隔离不同业务日志。 |
| 机器组 | k8s-group-${cluster_id} | 日志采集节点集合。 |
| k8s-group-${cluster_id}-cluster | loongcollector-cluster 的机器组，主要用于指标采集场景。 |  |
| k8s-group-${cluster_id}-singleton | 单实例机器组，主要用于部分单实例采集配置。 |  |

重要
LoongCollector 组件中将不会创建名为config-operation-log的LogStore，若已创建的将不再写入日志。
