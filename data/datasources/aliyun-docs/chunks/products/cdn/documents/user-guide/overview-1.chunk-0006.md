## 适用场景
实时日志可以帮助您分析加速域名遇到的异常问题，也可以帮助您了解用户的访问情况。当前阿里云CDN提供4类日志数据报表，如下表所示。

| 日志分析场景 | 报表作用描述 |
| --- | --- |
| CDN 基础数据 | 该数据可以帮助您快速了解到 CDN 整体的服务质量以及终端用户的访问效率（命中率、访问延时、下载速度等），同时也可以在服务质量出现异常情况下及时进行处理。 |
| CDN 访问错误 | 该数据可以帮助您在应用访问出现异常时，快速定位到 CDN 服务问题的源头，例如：部分 URI 问题、源站出现故障、部分节点不可用、部分省份网络问题、部分运营商网络问题等。 |
| CDN 热门资源 | 该数据可以帮助您更好地了解热门资源情况，分析出热门域名、热门 URI、热门省份、热门运营商等，您也可以从热门数据了解到您的运营活动效果是否正常、热点时间内流量的上涨是否符合预期，以帮助您及时调整运营策略。 |
| CDN 用户构成 | 该数据可以帮助您更好地了解网站的用户构成，包括用户的客户端类型、省份、运营商等，也能够统计出访问量 TOP 用户、下载量 TOP 用户。 |

如果您想开通实时日志推送服务，请参见[配置实时日志推送](configure-real-time-log-delivery.md)。
开通后，您可以通过[投递](best-practices-for-shipping-and-analyzing-alibaba-cloud-cdn-real-time-logs-in-log-service.md)[CDN](best-practices-for-shipping-and-analyzing-alibaba-cloud-cdn-real-time-logs-in-log-service.md)[实时日志到](best-practices-for-shipping-and-analyzing-alibaba-cloud-cdn-real-time-logs-in-log-service.md)[SLS](best-practices-for-shipping-and-analyzing-alibaba-cloud-cdn-real-time-logs-in-log-service.md)[来分析用户访问数据](best-practices-for-shipping-and-analyzing-alibaba-cloud-cdn-real-time-logs-in-log-service.md)来了解如何使用日志分析模块及实现常见的用户访问数据分析。
该文章对您有帮助吗？
反馈
