| 接入失败信息 | 失败原因 | 处理建议 |
| --- | --- | --- |
| The os XXX unsupport | 当前边缘节点的系统版本不支持。 | 关于支持的边缘节点的系统列表，请参见 [添加边缘节点](add-an-edge-node.md) 。 |
| invalid nodeName | 节点名称不合法。 | 节点名称只能由英文小写字母、中划线（-）和半角句号（.）组成。 节点名称不能超过 253 个字符。 节点名称不能以 localhost 开头。 |
| Node route overlaps with service cidr | 节点的路由表网段与集群创建时配置的 Pod CIDR 或 Service CIDR 冲突。 | 重新创建集群，请注意配置 Pod CIDR 与 Service CIDR，需避免与边缘节点的 NameServer 地址以及路由表网段冲突。 |
| response error msg: TOKEN_EXPIRED | 接入 Token 过期。 | 重新生成节点接入脚本。 检查节点系统时间是否正常。 |
| A node named XXX is already exist in the cluster | 集群中已存在同名的节点。 | 下线集群中的同名节点。 |
| error run phase join-node: failed to get cluster info: failed to get cluster-info configmap, Get "https://xx.xxx.xx.xx:6443/api/v1/namespaces/kube-public/configmaps/cluster-info": dial tcp xx.xxx.xx.xx:6443: i/o timeout | 获取集群 cluster-info 失败。 | edgeadm 接入边缘节点时需要通过该地址访问 APIServer， 请检查 API Server 负载均衡（SLB）ACL 规则是否限制了该地址的访问。 |
| error run phase join-node: Install edge-hub failed: Copy file /tmp/edge-hub to /usr/bin/edge-hub fail: open /usr/bin/edge-hub: text file busy | 40009 | 40009 | 安装 edge-hub 失败，节点上已经存在 edge-hub 的二进制文件。 | 执行 edgeadm reset 命令清理节点后重新接入。 |
| error run phase post-check: timed out waiting for the condit
