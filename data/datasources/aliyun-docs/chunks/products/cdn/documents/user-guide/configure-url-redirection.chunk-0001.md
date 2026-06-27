## 适用场景
已经配置了HTTPS证书的加速域名，可配置强制跳转，默认通过301重定向方式，将客户端到CDN节点的HTTP请求强制跳转为HTTPS请求，HTTPS请求更安全。
$ curl http://xxx xxx xxx/' -i HTTP/1.1 301 Moved Permanently Server: Tengine Date: Mon, 03 Jun 2019 13:26:01 GMT Content-Type: text/html Content-Length: 278 Connection: keep-alive Location: https://xxx xxx xxx/ Via: cache2.cn201[,0] Timing-Allow-Origin: * EagleId: 2a786b0215595683612635433e &lt;!DOCTYPE HTML PUBLIC &quot;-//IETF//DTD HTML 2.0//EN&quot;&gt; <html> <head><title>301 Moved Permanently</title></head> <body bgcolor="white"> <h1>301 Moved Permanently</h1> <p>The requested resource has been assigned a new permanent URI.</p> &lt;hr/&gt;Powered by Tengine</body> </html>
强制跳转功能默认使用301重定向方式，同时也支持308重定向方式，如果您需要修改重定向方式，可以通过[填写信息](https://page.aliyun.com/form/act2017566026/index.htm)申请。

| 编码 | 含义 | 处理方法 | 典型应用场景 |
| --- | --- | --- | --- |
| 301 | Moved Permanently | GET 方法不会发生变更，其他方法有可能会变更为 GET 方法。 | 网站重构。 |
| 308 | Permanent Redirect | 方法和消息主体都不发生变化。 | 网站重构，用于非 GET 方法。(with non-GET links/operations) |
