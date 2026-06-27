### API
调用[CreateIpv4Gateway](developer-reference/api-vpc-2016-04-28-createipv4gateway.md)创建IPv4网关。
调用[EnableVpcIpv4Gateway](developer-reference/api-vpc-2016-04-28-enablevpcipv4gateway.md)激活IPv4网关，指定RouteTableList为公有交换机绑定的路由表；如未指定，需要调用[CreateRouteEntry](developer-reference/api-vpc-2016-04-28-createrouteentry.md)在对应路由表中自行添加0.0.0.0/0路由指向IPv4网关。
