-an-eip.md)[IP](convert-the-public-ip-address-of-an-instance-in-a-vpc-to-an-eip.md)[转为弹性公网](convert-the-public-ip-address-of-an-instance-in-a-vpc-to-an-eip.md)[IP](convert-the-public-ip-address-of-an-instance-in-a-vpc-to-an-eip.md)和[ConvertNatPublicIpToEip](../api-convertnatpubliciptoeip.md)。
重要
固定公网IP转成弹性公网IP后，使用弹性公网IP访问公网会收取公网出网带宽费用、EIP配置费（满足特定条件时不收取）和EIP绑定费（满足特定条件时不收取）。具体收费细则，请参见[弹性公网](../../../eip/documents/billing-overview.md)[IP](../../../eip/documents/billing-overview.md)[计费概述](../../../eip/documents/billing-overview.md)。
- 调用StopInstance并指定StoppedMode=StopCharging后，实例没有进入节省停机模式？
对于不满足节省停机模式条件的实例，调用[StopInstance](../api-stopinstance.md)接口并设置StoppedMode=StopCharging时，系统不会拦截该操作，系统将优先确保实例正常停机。要确认实例是否成功进入节省停机模式，请通过[DescribeInstances](../developer-reference/api-ecs-2014-05-26-describeinstances.md)接口查询实例状态。
- 如何将普通停机模式切换到节省停机模式？
无法直接切换，需先启动实例至运行中状态，再启用节省停机模式。
该文章对您有帮助吗？
反馈
