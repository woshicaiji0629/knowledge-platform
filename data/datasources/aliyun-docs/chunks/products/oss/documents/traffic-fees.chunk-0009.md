### Bucket未开启实时日志查询
登录[OSS](https://oss.console.aliyun.com/)[管理控制台](https://oss.console.aliyun.com/)。
单击Bucket 列表，然后单击目标Bucket名称。
在左侧导航栏，选择用量查询>热点统计，然后单击热点 Referer/IP页签，查看Top 10（Referer/IP）。
在左侧导航栏，选择用量查询>文件访问统计，查看高频访问文件的文件名、产生的流出流量。
识别是否为异常流量。
如果发现某些IP地址频繁请求特定对象，可能是恶意行为，请执行[步骤](traffic-fees.md)[3](traffic-fees.md)检查相关配置。
如果发现多个IP地址访问不同对象，可能是内容被大规模分发（如社交媒体传播），请执行[步骤](traffic-fees.md)[4](traffic-fees.md)配置CDN加速访问OSS。
检查相关配置。
