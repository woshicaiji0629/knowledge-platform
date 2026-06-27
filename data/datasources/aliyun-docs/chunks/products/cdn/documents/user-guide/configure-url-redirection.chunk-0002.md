## 操作步骤
登录[CDN](https://cdn.console.aliyun.com)[控制台](https://cdn.console.aliyun.com)。
在左侧导航栏，单击域名管理。
在域名管理页面，找到目标域名，单击操作列的管理。
在指定域名的左侧导航栏，单击HTTPS配置。
在协议重定向区域，单击修改配置。
在协议重定向对话框，选择跳转类型。

| 跳转类型 | 说明 |
| --- | --- |
| 默认 | 同时支持 HTTP 和 HTTPS 方式的请求。 |
| HTTPS -> HTTP | 将客户端到 CDN 节点的请求强制重定向为 HTTP 方式。 警告 配置 HTTPS 强制跳转 HTTP 后，请勿同时 [配置](configure-hsts.md) [HSTS](configure-hsts.md) ，否则会造成请求重定向循环，从而导致资源无法访问。 |
| HTTP -> HTTPS | 将客户端到 CDN 节点的请求强制重定向为 HTTPS 方式，以确保访问安全。 |

单击确定，完成配置。
