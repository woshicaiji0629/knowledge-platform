### CDN是否支持设置单个IP的流量限制或针对指定IP限速？
不支持。CDN用量封顶是针对整个域名的总用量（带宽、流量、HTTPS请求数）进行限制，无法细化到单个IP。如果您需要基于客户端IP进行频次控制或拦截，建议使用[边缘安全加速的 WAF 频次控制](https://help.aliyun.com/zh/edge-security-acceleration/esa/user-guide/waf-overview/)，当客户端IP超过设定的频次阈值时会被 403 拦截。
