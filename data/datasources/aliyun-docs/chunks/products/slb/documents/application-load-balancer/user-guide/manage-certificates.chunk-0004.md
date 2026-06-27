## 添加证书
- 登录[应用型负载均衡](https://slb.console.aliyun.com/alb)[ALB](https://slb.console.aliyun.com/alb)[控制台](https://slb.console.aliyun.com/alb)。
在顶部菜单栏处，选择实例所属的地域。
在实例页面，找到目标实例，单击实例ID。
选择以下一种方法，打开监听配置向导。
在实例页面，在目标实例操作列单击创建监听。
在实例页面，单击目标实例ID。在监听页签，单击创建监听。
在配置监听配置向导，完成以下配置，然后单击下一步。
本文仅列举强相关参数，更多信息，请参见[添加](add-an-https-listener.md)[HTTPS](add-an-https-listener.md)[监听](add-an-https-listener.md)。

| 监听配置 | 说明 |
| --- | --- |
| 选择监听协议 | 选择监听的协议类型。 您可以根据需要选择 HTTPS 或 QUIC 。 说明 QUIC 监听暂不支持双向认证。 HTTP 监听不支持单向认证和双向认证。 本文选择 HTTPS 。 |
| 监听端口 | 输入用来接收请求并向后端服务器进行请求转发的监听端口，端口范围为 1~65535。通常 HTTP 协议使用 80 端口，HTTPS 协议使用 443 端口。 本文输入 443 。 |
| 监听名称 | 输入自定义监听名称。 |
| 高级配置 | 单击 修改 展开高级配置。 |
