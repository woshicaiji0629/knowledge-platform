### 使用自建 DNS 服务
如果业务需要灵活的DNS调度策略，例如根据地理位置、网络质量、服务器负载等因素动态返回最优IP，您可以自建DNS服务器，但需自行维护域名解析记录，并确保服务可靠性。您可以参考以下示例部署自建DNS服务，并使用DHCP选项集为ECS实例指定自建DNS服务器IP和自定义域名。
使用BIND部署自建 DNS 服务示例
执行yum install -y bind bind-utils安装 BIND。
执行vim /etc/named.conf修改主配置文件的配置项。
listen-on port 53 { any; }; # 监听所有网络接口的53端口 allow-query { any; }; # 允许任何IP进行DNS查询
执行vim /etc/named.rfc1912.zones配置区域文件。
// 自定义域名 zone "example.com" IN { type master; file "example.com.zone"; }; zone "0.168.192.in-addr.arpa" IN { type master; file "0.168.192.zone"; };
执行cp -p /var/named/named.localhost /var/named/example.com.zone与vim /var/named/example.com.zone配置正向解析文件。
$TTL 1D @ IN SOA example.com. admin.example.com. ( 1 ; serial 1D ; refresh 1H ; retry 1W ; expire 3H ) ; minimum NS dns.example.com. Web01 A 192.168.0.2; Web02 A 192.168.0.3;
执行cp -p /var/named/named.empty /var/named/0.168.192.zone与vim /var/named/0.168.192.zone配置反向解析文件。
$TTL 3H @ IN SOA 0.168.192.in-addr.arpa. admin.zjq.com. ( 1 ; serial 1D ; refresh 1H ; retry 1W ; expire 3H ) ; minimum NS dns.example.com. 2 PTR Web01.example.com. 3 PTR Web02.example.com.
执行systemctl restart named重启 BIND 服务。
如果您在使用自建 DNS 服务的同时希望使用阿里云 DNS 服务，需要为自建 DNS 服务器配置转发规则，将自定义域名以外的查询请求转发至阿里云默认DNS服务器。
