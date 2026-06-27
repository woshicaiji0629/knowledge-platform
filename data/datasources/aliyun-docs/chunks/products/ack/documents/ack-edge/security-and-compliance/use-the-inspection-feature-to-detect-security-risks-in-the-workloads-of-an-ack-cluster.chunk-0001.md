## 前提条件
集群版本为v1.14及以上版本。如需升级集群，请参见[手动升级集群](../../ack-managed-and-ack-dedicated/user-guide/update-the-kubernetes-version-of-an-ack-cluster.md)。
如果您当前使用的是RAM用户，请确保已参见下方内容完成RAM授权和RBAC授权。
RAM授权
请完成配置巡检页面的RAM授权操作，确保当前RAM用户拥有操作当前集群的配置巡检页面的权限，否则会出现权限不足无法操作配置巡检页面功能的问题。具体操作，请参见[使用](../../ack-managed-and-ack-dedicated/user-guide/create-a-custom-ram-policy.md)[RAM](../../ack-managed-and-ack-dedicated/user-guide/create-a-custom-ram-policy.md)[授予集群及云资源访问权限](../../ack-managed-and-ack-dedicated/user-guide/create-a-custom-ram-policy.md)。
展开查看配置巡检授权代码
{ "Statement": [ { "Action": [ "cs:DescribePolarisConfig", "cs:DescribePolarisJob", "cs:DescribePolarisCronJob", "cs:UpdatePolarisJob", "cs:UpdatePolarisCronJob" ], "Effect": "Allow", "Resource": [ "acs:cs:*:*:cluster/<yourclusterID>" ] } ], "Version": "1" }
如果您需要使用巡检报告功能，请完成日志服务指定logproject（当前集群logtail-ds组件所使用的logproject）的RAM授权，确保当前RAM用户拥有日志服务指定logproject的数据读取权限，否则会出现权限不足无法查看巡检报告的问题。具体操作，请参见[RAM](../../../../sls/documents/use-custom-policies-to-grant-permissions-to-a-ram-user.md)[自定义授权示例](../../../../sls/documents/use-custom-policies-to-grant-permissions-to-a-ram-user.md)。
展开查看日志服务日志读取授权代码
{ "Version": "1", "Statement": [ { "Action": [ "log:Get*", "l
