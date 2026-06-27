## 注意事项
开启Range回源有以下注意事项：
开启Range回源前需确认源站是否支持Range请求，即HTTP请求头中包含Range字段，并且源站能够响应正确的206文件分片。如果源站不支持Range请求，开启Range回源可能导致缓存异常或客户端请求失败。
Range回源是可选配置项，控制台默认未开启。
Multipart Ranges特性状态默认关闭，开启Range回源功能也不会同步开启Multipart Ranges特性，请[提交工单](https://smartservice.console.aliyun.com/service/create-ticket?spm=a2c4g.11186623.0.0.629c1faeE1XJOx)申请开启Multipart Ranges特性。
开启Range回源功能以后，会导致回源的QPS升高，如果源站有设置频次控制功能，需要注意避免触发源站的限流；规避办法是通过[DescribeL2VipsByDomain](../developer-reference/api-cdn-2018-05-10-describel2vipsbydomain.md)查询回源节点的IP地址 ，并且将回源节点的IP加入源站的访问IP白名单。
