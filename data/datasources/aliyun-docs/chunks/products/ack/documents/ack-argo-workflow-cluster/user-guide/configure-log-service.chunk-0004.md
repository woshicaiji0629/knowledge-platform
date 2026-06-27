## 开启日志服务
工作流集群创建后，系统会自动创建一个名为k8s-log-<clusterid>的Project，用来收集工作流集群日志。如果日志服务Project不存在，请自行创建名为k8s-log-<clusterid>的Project。关于创建Project的具体操作，请参见[创建](../../../../sls/documents/manage-a-project.md)[Project](../../../../sls/documents/manage-a-project.md)。
您可以通过阿里云 Argo CLI或者通过直接创建日志服务CR两种方式开启日志服务。
