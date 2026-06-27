## 其他优化建议
使用Logtail：有 Batch 与断点续传功能，在保障实时性的同时以最优算法传输数据。Logtail 消耗资源是开源软件（Logstash，FluentD）的1/4，减少CPU消耗。
API写入用户尽量使用64KB~1MB大包写入，减少请求次数。
索引关键字段，例如UserID，Action等，对无用字段不配置索引。
该文章对您有帮助吗？
反馈
