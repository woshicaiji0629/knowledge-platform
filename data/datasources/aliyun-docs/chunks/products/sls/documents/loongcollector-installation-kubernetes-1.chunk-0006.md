| 参数说明 | values.yaml # ===================== 必需要补充的内容 ===================== # 本集群要采集的 Project 名，例如 k8s-log-custom-sd89ehdq projectName: "" # Project 所属地域，例如上海：cn-shanghai region: "" # Project 所属主账号 uid，请用引号包围，例如"123456789" aliUid: "" # 使用网络，可选参数：公网 Internet，内网 Intranet，默认使用公网 net: Internet # 主账号或者子账号的 AK，SK accessKeyID: "" accessKeySecret: "" # 自定义集群 ID，命名只支持大小写，数字，短划线(-)。 clusterID: "" # ...省略非必填参数... |
| --- | --- |
| projectName String (必填) Project 名称，LoongCollector 将上传日志到该 Project 中。命名规则如下： 项目名称仅支持小写字母、数字和连字符（-）。 必须以小写字母开头，以小写字母和数字结尾。 名称长度为 3～63 个字符。 |  |
| region String (必填) Project 所属地域 ID，请参考 [地域](loongcollector-installation-kubernetes-1.md) 查看 Project 所在地域的 ID。 |  |
| aliUid String (必填) Project 所属的阿里云 主账号 ID 。 |  |
| net String (必填) 日志数据传输使用的 [网络类型](loongcollector-installation-kubernetes-1.md) 。 Internet（默认值）：公网。 Intranet：内网。 |  |
| accessKeyID String (必填) Project 所属账号的 AccessKey ID。推荐使用 RAM 用户的 AccessKey，并授予 RAM 用户 AliyunLogFullAccess 系统策略权限。RAM 相关概念请参见 [RAM](../../ram/documents/user-guide/overview-of-ram-users.md) [用户概览](../../ram/documents/user-guide/overview-of-ram-users.md) 。 |  |
| accessKeySecret String (必填) Project 所属账号的 AccessKey Secret。 |  |
| clusterID String (必填
