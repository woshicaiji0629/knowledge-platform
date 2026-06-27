### 采集规则配置
日志服务提供了如下两种方式来定义采集配置规则：

| 配置方式 | 特点 | 适用场景 | 注意事项 |
| --- | --- | --- | --- |
| [Kubernetes-CRD](collect-text-logs-of-self-built-k8s-clusters-deploy-logtail-in-daemonset-mode-2.md) | 云原生友好： 通过 CRD 声明配置，与 Kubernetes API 无缝集成。 配置即代码 ：支持 GitOps 流程，版本可控。 动态生效 ：Operator 自动监听变更，实时同步到 LoongCollector。 | 生产集群优先选择 CRD 模式，支持 CI/CD 自动化的场景。 | 对于单个采集配置，只能选择一种方式进行配置与修改，否则会发生配置失效的情况。 若多个采集配置同时覆盖同一个文件，可以开启 [允许文件多次采集](container-log-collection-in-a-kubernetes-cluster.md) 开关，否则多个配置的生效情况是随机的。但更建议使用 [数据加工](data-processing-new-version-quick-start.md) 的方式来实现保存多份日志。 |
| [日志服务控制台](container-log-collection-in-a-kubernetes-cluster.md) | 操作简单 ：图形化界面配置，零编码。 快速验证 ：适合快速测试。 集中管理 ：所有配置在 SLS 控制台统一查看。 | 大规模集群需逐个关联配置，因此适合小型集群、临时调试、非生产环境使用。 |  |
