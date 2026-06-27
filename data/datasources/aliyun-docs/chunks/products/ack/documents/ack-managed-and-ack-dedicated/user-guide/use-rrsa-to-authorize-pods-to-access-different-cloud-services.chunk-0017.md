### 使用已存在的RAM角色并授权
如果您的应用需要使用已存在的RAM角色，而非创建新的单独RAM角色，您可以修改RAM角色的信任策略，新增一条允许使用指定的服务账户的应用有权限通过扮演此RAM角色获取临时凭证的信任策略。更多信息，请参见[修改](../../../../ram/documents/user-guide/edit-the-trust-policy-of-a-ram-role.md)[RAM](../../../../ram/documents/user-guide/edit-the-trust-policy-of-a-ram-role.md)[角色的信任策略](../../../../ram/documents/user-guide/edit-the-trust-policy-of-a-ram-role.md)。
RAM角色信任策略中新增的Statement条目内容示例如下。
{ "Action": "sts:AssumeRole", "Condition": { "StringEquals": { "oidc:aud": "sts.aliyuncs.com", "oidc:iss": "<oidc_issuer_url>", "oidc:sub": "system:serviceaccount:<namespace>:<service_account>" } }, "Effect": "Allow", "Principal": { "Federated": [ "<oidc_provider_arn>" ] } }
重要
请替换Statement条目内容示例中的如下字段。
<oidc_issuer_url>：替换为当前集群的OIDC提供商URL。该URL获取请参见[获取集群中](use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)[OIDC](use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)[提供商的](use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)[URL](use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)[和](use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)[ARN](use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)[信息](use-rrsa-to-a
