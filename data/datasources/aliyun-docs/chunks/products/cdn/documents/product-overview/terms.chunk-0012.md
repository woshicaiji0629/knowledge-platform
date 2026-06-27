## 回源SNI
SNI（Server Name Indication）是对SSL/TLS协议的扩展，可用来解决一个HTTPS服务器（同一个IP地址）拥有多个域名，但是无法确定客户端到底请求的是哪一个域名的服务的问题。
当您的源站IP绑定了多个域名，且CDN回源协议为HTTPS时，可通过配置回源SNI，来指明客户端从哪个域名获取资源，服务器会根据配置的SNI信息返回正确的证书给客户端。具体操作，可参见[配置默认回源](../user-guide/configure-sni.md)[SNI](../user-guide/configure-sni.md)。
