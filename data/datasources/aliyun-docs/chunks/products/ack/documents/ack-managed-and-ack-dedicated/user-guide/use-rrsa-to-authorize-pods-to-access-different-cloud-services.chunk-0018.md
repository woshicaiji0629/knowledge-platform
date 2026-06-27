d)[和](use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)[ARN](use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)[信息](use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)。
<oidc_provider_arn>：替换为当前集群的OIDC提供商ARN。该ARN获取请参见[获取集群中](use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)[OIDC](use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)[提供商的](use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)[URL](use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)[和](use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)[ARN](use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)[信息](use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)。
<namespace>：替换为应用所在的命名空间。
<service_account>：替换为应用使用的服务账户。
您也可以使用命令行工具ack-ram-tool通过自动化的方式配置该策略。对应的命令行示例如下。
ack-ram-tool rrsa associate-role --cluster-id <cluster_id> \ --namespace <namespace> --service-account <service_account> \ --role-name <role_name> --create-role-if-not-exist
