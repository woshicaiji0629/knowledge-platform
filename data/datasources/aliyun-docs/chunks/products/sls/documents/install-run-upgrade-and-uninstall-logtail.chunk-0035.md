### 升级与回滚Logtail
在升级前，您需要对Logtail组件相关描述文件进行备份。
重要
在升级前如果已存在明显的采集延迟，执行 Logtail 升级操作可能会导致少量日志丢失。
kubectl get ds -n kube-system logtail-ds -o yaml > logtail-ds.yaml kubectl get deployment -n kube-system alibaba-log-controller -o yaml > alibaba-log-controller.yaml kubectl get crd aliyunlogconfigs.log.alibabacloud.com -o yaml > aliyunlogconfigs-crd.yaml kubectl get cm -n kube-system alibaba-log-configuration -o yaml > alibaba-log-configuration.yaml kubectl get aliyunlogconfigs --all-namespaces -o yaml > aliyunlogconfigs-cr.yaml
请根据集群情况选择组件升级方式，当您使用的是ACK集群且集群与日志服务属于同一个阿里云账号时，参考ACK集群升级方式。若使用自建集群或ACK集群与日志服务属于不同的阿里云账号，请参考自建集群升级方式。
