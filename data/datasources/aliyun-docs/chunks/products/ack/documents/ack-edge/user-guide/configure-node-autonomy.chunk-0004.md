### 通过kubectl开启
给边缘节点添加如下注解，开启节点自治，该操作仅对边缘节点生效。
kubectl annotate node xxx node.beta.openyurt.io/autonomy=true --overwrite
此外，您还可以通过如下方式为边缘节点配置自治时间。
说明
仅支持1.28及以上的ACK Edge集群配置边缘节点自治时间，配置后，如果边缘节点与云端管控之间持续断网时间在自治时间内，则节点上的Pod持续运行，业务不受影响，不会触发驱逐行为，如果超过了配置的自治时间，则会驱逐边缘节点上的Pod。
kubectl annotate node xxx node.alibabacloud.com/autonomy-duration=500s --overwrite
