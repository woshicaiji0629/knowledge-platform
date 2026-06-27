URL 的长度之和，不能超过 256 KB，否则返回 400 错误码。 |
| 请求方式 | 常见的 HTTP 请求方式里面， CDN 支持 GET 、 PUT 、 POST 、 HEAD 和 OPTIONS 这几种请求方式。 说明 如果需要支持 DELETE 和 PATCH 请求方式，请使用 DCDN 全站加速产品，并且开启动态加速功能。 PUT 请求方式支持带有请求体（BODY）或者不带请求体（ Content-Length=0 ）的 HTTP 请求。 POST 请求方式支持 chunk 编码，支持带有请求体（BODY）或者不带请求体（ Content-Length=0 ）的 HTTP 请求。 对于访问静态缓存资源的场景，默认情况下，CDN 节点会将用户的 HEAD 请求转换为 GET 请求方式回源，如果您希望保持 HEAD 请求方式回源， 请 [提交工单](https://selfservice.console.aliyun.com/ticket/createIndex) ，联系客服为您处理。 |
| 物联网卡访问限制 | 根据中华人民共和国工业和信息化部（简称：工信部）的相关规定（《关于印发〈物联网卡安全分类管理实施指引（试行）〉的通知》（工网安函[2020]1173 号）），阿里云 CDN 产品在中国内地无法为使用物联网卡的终端提供加速服务，终端设备使用物联网卡来访问阿里云 CDN 节点的情况下，很可能会无法连接到节点 IP。 |
| HTTPS 访问限制 | 如果客户端在发起与 CDN 节点的 SSL 握手时没有传递 SNI 信息，则 CDN 节点无法保证能够握手成功。 |
