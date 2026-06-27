### 常见问题
VPC流日志可以保存多长时间？
VPC流日志生成后会被自动投递至日志服务中，遵循日志服务产品的保存策略。
创建VPC流日志时如果勾选了开启流日志分析报表功能，则用于存储VPC流日志的Logstore的数据保存时长默认为7天。未勾选时，默认为300天。
可在日志服务控制台[查看现有](../../sls/documents/manage-a-logstore.md)[Logstore](../../sls/documents/manage-a-logstore.md)[的数据保存时间](../../sls/documents/manage-a-logstore.md)，并按需修改。
等保（信息安全等级保护）要求网络日志，如何查询？
阿里云 VPC 默认不记录网络日志。若需满足等保要求，[开启](vpc-flow-logs.md)[VPC](vpc-flow-logs.md)[流日志功能](vpc-flow-logs.md)即可记录并分析出入弹性网卡的流量信息，实现安全合规监控。
该文章对您有帮助吗？
反馈
