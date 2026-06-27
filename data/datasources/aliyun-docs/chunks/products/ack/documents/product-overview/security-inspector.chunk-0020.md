### 2022年06月

| 版本号 | 镜像地址 | 变更时间 | 变更内容 | 变更影响 |
| --- | --- | --- | --- | --- |
| v0.8.2.16-gc84d60d-aliyun | registry.cn-hangzhou.aliyuncs.com/acs/security-inspector:v0.8.2.16-gc84d60d-aliyun | 2022 年 06 月 21 日 | 修复在 Kubernetes 1.22 集群中可能会出现 MountVolume.SetUp failed for volume "config" : object "kube-system"/"security-inspector-polaris-config" not registered 事件的问题。 优化组件对 API Server 的请求，进一步减轻大规模集群下 API Server 的压力。 | 此次升级不会对业务造成影响。 |
