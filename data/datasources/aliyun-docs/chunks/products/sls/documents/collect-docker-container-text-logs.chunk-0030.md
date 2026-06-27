### 常见错误信息

| 错误现象 | 原因 | 解决方案 |
| --- | --- | --- |
| Failed to connect to Logtail | Project 地域与 LoongCollector（Logtail）容器不一致 | 检查 ALIYUN_LOGTAIL_CONFIG 中的地域配置 |
| No logs in LogStore | 文件路径配置错误 | 确认业务容器内日志路径与采集配置匹配 |
