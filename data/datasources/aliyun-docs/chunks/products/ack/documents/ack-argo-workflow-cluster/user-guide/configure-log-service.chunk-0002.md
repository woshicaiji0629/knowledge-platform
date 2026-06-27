## 注意事项
如果工作流集群开启oss-artifact-repository，同时设置archiveLogs: true，即工作流集群已配置使用oss-artifact-repository存储日志，则SLS日志收集不生效。
相比oss-artifact-repository收集，SLS日志收集具有自动的日志生命周期管理（可配置日志保留的天数），强大的查询能力。如需通过SLS收集日志，可以将archiveLogs: true删除。
