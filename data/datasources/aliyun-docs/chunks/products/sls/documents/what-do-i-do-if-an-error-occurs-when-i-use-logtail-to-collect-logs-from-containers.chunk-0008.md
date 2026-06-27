### 误删由CRD创建的LogStore后，如何处理
如果您删除了由CRD自动创建出的LogStore，则已采集的数据无法恢复，并且针对此LogStore的CRD配置会失效，您可以选择以下方案避免日志采集异常。
在CRD配置中使用其他LogStore，避免使用手动误删的LogStore。
重启alibaba-log-controllerPod。
您可通过如下命令查找该Pod。
kubectl get po -n kube-system | grep alibaba-log-controller
该文章对您有帮助吗？
反馈
