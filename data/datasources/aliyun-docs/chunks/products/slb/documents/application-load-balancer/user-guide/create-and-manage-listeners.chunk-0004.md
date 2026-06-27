### 控制台
步骤一：配置监听
前往ALB控制台的[实例](https://slb.console.aliyun.com/alb/cn-hangzhou/albs)页面，单击目标实例ID，在监听页签下单击创建监听。
在配置监听配置向导，完成以下配置，然后单击下一步。
选择监听协议：HTTP、HTTPS或QUIC。
监听端口：端口范围为1~65535。通常HTTP使用80端口，HTTPS使用443端口。
同一个ALB实例内，相同协议的监听端口不能重复。此外，HTTP和HTTPS监听也不能使用相同端口。
监听名称：输入监听的自定义名称。
标签：以键值对形式标记监听。
高级配置：单击修改展开。
启用HTTP2.0：仅HTTPS监听支持。
连接空闲超时时间：取值范围1~600秒，默认15秒。超时后连接将被断开。如需提升最大超时时间，请前往[配额中心](https://quotas.console.aliyun.com/products/alb/quotas?query=alb_quota_max_idle_timeout)申请。
当监听协议为HTTP时，连接空闲超时时间对HTTP 2.0请求暂不生效。
连接请求超时时间：取值范围1~600秒，默认60秒。超时后返回HTTP 504错误码。如需提升最大超时时间，请前往[配额中心](https://quotas.console.aliyun.com/products/alb/quotas?query=alb_quota_max_request_timeout)申请。
数据压缩：开启后对响应内容进行压缩，仅当Content-Length超过1024字节时触发。支持Brotli（所有类型）和Gzip（压缩级别为 Level 4），客户端同时支持时优先使用Brotli。
Gzip支持的类型：text/xml、text/plain、text/css、application/javascript、application/x-javascript、application/rss+xml、application/atom+xml、application/xml、application/json。
查找真实客户端源IP：开启后，ALB从X-Forwarded-For头字段中提取真实客户端IP。需设置可信IP列表：
0.0.0.0/0：取X-Forwarded-For中最左边的地址。
proxy1 IP;proxy2 IP;..：从右往左取第一个不在列表中的值。
开启后，转发规则中基于SourceIp匹配和QPS(基于客户端源IP限速)将使用真实客户端IP。
QUIC监听不支持此配置项。仅标准版、WAF增强版实例支持，基础版不支持。
附加HTTP头字段：选择要添加的HTTP头字段，用于获取客户端IP、监听协议、端口等信息。各头字段的详细
