### 隧道模式
仅支持节点间网络互通的节点池。
边缘侧被选举的网关节点会主动与云上网关节点构建IPSec加密的VPN隧道。
Raven Agent在本网络域内构建 VXLAN网络，将跨域容器网络请求转发到网关节点。
本网络域内的容器间通信通过Flannel VXLAN进行通信。
跨网络域的请求将被拦截，并通过Raven VXLAN传送到网关节点，通过VPN隧道实现通信。
重要
由于跨域通信通过公网传输，可能存在数据丢失风险，请勿传输重要业务数据。如在使用过程中遇到问题或有相关产品建议，请[提交工单](https://selfservice.console.aliyun.com/ticket/createIndex)联系容器服务团队。
