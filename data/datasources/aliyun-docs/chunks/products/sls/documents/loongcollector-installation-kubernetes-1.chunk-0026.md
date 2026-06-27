## 附录：YAML示例
本示例展示了一个完整的 Kubernetes Deployment 配置，包含业务容器（Nginx）和 LoongCollector Sidecar 容器，适用于通过 Sidecar 模式采集容器日志。
使用前请完成以下三项关键替换：
将${your_aliyun_user_id}替换为您的阿里云主账号 UID；
将${your_machine_group_user_defined_id}替换为[步骤三中创建的机器组自定义标识](collect-k8s-cluster-logs-through-sidecar.md)，必须完全一致。
将${your_region_config}替换为与日志服务 Project 所在地域及网络类型匹配的配置名。
示例：Project 位于 华东1（杭州），内网访问——>cn-hangzhou；公网访问——>cn-hangzhou-internet。
