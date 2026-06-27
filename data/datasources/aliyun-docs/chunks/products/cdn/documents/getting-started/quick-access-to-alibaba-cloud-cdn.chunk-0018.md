### 三、配置CNAME
配置 CNAME 将域名解析指向最近的 CDN 节点，使用户请求通过 CDN 加速。
CNAME记录是一种DNS记录类型，用于将一个域名指向另一个域名，更多关于CNAME的介绍，敬请参考[CNAME](../what-is-a-dns-cname-record.md)[记录简介](../what-is-a-dns-cname-record.md)。
在DNS服务中配置CNAME
前往阿里云CDN控制台的[域名管理列表](https://cdn.console.aliyun.com/domain/list)，找到之前添加的域名，复制域名对应的CNAME值（如果此处值为空，请稍等五秒之后刷新重试）。
在DNS服务器中配置CNAME记录。不同DNS服务商配置CNAME域名解析的方法不同，请以实际情况为准。本文以阿里云和腾讯云为例。
