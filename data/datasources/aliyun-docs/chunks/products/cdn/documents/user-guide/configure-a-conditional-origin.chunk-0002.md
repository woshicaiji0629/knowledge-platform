## 源站为OSS时的注意事项
若源站为OSS，需要添加该源站地址到域名管理>基本配置>源站信息中，并且将源站类型设置为OSS域名，以便CDN与OSS正常鉴权。
多 OSS 源站场景：当配置多个 OSS 源站时，必须为每个源站配置[指定源站回源](specify-an-origin-host-for-each-origin.md)[HOST](specify-an-origin-host-for-each-origin.md)，且 Host 值需与对应的 OSS Bucket 域名完全一致（例如dev-3mir.oss-cn-guangzhou.aliyuncs.com）。
若未正确配置或依赖默认回源 Host，请求可能随机回源至错误的 Bucket，导致 403 SignatureDoesNotMatch（签名验证失败）或 404 Not Found 错误。每条条件回源规则（包括匹配规则和不匹配/兜底规则）都需要明确绑定对应的源站和回源 Host。建议在配置多个源站时，将基础源站的权重设置为一致，并为每个条件源站配置独立的规则条件，以确保回源路径可控。
