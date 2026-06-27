# 查看集群内所有isvc资源。 kubectl get isvc --all-namespaces # 保存集群内所有isvc资源。 kubectl get isvc --all-namespaces -oyaml > isvc.yaml.bak # 确认业务不再使用后删除isvc资源。 kubectl delete isvc --all
删除集群内的KServe CRD资源。
在删除CRD之前，应确保先删除所有依赖于该CRD的CR，否则会导致CRD删除失败。
kubectl delete crd clusterservingruntimes.serving.kserve.io kubectl delete crd clusterstoragecontainers.serving.kserve.io kubectl delete crd inferencegraphs.serving.kserve.io kubectl delete crd inferenceservices.serving.kserve.io kubectl delete crd predictors.serving.kserve.io kubectl delete crd servingruntimes.serving.kserve.io kubectl delete crd trainedmodels.serving.kserve.io
卸载ack-kserve组件。
登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。
在集群列表页面，单击目标集群名称，然后在左侧导航栏，选择应用>Helm。
在Helm页面，单击ack-kserve组件操作列的删除，即可根据页面提示卸载ack-kserve组件。
卸载cert-manager组件。
警告
卸载cert-manager组件前，请先确认集群中没有其他组件使用cert-manager组件，否则会导致业务不可用。
登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。
在集群列表页面，单击目标集群名称，然后在左侧导航栏，选择应用>Helm。
在Helm页面，单击cert-manager组件操作列的删除，即可根据页面提示卸载cert-manager组件。
执行以下命令，删除集群内cert-manager的CRD资源。
kubectl delete crd certificaterequests.cert-manager.io kubectl delete crd certificates.cert-manager.io kubectl delete crd challenges.acme.cert-manager.io
