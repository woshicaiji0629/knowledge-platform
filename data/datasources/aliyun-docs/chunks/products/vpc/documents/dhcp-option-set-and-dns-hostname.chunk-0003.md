### 配置DNS服务器IP：查询域名解析记录
DNS 服务器维护域名解析记录。当 ECS 执行ping host01.host.prvz时，会向指定的 DNS 服务器发送查询请求，DNS 服务器将返回对应的 IP 地址。
使用官方镜像创建 ECS 时，阿里云会通过[DHCP](https://www.rfc-editor.org/rfc/rfc2131)自动为 ECS 配置默认 DNS 服务器，其 IP 为 100.100.2.136 和 100.100.2.138。

| 对比项 | 启用 DNS 主机名 | 内网 DNS 解析（Private DNS） | 自建 DNS 服务 |
| --- | --- | --- | --- |
| DHCP 选项集类型 | 默认 DHCP 选项集 | 自定义 DHCP 选项集 | 自定义 DHCP 选项集 |
| 域名配置 | ECS 私网域名 [regionID].ecs.internal 默认 DNS 服务器 | 自定义域名 默认 DNS 服务器 | 自定义域名 自建 DNS 服务器 |
| 计费 | 无需支付域名费用 | 结合添加的域名数量、解析请求量 [收取费用](https://help.aliyun.com/zh/dns/product-billing) | 无需支付域名费用 |
| 是否支持跨 VPC、混合云私网域名通信 | 不支持 | 支持 | 支持 |

DNS 查询性能取决于使用的DNS服务器。阿里云默认DNS服务器的查询性能，可参考[内网](https://help.aliyun.com/zh/dns/limits-pvtz#td-sss-vz2-tsl)[DNS](https://help.aliyun.com/zh/dns/limits-pvtz#td-sss-vz2-tsl)[解析服务的使用限制](https://help.aliyun.com/zh/dns/limits-pvtz#td-sss-vz2-tsl)。
