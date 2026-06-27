## 回源限制

| 限制项 | 说明 |
| --- | --- |
| 回源请求头最大长度 | 最大不能超过 300 Bytes。 |
| 回源请求超时时间 | TCP 层默认为 10 秒，HTTP 层默认为 30 秒。 |
| 回源的 Content-Type | 如果源站不响应 Content-Type ， CDN 会自动添加 Content-Type:application/octet-stream 。 |
| Head 请求默认转换为 Get 请求方式回源 | 默认情况下，用户的 Head 请求经过阿里云 CDN 节点之后再访问源站，会被自动转换为 Get 请求方式，如果您希望保持 Head 请求回源的方式， 请 [提交工单](https://selfservice.console.aliyun.com/ticket/createIndex) ，联系客服为您处理。 |
| 回源请求头默认的字符串格式转化 | 使用 回源 HTTP 请求头 功能添加的回源请求头，在实际回源的时候，字符串的大小写格式会被自动转换成驼峰式，例如： 示例 1：回源请求头 ALI-CDN 在实际回源的时候会被改写为 Ali-Cdn 。 示例 2：回源请求头 ALICDN 在实际回源的时候会被改写为 Alicdn 。 如果您需要关闭默认改写，可以通过 回源 HTTP 请求头 功能添加以下回源请求头： 自定义参数： Ali-Swift-Header-Capitalize 取值：off |
