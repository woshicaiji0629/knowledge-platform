## 相关文档
什么是源站，请参见[源站](../product-overview/terms.md)。
当您使用多个源站进行加速时，可以通过设置不同的回源HOST来指定CDN节点回源到不同的源站，请参见[配置默认回源](configure-the-default-origin-host.md)[HOST](configure-the-default-origin-host.md)。
如果您需要自定义HTTP或HTTPS回源协议，请参见[配置回源协议](configure-the-origin-protocol-policy.md)。
如果您的源站使用的是阿里云对象存储OSS，并且OSS的Bucket被配置为私有模式，需要给加速域名开启OSS私有Bucket回源功能，请参见[OSS](grant-alibaba-cloud-cdn-access-permissions-on-private-oss-buckets.md)[私有](grant-alibaba-cloud-cdn-access-permissions-on-private-oss-buckets.md)[Bucket](grant-alibaba-cloud-cdn-access-permissions-on-private-oss-buckets.md)[回源](grant-alibaba-cloud-cdn-access-permissions-on-private-oss-buckets.md)。
如果您的源站IP绑定了多个域名，且CDN回源协议为HTTPS时，需配置回源SNI，请参见[配置默认回源](configure-sni.md)[SNI](configure-sni.md)。
该文章对您有帮助吗？
反馈
