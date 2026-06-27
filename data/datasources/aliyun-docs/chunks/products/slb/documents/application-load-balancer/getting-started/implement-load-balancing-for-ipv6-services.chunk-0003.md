## 前提条件
您已在华东2（上海）地域创建了一个VPC1，并分别在可用区E和可用区G创建了一个交换机VSW1和VSW2，且VPC1已[开通](https://help.aliyun.com/zh/ipv6-gateway/user-guide/enable-ipv6-for-a-vpc#section-p31-wbx-mlj)[IPv6](https://help.aliyun.com/zh/ipv6-gateway/user-guide/enable-ipv6-for-a-vpc#section-p31-wbx-mlj)[网段](https://help.aliyun.com/zh/ipv6-gateway/user-guide/enable-ipv6-for-a-vpc#section-p31-wbx-mlj)、VSW1和VSW2均已[开通](https://help.aliyun.com/zh/ipv6-gateway/user-guide/enable-ipv6-for-a-vswitch-1#section-qn2-ft9-1g2)[IPv6](https://help.aliyun.com/zh/ipv6-gateway/user-guide/enable-ipv6-for-a-vswitch-1#section-qn2-ft9-1g2)。VPC开通IPv6网段后，系统会为您默认创建一个IPv6网关。
如果计划将ALB部署在交换机VSW1和VSW2，需注意：[ALB](../../product-overview/alb.md)[升级实例](../../product-overview/alb.md)会从每个指定的交换机中分配3个IP地址，包含1个VIP（对外提供服务）和2个Local IP（用于与后端服务器通信），如果IP不足会出现报错并且无法创建实例，请确保交换机VSW1和VSW2中已预留足够的可用IP；升级前的ALB实例不受该限制。
说明
为确保ALB升级实例各项弹性能力可用，建议您在ALB实例所在的每个交换机内预留至少8个IP地址。
为确保ALB升级实例与后端服务正常连通，如您的后端服务中存在访问策略（包括iptables或其他任何第三方安全策略软件），建议您提前放通ALB实例所属交换机网段。
您已经[注册域名](https://help.aliyun.com/zh/dws/user-guide/how-to-register-a-domain-name)并完成[备案](https://help.aliyun.com/zh/icp-filing/basic-icp-service/user-guide/icp-filing-application-overview)。
