## 实例网络类型
ALB网络类型分为公网和私网。公网和私网的区别：
私网：ALB只有私网IP地址，只能被ALB所在VPC内的资源访问，无法从互联网访问。
公网：ALB具有公网IP和私网IP地址。公网ALB默认通过弹性公网IP（Elastic IP Address，简称EIP）提供公网能力，选择公网将会收取弹性公网IP的实例费、流量费用。
如需通过任播弹性公网IP（ Anycast Elastic IP Address，简称Anycast EIP）提供公网能力，您需要为ALB实例绑定Anycast EIP，具体操作，请参见[ALB](../use-cases/associate-an-anycast-eip-with-an-alb-instance.md)[绑定](../use-cases/associate-an-anycast-eip-with-an-alb-instance.md)[Anycast EIP](../use-cases/associate-an-anycast-eip-with-an-alb-instance.md)[实现多地域业务就近接入](../use-cases/associate-an-anycast-eip-with-an-alb-instance.md)。
