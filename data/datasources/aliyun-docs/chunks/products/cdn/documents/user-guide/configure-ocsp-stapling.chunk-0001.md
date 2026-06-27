## 功能说明
OCSP（Online Certificate Status Protocol，在线证书状态协议）是由数字证书颁发机构CA（Certificate Authority）提供，客户端通过OCSP可实时验证证书的合法性和有效性。
未开启OCSP Stapling时：客户端的每次请求都会向CA进行OCSP查询，以确认证书未被吊销，频繁的OCSP查询请求导致TLS握手效率较低，将影响用户访问速度。
开启OCSP Stapling功能后，OCSP信息查询的工作将由CDN服务器完成。CDN通过低频次查询，将查询结果缓存到服务器中（默认缓存时间60分钟）。当客户端向服务器发起TLS握手请求时，CDN服务器将证书的OCSP信息和证书一起发送给客户端，无需再向数字证书认证机构（CA）发送查询请求。极大地提高了TLS握手效率，节省了证书验证时间。
重要
OCSP Stapling功能默认关闭。
OCSP Stapling功能默认缓存时间是1小时，缓存过期后第一个访问请求OCSP Stapling将不生效，直到重新获取OCSP Stapling信息为止。
配置了HTTPS加速的域名，可启用或者关闭OCSP Stapling功能，删除HTTPS证书配置后，OCSP Stapling功能会同步失效。
OCSP信息是无法伪造的，因此这一过程不会产生额外的安全问题。
