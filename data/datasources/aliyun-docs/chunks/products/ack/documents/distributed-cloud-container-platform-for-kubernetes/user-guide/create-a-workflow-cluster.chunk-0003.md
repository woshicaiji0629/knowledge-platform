| 参数 | 描述 |
| --- | --- |
| 集群名称 | 填写集群的名称。 说明 长度为 1~63 个字符，可包含字母、数字、下划线（_）或中划线（-），且仅允许以字母开头。 |
| 地域 | 选择集群所在的地域。 |
| 专有网络 | 设置集群的专有网络 VPC，在下拉列表中选择已创建的 VPC。 |
| 虚拟交换机 | 在下拉列表中选择已创建的交换机。 |
| APIServer 负载均衡（SLB） | 无需设置，创建 工作流集群 时会默认为 API Server 创建一个规格为 标准型 I（slb.s2.small） 的 SLB 实例，若删除该实例会导致 API Server 无法访问。 如 SLB 实例规格不满足要求，您可以前往 SLB 控制台修改，具体操作，请参见 [SLB](../../../../slb/documents/classic-load-balancer/product-overview/change-the-configurations-of-subscription-instances.md) [实例升配](../../../../slb/documents/classic-load-balancer/product-overview/change-the-configurations-of-subscription-instances.md) 。 SLB 实例计费信息，请参见 [SLB](../../../../slb/documents/classic-load-balancer/product-overview/billing-overview.md) [计费说明](../../../../slb/documents/classic-load-balancer/product-overview/billing-overview.md) 。 |
| 创建并绑定 EIP | 选择是否为集群绑定 EIP。 开启后，系统将为内网 SLB 实例创建并绑定一个 EIP（弹性公网 IP），获得从公网访问集群 API Server 的能力。EIP 绑定后不支持解绑，因为可能有子集群已经使用舰队的公网访问链接。 若选择不开启，则无法通过外网访问集群 API Server。 EIP 计费信息，请参见 [弹性公网](../../../../eip/documents/billing-overview.md) [IP](../../../../eip/documents/billing-overview.md) [计费说明](../../../../eip/documents/billing-overview.md) 。 |
| 开启组件及审计日志 | 选择是否开启日志服务功能。 开启后，系统将自动创建一个名称为 k8s-log-{C
