## 背景信息
HSTS（HTTP Strict Transport Security，HTTP 严格传输安全），是一种网站用来声明他们只能使用安全连接（HTTPS）访问的方法。
配置HSTS后，客户端第一次使用HTTPS与CDN节点连接时，CDN节点通过使用响应头来告知客户端后续一段时间内访问时只能使用HTTPS访问，并阻止HTTP请求，HSTS响应头结构为：Strict-Transport-Security:max-age=expireTime [;includeSubDomains] [;preload]，参数说明如下表所示。

| 参数 | 说明 |
| --- | --- |
| max-age | HSTS Header 的过期时间，单位为秒，客户端在此时间段内强制使用 HTTPS 访问。 |
| includeSubDomains | 可选参数。如果包含这个参数，说明该域名及其所有子域名均开启 HSTS。 |
| preload | 可选参数。当您申请将域名加入到浏览器内置列表时需要使用 preload 列表。 |

客户端会记录域名在max-age到期前强制执行HSTS策略，客户端发起HTTP请求时将被强制转换为HTTPS请求，HTTP请求将被阻止。
说明
配置HSTS后，如果客户端第一次访问时使用HTTP，此时由于HSTS策略未同步至客户端，CDN节点会将该HTTP请求301重定向到HTTPS，从而避免此安全隐患。
