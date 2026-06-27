## 常见问题及解决方案
常见问题：安装ack-kserve组件时出现报错failed to call webhook: Post "https://cert-manager-webhook.cert-manager.svc:443/validate?timeout=30s": tls: failed to verify certificate: x509: certificate signed by unknown authority。
问题原因：ack-kserve组件强依赖于cert-manager组件，如果当前集群中未安装cert-manager组件或者cert-manager组件未就绪，此时安装ack-kserve组件就会出现上述报错。
解决方案：
执行以下命令，确认集群中是否已经安装cert-manager组件。
kubectl get crd |grep certificates.cert-manager.io
预期输出如下所示，表明集群中已经安装cert-manager组件。
certificates.cert-manager.io 2024-05-06T07:09:17Z
如集群中没有cert-manager的CRD资源，请参见[步骤一](../../cloud-native-ai-suite/user-guide/installing-ack-kserve-components.md)安装cert-manager组件。
执行以下命令，确认cert-manager组件是否已经就绪。
kubectl -n cert-manager get po
预期输出如下所示，表明cert-manager组件的Pod均已就绪。
NAME READY STATUS RESTARTS AGE cert-manager-7f4bb44d5b-jrrfn 1/1 Running 0 23h cert-manager-cainjector-79544456cc-qp5pp 1/1 Running 0 23h cert-manager-webhook-f74ccb647-7m5dt 1/1 Running 0 23h
如果所有Pod均为Ready状态，请参见上文先卸载ack-kserve组件，然后再重新安装即可解决报错。
该文章对您有帮助吗？
反馈
