m/eip)[管理控制台](https://vpc.console.aliyun.com/eip)查看已购EIP的相关参数信息。
新购的EIP为按量付费（按使用流量计费）的BGP多线默认安全防护EIP。
分配Anycast EIP
关于ALB绑定Anycast EIP的相关限制和详细操作，请参见[ALB](../use-cases/associate-an-anycast-eip-with-an-alb-instance.md)[绑定](../use-cases/associate-an-anycast-eip-with-an-alb-instance.md)[Anycast EIP](../use-cases/associate-an-anycast-eip-with-an-alb-instance.md)[实现多地域业务就近接入](../use-cases/associate-an-anycast-eip-with-an-alb-instance.md)。
选择IP类型为Anycast弹性公网IP。
在列表中的分配Anycast弹性公网IP下拉框中选择新购Anycast弹性公网IP或指定可用的Anycast EIP，然后单击确定变更。
说明
列表中的所有可用区都需要分配Anycast EIP。
选择新购Anycast弹性公网IP时，请注意：
ALB实例变更私网或释放后，关联的Anycast EIP会自动解绑并释放。
您可以通过[任播弹性公网](https://vpc.console.aliyun.com/eip/anycasts)[IP](https://vpc.console.aliyun.com/eip/anycasts)[管理控制台](https://vpc.console.aliyun.com/eip/anycasts)查看已购Anycast EIP的相关参数信息。
在实例详情页签，查看网络类型。
此变更生效大约需要一分钟，在实例详情页签查看IPv4的网络类型转变为公网后，代表转换成功。
