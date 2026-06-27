## 秒级监控
相较于ECS为单块云盘提供的分钟级数据监控，[块存储数据洞察](what-is-a-piece-of-data-is-stored-insight.md)（CloudLens for EBS）针对云盘性能提供了秒级数据监控能力，您可以通过块存储控制台的[云盘分析](cloud-disk-analysis.md)监控到更细粒度的云盘性能变化。
说明
首次使用块存储数据洞察时，需要根据页面提示[开通](cloud-disk-analysis.md)[CloudLens for EBS](cloud-disk-analysis.md)。
登录[块存储](https://ebs.console.aliyun.com/home)[EBS](https://ebs.console.aliyun.com/home)[控制台](https://ebs.console.aliyun.com/home)。
说明
首次登录EBS控制台时，请根据页面提示创建一个EBS服务关联角色。更多信息，请参见[块存储](service-linked-role-for-ebs.md)[EBS](service-linked-role-for-ebs.md)[服务关联角色](service-linked-role-for-ebs.md)。
在左侧导航栏，选择数据洞察(EBS Lens)>云盘分析。
在顶部菜单栏左上角处，选择地域。
在云盘分析页面，找到待查看监控数据的云盘，在操作列单击监控。
在秒级监控页面，在查询时间范围内查看目标云盘的监控数据。
说明
秒级监控数据会有1分钟到5分钟的延迟。因此在查询时，最近1分钟到5分钟的数据有可能是零，表示数据值还没有获取到。
指标说明
