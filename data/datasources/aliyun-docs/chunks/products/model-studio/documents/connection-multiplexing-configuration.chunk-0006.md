### HTTP异步调用方式
在异步调用场景中，您可以通过aiohttp.ClientSession配合aiohttp.TCPConnector实现连接复用。TCPConnector支持配置连接数限制等参数：

| 参数 | 含义 | 默认值 | 备注 |
| --- | --- | --- | --- |
| limit | 总连接数限制 | 100 | 控制最大连接数。在高并发场景下，适当增加此值可以提高并发能力。 |
| limit_per_host | 每个主机的连接数限制 | 0（无限制） | 限制对单个主机的最大连接数，避免对单一服务端造成过大压力。 |
| ssl | SSL 上下文配置 | None | 用于 HTTPS 连接的 SSL 证书验证配置。 |
