## C Producer
日志服务量身定制的日志数据采集解决方案。
日志服务客户端Logtail在X86服务器上有百万级部署，可以参见文章：Logtail技术分享：[多租户隔离技术+双十一实战效果](https://yq.aliyun.com/articles/251629?spm=a2c4g.11186623.2.22.2dfc505eazEyHL)，[Polling+Inotify 组合下的日志保序采集方案](https://yq.aliyun.com/articles/204554?spm=a2c4g.11186623.2.23.2dfc505eazEyHL)。除此之外，日志服务提供多样化的采集方案：
移动端SDK：Android/iOS平台数据采集，一天已有千万级DAU。
Web Tracking（JS）：类似百度统计，Analytics轻量级采集方式，无需签名。
日志服务团队结合IoT设备的特点，为IoT设备量身定制一套日志数据采集方案：C Producer。
