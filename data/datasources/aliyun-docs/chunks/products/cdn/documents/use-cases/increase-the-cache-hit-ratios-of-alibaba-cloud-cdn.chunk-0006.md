## 查看缓存命中状态日志
在CDN的请求日志中，记录了所有CDN请求的缓存命中状态。详细日志格式，请参见[快速入门](../user-guide/offline-logs-quick-start.md)。
缓存命中状态字段说明：
HIT：表示命中缓存。
MISS：表示未命中缓存。
说明
命中状态仅表示CDN L1节点的命中状态。例如，CDN L1节点未命中缓存，L2节点命中缓存，日志中仍显示MISS。
日志示例：
26/Jun/2019:10:38:19 +0800] 192.168.53.146 - 1542 "-" "GET http://example.aliyundoc.com/index.html" 200 191 2830 MISS "Mozilla/5.0 (compatible; AhrefsBot/5.0; +http://example.com/robot/)" "text/html"
您也可以调用[查询离线日志下载地址](../developer-reference/api-cdn-2018-05-10-describecdndomainlogs.md)接口，获取加速域名的日志信息。
该文章对您有帮助吗？
反馈
