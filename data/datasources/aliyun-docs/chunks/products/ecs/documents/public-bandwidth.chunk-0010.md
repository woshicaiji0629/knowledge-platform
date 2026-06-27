## 常见问题
如果使用IPv6、EIP、NAT网关方式访问公网，怎么查看计费规则？
使用IPv6地址：请参见[IPv6](https://help.aliyun.com/zh/ipv6-gateway/product-overview/ipv6-gateway-billing/)[计费说明](https://help.aliyun.com/zh/ipv6-gateway/product-overview/ipv6-gateway-billing/)。
绑定了弹性公网IP（EIP）：请参见[EIP](../../eip/documents/billing-overview.md)[计费概述](../../eip/documents/billing-overview.md)。
使用NAT网关：请参见[NAT](../../nat-gateway/documents/nat-gateway-billing.md)[网关计费说明](../../nat-gateway/documents/nat-gateway-billing.md)。
开通公网后，哪些常见场景消耗的流量是不计费的？
ECS通过内网地址访问同VPC的RDS/SLB/OSS产品或传输数据、通过公网上传文件到ECS服务器等。
重要
通过公网地址从阿里云相关产品下载文件到ECS，可能会在相关产品侧产生流量费用，请仔细阅读相关计费说明。
包年包月实例开通固定公网IP为什么会有额外费用？
当包年包月实例开通按流量计费的固定公网IP时，可能会在ECS实例使用过程中根据实际使用的出网流量产生后付费费用。具体计费情况如下：
包年包月实例：购买实例时无需对固定公网IP配置额外预付费，但使用过程中会在实际产生出网流量的计费周期内，产生相关费用。
按量付费、抢占式实例：与实例其他配置费用一起按计费周期产生账单，在实际产生出网流量的计费周期内，产生相关费用。
该文章对您有帮助吗？
反馈
