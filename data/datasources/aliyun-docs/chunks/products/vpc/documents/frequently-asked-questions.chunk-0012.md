## 网络规划设计问题
VPC支持组播吗？
VPC本身不支持组播能力。但VPC可以结合云企业网CEN产品，实现[组播管理](../../cen/documents/user-guide/multicast-overview.md)。
VPC如何实现公网私用？
部分企业在本地IDC或VPC使用了非[RFC 1918](https://www.rfc-editor.org/rfc/rfc1918)规定的私有网段，例如30.0.0.0/16。当与其他VPC或本地IDC建立网络连接时，由于VPC默认将[RFC 1918](https://www.rfc-editor.org/rfc/rfc1918)之外的IP地址视为公网网段，VPC中云产品资源具备公网访问能力后，即便配置了指向30.0.0.0/16的路由条目指向本地IDC或VPC，依旧优先访问公网，无法访问目标VPC或本地IDC。
您可通过如下方式，实现公网网段私用：
方式1：IPv4网关功能。
您可通过使用IPv4网关，集中控制VPC公网访问行为，访问30.0.0.0/16时将优先路由到其他VPC或本地IDC。详细方案您可参考[使用](using-ipv4-gateway-for-public-network-private-use.md)[IPv4](using-ipv4-gateway-for-public-network-private-use.md)[网关实现公网私用](using-ipv4-gateway-for-public-network-private-use.md)。
方式2：用户网段功能。
如果希望VPC在转发访问30.0.0.0/16的请求时，按照路由表进行转发而不是直接转发到公网，您可以在新建VPC时使用[CreateVpc](developer-reference/api-vpc-2016-04-28-createvpc.md)接口传入UserCidr参数，为VPC设置用户网段。设置用户网段后，该VPC访问用户网段地址的请求将按照路由表进行转发。
1、用户网段仅支持通过API设置，不支持控制台。用户网段创建后不支持修改。2、当您仅设置VPC的IPv4网段时，如果选择除192.168.0.0/16、172.16.0.0/12、10.0.0.0/8三个RFC标准私网网段及其子网之外的自定义地址网段，系统会默认设置该主网段为用户网段。
VPC与经典网络的区别是什么？
经典网络是阿里云早期的网络形态，默认与VPC不互通。目前已逐步下线，不推荐用户使用。用户所有购买的资源都应部署在VPC中。
