### 审计后端
审计事件采集后，会被存储到Log后端日志文件系统，日志文件为标准的JSON格式。您可以配置并使用如下flag作为API Server的启动参数。
说明
登录到Master节点后，可通过/etc/kubernetes/manifests/kube-apiserver.yaml查看API Server的配置文件。

| 配置参数 | 说明 |
| --- | --- |
| --audit-log-maxbackup | 指定审计日志可分片存储的最大文件数量，为 10 个。 |
| --audit-log-maxsize | 指定单个审计日志的最大内存容量，为 100 MB。 |
| --audit-log-path | 指定审计日志的输出路径，为 /var/log/kubernetes/kubernetes.audit 。 |
| --audit-log-maxage | 指定审计日志最长的保存周期，为 7 天。 |
| --audit-policy-file | 配置审计日志策略的文件路径，为 /etc/kubernetes/audit-policy.yml 。 |
