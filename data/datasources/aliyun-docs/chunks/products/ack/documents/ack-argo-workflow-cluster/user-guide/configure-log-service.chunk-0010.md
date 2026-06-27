## 访问持久化到数据库的工作流日志
您可以配置[持久化工作流](../../distributed-cloud-container-platform-for-kubernetes/user-guide/persistence-workflow.md)，将工作流持久化保存到数据库中，即使工作流在集群中被删除，也可以通过Agro CLI方式下载工作流日志。
执行以下命令，配置访问权限。
argo config init #按照提示配置相关信息,包括ak、sk等。
执行以下命令查询工作流的UID。
