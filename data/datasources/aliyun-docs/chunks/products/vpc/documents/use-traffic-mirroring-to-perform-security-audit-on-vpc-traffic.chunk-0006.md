### 步骤四：可视化分析VPC流量
[登录目标](https://help.aliyun.com/zh/es/user-guide/log-on-to-the-kibana-console#task-761873)[Elasticsearch](https://help.aliyun.com/zh/es/user-guide/log-on-to-the-kibana-console#task-761873)[实例的](https://help.aliyun.com/zh/es/user-guide/log-on-to-the-kibana-console#task-761873)[Kibana](https://help.aliyun.com/zh/es/user-guide/log-on-to-the-kibana-console#task-761873)[控制台](https://help.aliyun.com/zh/es/user-guide/log-on-to-the-kibana-console#task-761873)。在左侧导航栏，单击Kibana>Discover，更改索引模式为filebeat。
您可以添加alert筛选条件，在页面右上角选择查询时间，查看对应时间段内的有潜在威胁的VPC流量。
例如，在查询栏输入alert and 192.168.0.201进行搜索，索引模式为filebeat-*，可查看源 IP 为 192.168.0.201 的告警日志。搜索结果命中 409 条 Suricata 告警记录，告警签名为SURICATA TCPv4 invalid checksum，类别为Generic Protocol Command Decode，严重级别为 3。
