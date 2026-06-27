### 私网变更公网
实例由私网变更为公网时，您需要为ALB实例分配公网IP，支持为ALB实例分配EIP或Anycast EIP，该操作将产生相关公网网络费，更多信息，请参见[弹性公网](../../../../eip/documents/pay-as-you-go.md)[IP](../../../../eip/documents/pay-as-you-go.md)[计费](../../../../eip/documents/pay-as-you-go.md)和[Anycast EIP](https://help.aliyun.com/zh/anycast-eip/product-overview/product-billing)[计费](https://help.aliyun.com/zh/anycast-eip/product-overview/product-billing)。
- 登录[应用型负载均衡](https://slb.console.aliyun.com/alb)[ALB](https://slb.console.aliyun.com/alb)[控制台](https://slb.console.aliyun.com/alb)。
在顶部菜单栏，选择实例所属的地域。
在实例页面，找到目标私网ALB实例，然后单击实例ID。
在实例详情页签，找到基本信息区域，在网络类型的IPv4右侧单击变更网络类型。
在变更网络类型对话框中，根据您的业务需求选择IP类型并分配公网IP，然后单击确定变更。
分配EIP
选择IP类型为弹性公网IP。
在列表中的分配弹性公网IP下拉框中选择新购弹性公网IP或指定可用的弹性公网IP。
说明
列表中的所有可用区都需要分配弹性公网IP。
如果您的业务需要ALB使用某个特定IP地址的EIP，您可以通过变更单个EIP实现。变更单个EIP需要增加或减少可用区来实现绑定或解绑EIP。关于如何变更可用区，请参见[更新实例可用区](modify-the-configurations-of-alb-instances.md)。
选择新购弹性公网IP时，请注意：
ALB网络类型变更会影响业务，之前随公网ALB创建的EIP会因网络类型的变更自动解绑或释放掉且无法找回。
您可以通过[弹性公网](https://vpc.console.aliyun.com/eip)[IP](https://vpc.console.aliyun.com/eip)[管理控制台](https://vpc.console.aliyun.com/eip)查看已购EIP的相关参数信息。
新购的EIP为按量付费（按使用流量计费）的BGP多线默认安全防护EIP。
分配Anycast EIP
关于ALB绑定Anycast EIP的相关限制和详细操作，请参见[ALB](../use
