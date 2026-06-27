## 步骤一：创建数据加工任务
登录[日志服务控制台](https://sls.console.aliyun.com)。
进入数据加工页面。
在Project列表区域，单击目标Project。
在日志存储>日志库页签中，单击目标Logstore。
在查询与分析页面，单击数据加工。
在页面右上角，选择数据的时间范围。
选择时间范围后，请确认原始日志页签中存在日志。
在编辑框中，输入如下加工SPL规则。
* | extend status=cast(status as BIGINT) | where status>=0 AND status<500 | project-away remote_addr, remote_user
调试SPL规则。
从原始数据中选择测试数据，或者手动填入测试数据。
[ { "body_bytes_sent": "1061", "http_user_agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; ru-RU) AppleWebKit/533.18.1 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5", "remote_addr": "192.0.2.2", "remote_user": "vd_yw", "request_method": "DELETE", "request_uri": "/request/path-1/file-5", "status": "400", "time_local": "10/Jun/2021:19:10:59", "error": "Invalid time range" } ]
点击▷，执行调试运行。
查看预览结果。执行完成后，切换到加工结果标签页查看结果。加工后的日志已被结构化为多个字段，例如body_bytes_sent、error、http_user_agent、request_method、request_uri、status、time_local等。
创建数据加工任务。
单击保存数据加工（新版）。
在创建数据加工任务（新版）面板中，配置如下信息，然后单击确定。
