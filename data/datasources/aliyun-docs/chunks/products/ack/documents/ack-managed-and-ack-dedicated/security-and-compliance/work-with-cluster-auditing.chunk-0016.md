## 参考信息：ACK专有集群API Server审计配置介绍
创建ACK专有集群集群配置集群组件时，控制台会默认选中使用日志服务，开启API Server审计功能，按审计策略采集事件数据，并将事件数据写入到后端。
说明
以下功能涉及kube-apiserver启动参数的更改，仅面向ACK专有集群。ACK托管集群和ACK Serverless集群集群控制面由ACK托管，不支持手动修改。
