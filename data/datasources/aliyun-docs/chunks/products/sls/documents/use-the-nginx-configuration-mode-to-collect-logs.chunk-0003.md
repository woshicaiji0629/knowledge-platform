## 操作步骤
登录[日志服务控制台](https://sls.console.aliyun.com)。
在Project列表区域，单击目标Project。
在日志存储>日志库页签中，单击目标Logstore。
展开LogStore选项卡，单击Logtail 配置，然后单击添加Logtail配置。
在弹出的快速数据接入页面中，选择Nginx - 文本日志>立即接入。
在机器组配置步骤中，选择已创建的机器组。在机器组配置步骤中，使用场景选择主机场景，安装环境选择ECS。在选择机器组区域，将目标机器组（例如group-ip）从源机器组移至应用机器组，然后单击下一步。
在Logtail配置步骤中，配置以下选项。
配置名称：输入Logtail采集配置名称，例如nginx-logs。
文件路径：输入日志的存放路径，例如/var/log/nginx/**/access*表示/var/log/nginx目录（包含该目录的递归子目录）中以access开头的文件。
处理配置：单击NGINX模式解析，在弹出的处理插件页签中，输入标准NGINX配置文件日志配置部分，通常以log_format开头。日志服务将自动提取对应字段。例如：
log_format main '$remote_addr - $remote_user [$time_local] "$request" ' '$request_time $request_length ' '$status $body_bytes_sent "$http_referer" ' '"$http_user_agent"';
在原始字段中填写content。日志服务将根据配置自动生成正则表达式并提取对应字段。
其他配置项保持默认即可。如需了解更多配置信息，请参见[采集主机文本日志](collect-host-logs.md)。
在查询分析配置步骤中，单击刷新，可预览采集到的数据。
单击下一步，结束配置流程。您可在此单击查询日志，系统将跳转至LogStore查询分析页面。您需要等待1分钟左右，待索引生效后，才能在原始日志页签中，查看已采集到的日志。更多信息，请参见[查询与分析快速指引](quick-guide-to-query-and-analysis.md)。
