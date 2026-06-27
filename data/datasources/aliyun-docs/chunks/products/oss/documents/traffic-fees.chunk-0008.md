### 外网流出流量出现非预期增长怎么解决？
当您的Bucket出现外网流出流量异常突增的情况，您可以参考以下方法进行排查解决。
确认流量异常情况。
Bucket已开启实时日志查询
登录[OSS](https://oss.console.aliyun.com/)[管理控制台](https://oss.console.aliyun.com/)。
单击Bucket 列表，然后单击目标Bucket名称。
在左侧导航栏，选择日志管理>实时查询。
在实时查询页签下，输入以下查询和分析语句，查询examplebucket中高频访问文件及其对应的热门访问IP，并按访问次数排序，返回前5条记录。
* and __topic__: oss_access_log and bucket: examplebucket | SELECT client_ip AS ip_address, request_uri AS file_path, COUNT(*) AS access_count, SUM(response_body_length) AS total_bytes_sent FROM log WHERE http_status = 200 GROUP BY request_uri, client_ip ORDER BY access_count DESC LIMIT 5;
查询和分析结果如下：
