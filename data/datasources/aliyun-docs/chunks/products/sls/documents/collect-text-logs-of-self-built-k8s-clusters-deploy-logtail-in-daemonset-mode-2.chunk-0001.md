## 适用范围
运行环境：
支持阿里云容器服务ACK（托管与专有版）和自建Kubernetes 集群。
Kubernetes为1.16.0及以上版本且支持Mount propagation: HostToContainer。
容器运行时（仅支持Docker与Containerd）
Docker：
需具备访问docker.sock的权限。
标准输出采集仅支持JSON类型的日志驱动。
存储驱动仅支持overlay、overlay2两种存储驱动（其他类型需手动挂载日志目录）。
Containerd：需具备访问containerd.sock的权限。
资源要求：LoongCollector（Logtail）以system-cluster-critical高优先级运行，集群资源不足时请勿部署，否则可能驱逐节点上原有的Pod。
CPU：至少预留0.1 Core。
内存：采集组件至少150MB，控制器组件至少100MB。
实际使用量与采集速率、监控目录和文件数量、发送阻塞程度有关，请保证实际使用率低于限制值的80%。
权限要求：部署使用的阿里云主账号或子账号需具备AliyunLogFullAccess权限。
如需自定义权限策略，请参考[AliyunCSManagedLogRolePolicy](../../ram/documents/developer-reference/aliyuncsmanagedlogrolepolicy.md)系统策略，将其包含的权限内容复制并赋予目标 RAM 用户或角色，以实现精细化的权限配置。
