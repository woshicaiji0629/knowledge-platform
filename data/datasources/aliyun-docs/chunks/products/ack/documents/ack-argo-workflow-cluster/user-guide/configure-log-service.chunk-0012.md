## 关闭日志服务
执行以下命令，删除AliyunLogConfig CR。
kubectl delete aliyunlogconfigs.log.alibabacloud.com workflow-sls-config -n default
登录[日志服务控制台](https://sls.console.aliyun.com/)，将名为workflow-logstore的日志库删除。
该文章对您有帮助吗？
反馈
