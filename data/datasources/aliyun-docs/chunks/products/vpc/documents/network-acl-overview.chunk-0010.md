1、配置[DHCP](dhcp-option-set-and-dns-hostname.md)[选项集](dhcp-option-set-and-dns-hostname.md)后，您需要添加放行指定DNS服务器的出入方向规则。未添加规则，可能会造成域名解析异常。2、使用负载均衡时，您需要在出入方向规则中添加允许监听端口接收到的请求转发至后端服务器、健康检查端口的请求发送至后端服务器的规则。
