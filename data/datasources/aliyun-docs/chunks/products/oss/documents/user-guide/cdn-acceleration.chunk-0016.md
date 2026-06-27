Name Indication）的CDN回源请求导致OSS访问异常，需在CDN中[配置默认回源](../../../cdn/documents/user-guide/configure-sni.md)[SNI](../../../cdn/documents/user-guide/configure-sni.md)，并设置其与回源HOST相同（回源HOST默认为加速域名）。当回源请求携带SNI时，OSS能够在TLS握手阶段精准识别业务域名，从而返回匹配的证书。若OSS接收到不携带SNI的请求，将无法进行业务域名的精准识别，可能触发更严格的流量限制。
隐藏源站信息
默认情况下，CDN使用Bucket域名回源。当回源出错时（如文件不存在），错误信息中可能暴露OSS Bucket域名，存在安全风险。为隐藏源站信息，可按以下步骤将回源HOST修改为CDN加速域名：
在[Bucket](https://oss.console.aliyun.com/bucket)[列表](https://oss.console.aliyun.com/bucket)页面单击目标Bucket名称，然后在Bucket 配置>域名管理中将CDN加速域名绑定到Bucket。
在CDN控制台单击目标加速域名，然后在回源配置>默认回源HOST中单击修改配置，将域名类型修改为加速域名。
行为审计与排障：启用访问日志
生产环境必须具备完善的日志记录能力，以便进行安全审计、性能分析和故障排查。建议在CDN控制台[配置实时日志推送](../../../cdn/documents/user-guide/configure-real-time-log-delivery.md)，将访问日志投递到日志服务SLS。通过SLS，可以对访问行为、流量分布、热门资源、错误请求等进行深度分析和监控告警。
