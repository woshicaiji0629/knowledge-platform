## 新创建集群
登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。
在集群列表页面中，单击页面右上角的创建集群。
单击ACK Edge 集群页签，在页签最下方展开高级选项（选填），找到Secret 落盘加密，选中选择 KMS 密钥，在下拉框中选择KMS密钥ID。
如果您未创建KMS密钥，请单击创建密钥，前往[密钥管理服务控制台](https://kms.console.aliyun.com)创建密钥。具体操作，请参见[创建密钥](../../../../kms/documents/key-management-service/support/create-a-cmk.md)。
关于创建ACK Edge集群Pro版的其他配置信息，请参见[创建集群](../user-guide/create-an-ack-edge-cluster-1.md)。
登录[操作审计控制台](https://actiontrail.console.aliyun.com)，在左侧导航栏单击事件查询，在事件查询页面有使用aliyuncsmanagedsecurityrole系统角色的加密和解密事件日志，则说明该集群后台已成功开启Secret落盘加密特性。
