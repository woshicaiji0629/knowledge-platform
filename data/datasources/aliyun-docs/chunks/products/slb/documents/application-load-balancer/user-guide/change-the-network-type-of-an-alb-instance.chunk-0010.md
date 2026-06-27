### 私网变更公网
IPv4私网变更公网，请参见[IPv4](change-the-network-type-of-an-alb-instance.md)[实例网络类型变更](change-the-network-type-of-an-alb-instance.md)。
IPv6私网变更公网，请执行以下步骤完成变更。
说明
IPv6私网变更公网，将在VPC中的IPv6网关中开启公网带宽。开启公网带宽会产生一定的费用且会根据ALB公网和私网的切换，自动加入或删除。更多信息，请参见[IPv6](https://help.aliyun.com/zh/ipv6-gateway/product-overview/ipv6-gateway-billing/#concept-gvc-fyt-zfb)[网关计费说明](https://help.aliyun.com/zh/ipv6-gateway/product-overview/ipv6-gateway-billing/#concept-gvc-fyt-zfb)。
- 登录[应用型负载均衡](https://slb.console.aliyun.com/alb)[ALB](https://slb.console.aliyun.com/alb)[控制台](https://slb.console.aliyun.com/alb)。
在顶部菜单栏，选择实例所属的地域。
在实例页面，找到目标私网ALB实例，然后单击实例ID。
在实例详情页签，找到基本信息区域，在网络类型的IPv6右侧单击变更网络类型。
在弹出的IPv6变更网络类型对话框中，确认提示信息，然后单击确定变更。
说明
如果ALB实例所在的VPC下没有IPv6网关，系统将提示您新建IPv6网关。请根据控制台提示信息完成操作。
在实例详情页签，查看网络类型。
此变更生效大约需要一分钟，在实例详情页签查看IPv6的网络类型转变为公网后，代表转换成功。
