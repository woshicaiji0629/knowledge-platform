gnext/project/k8s-log-{clusterid}/logsearch/workflow-logstore?slsRegion={region}&queryTimeType=3&queryString=_pod_name_=NAMEand _namespace_=NAMESPACE
在工作流集群中重启Argo Server，使配置生效。
kubectl rollout restart deployment/argo-server -n {clusterid}
登录Argo UI查看，UI中已添加日志服务链接。
该文章对您有帮助吗？
反馈
