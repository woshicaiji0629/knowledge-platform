## 前提条件
已创建ACK Edge集群，且集群版本为v1.26.3及以上。具体操作，请参见[创建集群](create-an-ack-edge-cluster-1.md)。
如开启代理模式，边缘侧安全策略请勿阻挡TCP[10280,10285)区间的端口。
如开启隧道模式，边缘侧安全策略请勿阻挡UDP 4500，云端安全组放开UDP 8472端口。
由于边缘侧需要与云上构建反向通道，因此边缘侧安全策略请勿阻挡Raven组件挂载的EIP地址。
如何查看Raven挂载的EIP地址，请参见[云资源信息](using-the-cloud-side-communication-raven-component.md)。
