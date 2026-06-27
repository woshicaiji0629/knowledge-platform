### Kubernetes 原生存储卷
Kubernetes原生存储卷的生命周期通常与Pod绑定，不适用于需要持久化保存应用数据的场景。

| 类型 | 说明 | 核心特点 |
| --- | --- | --- |
| emptyDir | 与 Pod 生命周期相同的临时空目录。 | Pod 删除后数据即丢失。可用于 Pod 内容器间数据交换或临时缓存。 |
| HostPath | 将节点宿主机上的文件或目录挂载到 Pod 中。可通过 type 字段（如 DirectoryOrCreate ）控制挂载前的检查和创建行为。 详见 [HostPath](use-hostpath-volumes.md) [数据卷](use-hostpath-volumes.md) | 数据与节点绑定，不随 Pod 迁移。不适用于需要高可用和持久化存储的有状态应用（如数据库、缓存）。 |
| ConfigMap/Secret | 以文件形式挂载配置项或敏感凭据。 | 仅用于存储小体积配置数据，非业务数据。用于将配置与应用解耦。 |
