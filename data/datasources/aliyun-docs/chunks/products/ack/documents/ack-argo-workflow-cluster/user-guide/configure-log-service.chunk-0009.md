### 通过访问Argo Server访问SLS
如需通过Argo CLI访问已删除Pod的日志，则需要先开启Argo Server并配置相关参数。
说明
通过日志服务获取工作流日志，必须指定<pod-name>。
若需要访问其他Namespace的Workflow/Pod，则获取KUBE_TOKEN时，需要使用对应Namespace。
执行以下命令，开启Argo Server并配置参数。
export ARGO_SERVER=argo.<cluster id>.<region>.alicontainer.com:2746 export KUBE_TOKEN=$(k create token default -n default --duration 24h) export ARGO_TOKEN="Bearer $KUBE_TOKEN" export ARGO_INSECURE_SKIP_VERIFY=true
执行以下命令，获取工作流Pod的日志。
argo logs <workflow-name> <pod-name>
