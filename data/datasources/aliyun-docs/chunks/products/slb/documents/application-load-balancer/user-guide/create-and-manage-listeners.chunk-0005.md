;..：从右往左取第一个不在列表中的值。
开启后，转发规则中基于SourceIp匹配和QPS(基于客户端源IP限速)将使用真实客户端IP。
QUIC监听不支持此配置项。仅标准版、WAF增强版实例支持，基础版不支持。
附加HTTP头字段：选择要添加的HTTP头字段，用于获取客户端IP、监听协议、端口等信息。各头字段的详细说明，请参见[HTTP](http-headers.md)[头字段](http-headers.md)。
开启QUIC升级：适用于HTTPS监听与QUIC监听联合使用的场景。在关联的QUIC监听中选择已创建的QUIC监听。开启后，ALB会向客户端通告HTTP/3协议，支持HTTP/3的客户端将优先通过QUIC监听访问，不支持时自动回退为HTTPS。
仅HTTPS监听支持此配置项。
步骤二：配置SSL证书（仅HTTPS/QUIC监听）
