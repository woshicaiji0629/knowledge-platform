### CDN是否支持对指定IP限速？
不支持。CDN用量封顶是针对整个域名的总用量进行限制，无法将流量或带宽限制细化到单个 IP 上。如需基于客户端 IP 进行限速，建议使用[边缘安全加速的 WAF 频次控制](https://help.aliyun.com/zh/edge-security-acceleration/esa/user-guide/waf-overview/)。
