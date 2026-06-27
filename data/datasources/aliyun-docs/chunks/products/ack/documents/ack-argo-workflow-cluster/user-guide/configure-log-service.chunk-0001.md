## 使用说明
日志收集后，如果工作流还在集群中，无论Pod是否被删除，您都可以通过[Argo CLI](configure-log-service.md)和[Argo UI](configure-log-service.md)查看工作流相关的Pod日志。
如果工作流在集群中被删除，但是已经 持久化 到数据库中，您可以通过Argo CLI[下载工作流日志的](configure-log-service.md)[ZIP](configure-log-service.md)[包](configure-log-service.md)或者直接访问[日志服务控制台](https://sls.console.aliyun.com/)查看日志。
关于如何将工作流持久化到数据库中，请参见[持久化工作流](../../distributed-cloud-container-platform-for-kubernetes/user-guide/persistence-workflow.md)。
