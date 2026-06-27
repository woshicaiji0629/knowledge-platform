### 检查日志文件，识别异常流量
基础查询：离线日志
通过下载离线日志，查看相关时间段的访问日志，分析HTTP请求的详细信息，识别可疑的IP地址、User-Agent等。离线日志字段数据相对较少，如果您想查看更多数据，可使用实时日志功能。
获得离线日志文件后，您可以使用命令行工具来快速解析日志文件，提取访问量TOP10的IP地址或User-Agent等信息，详情请参见[CDN](../analysis-method-of-alibaba-cloud-content-delivery-network-access-log.md)[访问日志的分析方法](../analysis-method-of-alibaba-cloud-content-delivery-network-access-log.md)。
进阶查询：运营报表和实时日志
重要
运营报表需定制后才会进行生产统计分析，如果您之前已配置过实时日志推送或订阅运营报表，您可以查看到过去的日志信息。运营报表为CDN自带免费功能，无需额外付费。
实时日志需要开通日志服务（SLS）并成功投递日志后，才会生成实时日志。实时日志为付费功能，具体计费请参见[计费详情](../user-guide/overview-1.md)。
实时日志和运营报表均需要提前配置，如果您在产生高额账单之前未配置过这两项功能，只能通过离线日志进行历史数据分析。
运营报表
定制运营报表后，您可以看到用户访问的PV/UV、地区和运营商、域名排行、热门referer、热门URL、回源热门URL和Top客户端IP等报表内容。具体操作请参见[定制和订阅运营报表](../user-guide/customize-an-operations-report-template-and-create-a-tracking-task.md)。
实时日志
如果您想查询更多日志信息，例如Referer和URI等信息，需要开通[日志服务](https://sls.console.aliyun.com)[SLS](https://sls.console.aliyun.com)，将采集到的实时日志实时推送至日志服务。开启实时日志，并成功投递日志后，根据日志投递条数产生计费。
参考[配置实时日志推送](../user-guide/configure-real-time-log-delivery.md)为需要分析用户访问数据的CDN加速域名配置实时日志推送。
在实时日志功能页面找到需要分析日志的Project名称，单击日志分析。
进入日志分析页面，在右上角过滤时间段，单击左侧原始日志页签，找到refer_domain字段，您可以看到由高到低排列的Referer信息。
