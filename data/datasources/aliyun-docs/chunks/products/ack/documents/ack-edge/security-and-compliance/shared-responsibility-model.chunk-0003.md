## 理解责任共担模型
在您设计和部署企业应用系统之前，请您充分理解企业自身和阿里云的安全责任边界。
ACK托管架构下集群安全的责任共担模型如下图所示。
当您选择使用ACK Serverless集群或在ACK托管集群中部署虚拟节点组件（ack-virtual-node）时，除了集群控制面和基础设施安全外，阿里云还将负责Pod底层[弹性容器实例（ECI）运行时](https://help.aliyun.com/zh/eci/product-overview/what-is-elastic-container-instance)的安全，由客户负责重建应用Pod以使修复生效。下图为Serverless架构下使用ACK Serverless集群或在ACK托管集群中部署虚拟节点组件（ack-virtual-node）时的安全责任共担模型。
对于使用[托管节点池](../../overview-of-managed-node-pools.md)的ACK集群，阿里云会负责根据客户对于托管节点池的配置尝试自动化的修复节点OS漏洞和Kubelet版本升级，其中，节点OS漏洞的修复补丁由[云安全中心](https://help.aliyun.com/zh/security-center/user-guide/purchase-security-center#task-lxj-3bc-zdb)提供。如果集群节点使用的是自定义OS镜像，仍需要由客户负责节点漏洞的修复更新。下图为托管架构下ACK集群使用托管节点池时的安全责任共担模型。
针对容器服务ACK Edge集群，阿里云负责集群控制面，对数据面[边缘节点池](../user-guide/overview-of-cell-based-management-at-the-edge.md)提供K8s相关公告并发布对应的漏洞补丁或版本更新能力，客户需要基于阿里云公告以及提供的补丁或版本升级方式及时进行集群侧系统组件、运行时等漏洞的修复和版本更新。此外，客户需要负责边缘节点自身的稳定性、OS层面安全漏洞的修复和版本更新。
该文章对您有帮助吗？
反馈
