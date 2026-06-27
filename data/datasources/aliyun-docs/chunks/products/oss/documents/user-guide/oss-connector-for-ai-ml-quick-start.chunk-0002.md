## 配置
创建访问凭证配置文件。
mkdir -p /root/.alibabacloud && touch /root/.alibabacloud/credentials
添加访问凭证配置并保存。
示例中的<Access-key-id>、<Access-key-secret>请分别替换为RAM用户的AccessKey ID、AccessKeySecret。关于如何创建AccessKey ID和AccessKeySecret，请参见[创建](../../../ram/documents/user-guide/create-an-accesskey-pair.md)[AccessKey](../../../ram/documents/user-guide/create-an-accesskey-pair.md)，配置项说明以及使用临时访问凭证配置请参见[配置访问凭证](../developer-reference/oss-connector-configuration.md)。
{ "AccessKeyId": "LTAI************************", "AccessKeySecret": "At32************************" }
创建OSS Connector配置文件。
mkdir -p /etc/oss-connector/ && touch /etc/oss-connector/config.json
添加OSS Connector相关配置并保存。配置项说明请参见[配置](../developer-reference/oss-connector-configuration.md)[OSS Connector](../developer-reference/oss-connector-configuration.md)。
正常情况下使用以下默认配置即可。
{ "logLevel": 1, "logPath": "/var/log/oss-connector/connector.log", "auditPath": "/var/log/oss-connector/audit.log", "datasetConfig": { "prefetchConcurrency": 24, "prefetchWorker": 2 }, "checkpointConfig": { "prefetchConcurrency": 24, "prefetchWorker": 4, "uploadConcurrency": 64 } }
