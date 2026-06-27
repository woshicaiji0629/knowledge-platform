## 背景信息
SNI（Server Name Indication）是对SSL/TLS协议的扩展，允许服务器在单个IP地址上承载多个SSL证书，可解决一个HTTPS服务器拥有多个域名但是无法预知客户端到底请求的是哪一个域名的服务问题。开启SNI后，在CDN节点向源站发起TLS握手请求时，源站会根据TLS握手请求中携带的SNI信息来确认被请求的业务域名，返回正确的SSL证书给CDN节点。
重要
源站的服务端需要支持解析TLS握手请求中包含的SNI信息。
如果加速域名配置了多个源站，通过控制台配置SNI功能，所有源站地址会共用一个回源SNI值，那么回源请求都会指向SNI值对应的域名。如果您希望不同的源站，配置不同的SNI值，您可以[填写信息](https://page.aliyun.com/form/act2017566026/index.htm)申请。
回源SNI的工作原理如下图所示。
回源SNI的工作流程如下：
当CDN节点以HTTPS协议访问源站时，需要在SNI中指定访问的具体域名（如：example.com）。
源站接收到请求后，根据SNI中记录的域名，返回对应域名的证书（即example.com的证书）。
CDN节点收到证书，与服务器端建立安全连接。
重要
建议将[回源](configure-the-default-origin-host.md)[HOST](configure-the-default-origin-host.md)和回源SNI设置为相同的域名（通常为源站域名或加速域名）。回源HOST（HTTP Host头）和回源SNI（TLS握手阶段指定的域名）配置不一致时（例如回源HOST设为源站域名但SNI设为加速域名），可能导致SSL握手失败或源站返回错误。两者需在控制台分别配置，请确保匹配源站证书和虚拟主机配置。
