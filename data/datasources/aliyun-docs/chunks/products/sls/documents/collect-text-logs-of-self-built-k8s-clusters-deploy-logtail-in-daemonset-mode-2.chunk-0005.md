# 设置资源名，在当前 Kubernetes 集群内唯一。 spec: project: # 设置目标 Project 名称。 name: k8s-your-project config: # 设置 Logtail 采集配置。 inputs: # 设置 Logtail 采集配置里的输入插件 ... processors: # 设置 Logtail 采集配置的处理插件 ... flushers: # 设置 Logtail 采集配置里的输出插件 ... |
| --- | --- |
