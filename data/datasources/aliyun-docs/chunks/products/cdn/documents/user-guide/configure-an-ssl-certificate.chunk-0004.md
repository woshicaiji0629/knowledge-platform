## HTTPS证书配置与回源端口的关系
CDN加速域名的HTTPS证书配置直接影响客户端可用的访问协议，进而影响回源协议和端口。
未配置HTTPS证书时，CDN仅支持HTTP协议访问，回源端口为80。
配置HTTPS证书并开启HTTPS安全加速后，CDN同时支持HTTP和HTTPS协议访问。
回源协议设置为跟随客户端模式时，CDN根据客户端访问协议自动选择回源端口：HTTP访问走80端口回源，HTTPS访问走443端口回源。
回源协议的详细配置方法，请参见[配置回源协议](configure-the-origin-protocol-policy.md)。
