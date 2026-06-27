## 通过阿里云CLI删除集群
使用以下命令关闭Argo Server同时删除相关SLB和ECI等资源。
aliyun adcp UpdateHubClusterFeature --ArgoServerEnabled false --ClusterId <cluster id>
使用以下命令删除工作流集群。
aliyun adcp DeleteHubCluster --ClusterId <cluster id>
