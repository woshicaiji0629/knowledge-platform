# 通过RRSA配置ServiceAccount的RAM权限实现Pod权限隔离-容器服务 Kubernetes 版 ACK(ACK)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [产品概述](products/ack/documents/ack-managed-and-ack-dedicated/product-overview.md)

- [快速入门](products/ack/documents/ack-managed-and-ack-dedicated/getting-started.md)

- [操作指南](products/ack/documents/ack-managed-and-ack-dedicated/user-guide.md)

- [实践教程](products/ack/documents/ack-managed-and-ack-dedicated/use-cases.md)

- [安全合规](products/ack/documents/ack-managed-and-ack-dedicated/security-and-compliance.md)

- [开发参考](products/ack/documents/ack-managed-and-ack-dedicated/developer-reference.md)

- [服务支持](products/ack/documents/ack-managed-and-ack-dedicated/support.md)

[首页](https://help.aliyun.com/zh)

# 通过RRSA配置ServiceAccount的RAM权限实现Pod权限隔离

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/kubernetes)

[我的收藏](https://help.aliyun.com/my_favorites.html)

基于适用于服务账户的RAM角色（RAM Roles for Service Accounts，简称RRSA）功能，您可以在集群内实现Pod维度的OpenAPI权限隔离，从而实现云资源访问权限的细粒度隔离，降低安全风险。本文介绍如何在集群中使用RRSA。

## 背景信息

ECS实例元数据包含了在阿里云系统中关于ECS实例（ECI实例基于ECS实例实现）的详细信息。您可以在运行中的实例内部访问这些元数据，从而配置或管理实例。通过实例元数据，Kubernetes集群内应用可以获取实例RAM角色策略生成的STS临时凭证，并通过这些临时凭证访问云资源OpenAPI。更多信息，请参见[实例元数据](products/ecs/documents/user-guide/view-instance-metadata.md)。

出于安全考虑，当您需要限制集群内不同应用的RAM权限时，应禁止这些应用通过ECS或ECI实例元数据获取您的实例关联角色对应的临时凭证，或者不为实例关联角色分配任何RAM权限策略。然而，这些应用仍然需要一种安全的途径去获取访问云资源的临时凭证。因此，阿里云容器服务ACK联合RAM访问控制服务推出了RRSA功能。

基于RRSA功能，您可以在集群内实现Pod级别隔离的应用关联RAM角色功能。各个应用可以扮演独立的RAM角色并使用获取的临时凭证访问云资源，从而实现应用RAM权限最小化以及无AccessKey访问阿里云OpenAPI避免AccessKey泄露的需求。

从用户侧视角来看，RRSA功能的工作流程如下。

- 

用户提交使用了服务账户令牌卷投影功能的应用Pod。

- 

集群将为该应用Pod创建和挂载相应的服务账户OIDC Token文件。

- 

Pod内程序使用挂载的OIDC Token文件访问STS服务的AssumeRoleWithOIDC接口，获取扮演指定RAM角色的临时凭证。

说明

- 

请提前修改RAM角色配置，允许Pod使用的服务账户扮演该RAM角色。更多信息，请参见[AssumeRoleWithOIDC](products/ram/documents/api-assumerolewithoidc.md)。

- 

从文件中读取的OIDC Token是一个临时Token，建议应用程序每次在使用时都从文件中读取最新的Token，集群会在Token过期前更新替换文件内已有的Token。

- 

Pod内程序使用获取到的临时凭证访问云资源OpenAPI。

## 使用限制

RRSA功能目前仅支持1.22及以上版本的集群，即ACK托管集群基础版、ACK托管集群Pro版、ACK Serverless集群基础版、ACK Serverless集群Pro版和ACK Edge集群Pro版。

## 启用RRSA功能

若未创建集群，您可以在创建ACK托管集群和ACK Edge集群时开启，若已创建集群，可在集群信息页面的安全与审计页签下开启。

ACK Serverless集群仅支持集群创建后在集群信息页面的安全与审计页签下开启。

重要

启用RRSA功能后，集群内新创建的ServiceAccount Token的最大有效期将被限制为不能超过12小时。

## 创建集群时开启

创建ACK托管集群和ACK Edge集群时，您可以在集群配置的高级选项（选填）区域，选中开启RRSA功能。

## 在集群信息页面开启

- 

登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。

- 

在集群列表页面，单击目标集群名称，然后在左侧导航栏，选择集群信息。

- 

在基本信息页签的安全与审计区域，单击RRSA OIDC右侧的开启。

- 

在弹出的启用 RRSA对话框，单击确定。

在基本信息区域，当集群状态由更新中变为运行中后，表明该集群的RRSA特性已变更完成。

### 获取集群中OIDC提供商的URL和ARN信息

集群中RRSA功能开启后，在基本信息页签的安全与审计区域，将鼠标悬浮至RRSA OIDC右侧已开启上面，即可查看提供商的URL链接和ARN信息。

集群开启RRSA功能后，ACK将在后台执行如下操作。

- 

自动创建一个集群专用的OIDC Issuer服务。该服务由ACK托管，无需您运维。更多信息，请参见[OIDC Issuer](https://openid.net/specs/openid-connect-discovery-1_0.html)。

- 

修改当前集群的服务账户令牌卷投影功能的配置，使用本次创建的OIDC Issuer配置合并集群已有的service-account-issuer参数的值。更多信息，请参见[使用](products/ack/documents/ack-managed-and-ack-dedicated/security-and-compliance/enable-service-account-token-volume-projection.md)[ServiceAccount Token](products/ack/documents/ack-managed-and-ack-dedicated/security-and-compliance/enable-service-account-token-volume-projection.md)[卷投影](products/ack/documents/ack-managed-and-ack-dedicated/security-and-compliance/enable-service-account-token-volume-projection.md)。

- 

在您的账号下创建一个使用该OIDC Issuer的OIDC身份提供商，名称为ack-rrsa-<cluster_id>，其中<cluster_id>为您的集群ID。更多信息，请参见[管理](products/ram/documents/manage-an-oidc-idp.md)[OIDC](products/ram/documents/manage-an-oidc-idp.md)[身份提供商](products/ram/documents/manage-an-oidc-idp.md)。

## 使用RRSA功能

集群开启RRSA功能后，您可以参考以下内容，赋予集群内应用通过RRSA功能获取访问云资源OpenAPI的临时凭证的能力。

### 使用示例

本示例部署的应用将使用RRSA功能扮演指定角色，获取当前账号下集群列表信息。

示例配置

- 

命名空间：rrsa-demo

- 

ServiceAccount：demo-sa

- 

RAM角色：demo-role-for-rrsa

示例流程

- 

如果您希望通过不安装ack-pod-identity-webhook组件的方式使用RRSA功能，您可以手动修改应用模板挂载应用所需的OIDC Token文件并配置相关环境变量。具体操作，请参见[手动修改应用模板使用](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)[RRSA](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)[功能](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)。

- 

如果您希望使用已存在的RAM角色，不创建新的RAM角色，您可以为已有RAM角色新增相关权限。具体操作，请参见[使用已存在的](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)[RAM](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)[角色并授权](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)。

- 

安装ack-pod-identity-webhook组件。

- 

在集群列表页面，单击目标集群名称，然后在左侧导航栏，选择运维管理 > 组件管理。

- 

在组件管理页面，单击安全页签，找到ack-pod-identity-webhook组件，单击组件右下方的安装。

- 

在提示对话框确认组件信息后，单击确定。

- 

创建一个名为demo-role-for-rrsa的RAM角色。主要参数说明如下，具体操作，请参见[创建](products/ram/documents/user-guide/create-a-ram-role-for-a-trusted-idp.md)[OIDC](products/ram/documents/user-guide/create-a-ram-role-for-a-trusted-idp.md)[身份提供商的](products/ram/documents/user-guide/create-a-ram-role-for-a-trusted-idp.md)[RAM](products/ram/documents/user-guide/create-a-ram-role-for-a-trusted-idp.md)[角色](products/ram/documents/user-guide/create-a-ram-role-for-a-trusted-idp.md)。

- 

- 

- 

- 

- 

- 

| 配置项 | 描述 |
| --- | --- |
| 身份提供商类型 | OIDC 。 |
| 身份提供商 | 选择 ack-rrsa-<cluster_id>。其中，<cluster_id>为您的集群 ID。 |
| 条件 | oidc:iss：保持默认。 oidc:aud：保持默认。 oidc:sub：需手动添加该条件。 条件键：选择 oidc:sub 。 运算符：选择 StringEquals 。 条件值：输入 system:serviceaccount:<namespace>:<serviceAccountName> 。其中， <namespace> 为应用所在的命名空间。 <serviceAccountName> 为服务账户名称。根据本文测试应用的信息，此处需填入 system:serviceaccount:rrsa-demo:demo-sa 。 |
| 角色名称 | demo-role-for-rrsa。 |


- 

为[步骤](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)[2](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)创建的角色授予测试应用所需的AliyunCSReadOnlyAccess系统策略权限。具体操作，请参见[管理](products/ram/documents/user-guide/grant-permissions-to-a-ram-role.md)[RAM](products/ram/documents/user-guide/grant-permissions-to-a-ram-role.md)[角色的权限](products/ram/documents/user-guide/grant-permissions-to-a-ram-role.md)。

- 

部署测试应用。关于测试应用的参考代码，请参见[阿里云官方](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)[SDK](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)[使用](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)[RRSA OIDC Token](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)[的参考代码](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)。

- 

使用以下内容，创建demo.yaml文件。

如下YAML示例中，为命名空间增加标签pod-identity.alibabacloud.com/injection: 'on'，并为服务账户增加注解pod-identity.alibabacloud.com/role-name: demo-role-for-rrsa，启用ack-pod-identity-webhook组件的配置自动注入功能。关于ack-pod-identity-webhook组件配置的更多说明，请参见[ack-pod-identity-webhook](products/ack/documents/product-overview/ack-pod-identity-webhook.md)。

展开查看示例代码

--- apiVersion: v1 kind: Namespace metadata: name: rrsa-demo labels: pod-identity.alibabacloud.com/injection: 'on' --- apiVersion: v1 kind: ServiceAccount metadata: name: demo-sa namespace: rrsa-demo annotations: pod-identity.alibabacloud.com/role-name: demo-role-for-rrsa --- apiVersion: v1 kind: Pod metadata: name: demo namespace: rrsa-demo spec: serviceAccountName: demo-sa containers: - image: registry.cn-hangzhou.aliyuncs.com/acs/ack-ram-tool:1.3.0 args: - rrsa - demo name: demo restartPolicy: OnFailure

- 

执行以下命令，部署测试应用。

kubectl apply -f demo.yaml

- 

执行以下命令，查看测试应用Pod，确认ack-pod-identity-webhook组件已为Pod自动注入所需的配置。

kubectl -n rrsa-demo get pod demo -o yaml

展开查看预期输出

apiVersion: v1 kind: Pod metadata: name: demo namespace: rrsa-demo spec: containers: - args: - rrsa - demo env: - name: ALIBABA_CLOUD_ROLE_ARN value: acs:ram::1***:role/demo-role-for-rrsa - name: ALIBABA_CLOUD_OIDC_PROVIDER_ARN value: acs:ram::1***:oidc-provider/ack-rrsa-c*** - name: ALIBABA_CLOUD_OIDC_TOKEN_FILE value: /var/run/secrets/ack.alibabacloud.com/rrsa-tokens/token - name: ALIBABA_CLOUD_STS_ENDPOINT value: sts-vpc.cn-hangzhou.aliyuncs.com - name: ALIBABA_CLOUD_STS_REGION value: cn-hangzhou - name: ALIBABA_CLOUD_VPC_ENDPOINT_ENABLED value: "true" image: registry.cn-hangzhou.aliyuncs.com/acs/ack-ram-tool:1.3.0 name: demo volumeMounts: - mountPath: /var/run/secrets/kubernetes.io/serviceaccount name: kube-api-access-4bwdg readOnly: true - mountPath: /var/run/secrets/ack.alibabacloud.com/rrsa-tokens name: rrsa-oidc-token readOnly: true restartPolicy: OnFailure serviceAccount: demo-sa serviceAccountName: demo-sa volumes: - name: kube-api-access-4bwdg projected: defaultMode: 420 sources: - serviceAccountToken: expirationSeconds: 3607 path: token - configMap: items: - key: ca.crt path: ca.crt name: kube-root-ca.crt - downwardAPI: items: - fieldRef: apiVersion: v1 fieldPath: metadata.namespace path: namespace - name: rrsa-oidc-token projected: defaultMode: 420 sources: - serviceAccountToken: audience: sts.aliyuncs.com expirationSeconds: 3600 path: token

预期输出表明，ack-pod-identity-webhook组件已为Pod自动注入了如下配置。

| 类别 | 配置项名称 | 配置项说明 |
| --- | --- | --- |
| 环境变量 | ALIBABA_CLOUD_ROLE_ARN | 需要扮演的 RAM 角色 ARN。 |
| ALIBABA_CLOUD_OIDC_PROVIDER_ARN | OIDC 身份提供商的 ARN。 |  |
| ALIBABA_CLOUD_STS_ENDPOINT | 当前地域的 STS VPC 内网域名。 |  |
| ALIBABA_CLOUD_STS_REGION | 当前地域的 STS 域名地域信息配置。 |  |
| ALIBABA_CLOUD_VPC_ENDPOINT_ENABLED | 是否使用 VPC 内网域名访问 STS 的配置。 |  |
| ALIBABA_CLOUD_OIDC_TOKEN_FILE | 包含 OIDC Token 的文件路径。 |  |
| VolumeMount | rrsa-oidc-token | 挂载 OIDC Token 的配置。 |
| Volume | rrsa-oidc-token | 挂载 OIDC Token 的配置。 |


- 

执行以下命令，查看测试应用日志。

kubectl -n rrsa-demo logs demo

预期输出集群列表信息：

cluster id: cf***, cluster name: foo* cluster id: c8***, cluster name: bar* cluster id: c4***, cluster name: foob*

- 

可选：移除角色被授予的AliyunCSReadOnlyAccess系统策略权限。具体操作，请参见[为](products/ram/documents/remove-permissions-from-a-ram-role.md)[RAM](products/ram/documents/remove-permissions-from-a-ram-role.md)[角色移除权限](products/ram/documents/remove-permissions-from-a-ram-role.md)。

等待30秒左右，执行以下命令，再次查看测试应用日志。

kubectl -n rrsa-demo logs demo

预期输出无权限的错误日志：

StatusCode: 403 Code: StatusForbidden Message: code: 403, STSToken policy Forbidden for action cs:DescribeClustersForRegion request id: E78A2E2D-*** Data: {"accessDeniedDetail":{"AuthAction":"cs:DescribeClustersForRegion","AuthPrincipalDisplayName":"demo-role-for-rrsa:ack-ram-tool","AuthPrincipalOwnerId":"11***","AuthPrincipalType":"AssumedRoleUser","NoPermissionType":"ImplicitDeny","PolicyType":"ResourceGroupLevelIdentityBasedPolicy"},"code":"StatusForbidden","message":"STSToken policy Forbidden for action cs:DescribeClustersForRegion","requestId":"E78A2E2D-***","status":403,"statusCode":403}

### 手动修改应用模板使用RRSA功能

您可以通过手动修改应用模板挂载应用所需的OIDC Token文件以及配置相关环境变量，在不安装ack-pod-identity-webhook组件的情况下使用RRSA功能。

应用模板示例代码如下。

展开查看应用模板示例代码

apiVersion: v1 kind: Pod metadata: name: demo namespace: rrsa-demo spec: containers: - args: - rrsa - demo env: - name: ALIBABA_CLOUD_ROLE_ARN value: <role_arn> - name: ALIBABA_CLOUD_OIDC_PROVIDER_ARN value: <oid_provider_arn> - name: ALIBABA_CLOUD_OIDC_TOKEN_FILE value: /var/run/secrets/ack.alibabacloud.com/rrsa-tokens/token image: registry.cn-hangzhou.aliyuncs.com/acs/ack-ram-tool:1.3.0 imagePullPolicy: Always name: demo volumeMounts: - mountPath: /var/run/secrets/ack.alibabacloud.com/rrsa-tokens name: rrsa-oidc-token readOnly: true restartPolicy: OnFailure serviceAccount: demo-sa serviceAccountName: demo-sa volumes: - name: rrsa-oidc-token projected: defaultMode: 420 sources: - serviceAccountToken: audience: sts.aliyuncs.com expirationSeconds: 3600 path: token

重要

请替换应用模板示例代码中的如下字段。

- 

<oid_provider_arn>：替换为当前集群的OIDC提供商ARN。该ARN获取请参见[获取集群中](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)[OIDC](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)[提供商的](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)[URL](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)[和](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)[ARN](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)[信息](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)。

- 

<role_arn>需要替换为当前应用使用的RAM角色ARN。该ARN可在[RAM](https://ram.console.aliyun.com/)[控制台](https://ram.console.aliyun.com/)角色页面的角色详情页面获取。

- 

audience：字段值必须为sts.aliyuncs.com。该字段值对应的是开启RRSA功能时自动创建的OIDC身份提供商中配置的客户端ID，与SDK访问STS的AssumeRoleWithOIDC接口时使用的域名无关，您可以在使用SDK时指定使用合适的STS域名。

- 

expirationSeconds：单位为秒，取值范围为[600, 43200]，即10分钟~12小时。如果设置的值大于43200（12小时），实际的OIDC Token的过期时间仍为12小时。

部署修改后的应用模板后，应用内程序可以使用容器内挂载的OIDC Token（环境变量ALIBABA_CLOUD_OIDC_TOKEN_FILE指向的文件内容，每次使用时都需要从文件中读取最新的Token）、角色的ARN（环境变量ALIBABA_CLOUD_ROLE_ARN配置的值）以及OIDC身份提供商的ARN（环境变量ALIBABA_CLOUD_OIDC_PROVIDER_ARN配置的值），调用STS的AssumeRoleWithOIDC接口，获取一个扮演指定RAM角色的临时凭证，然后使用该临时凭证访问云资源OpenAPI。应用参考代码，请参见[阿里云官方](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)[SDK](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)[使用](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)[RRSA OIDC Token](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)[的参考代码](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)。更多信息，请参见[AssumeRoleWithOIDC](products/ram/documents/api-assumerolewithoidc.md)。

### 使用已存在的RAM角色并授权

如果您的应用需要使用已存在的RAM角色，而非创建新的单独RAM角色，您可以修改RAM角色的信任策略，新增一条允许使用指定的服务账户的应用有权限通过扮演此RAM角色获取临时凭证的信任策略。更多信息，请参见[修改](products/ram/documents/user-guide/edit-the-trust-policy-of-a-ram-role.md)[RAM](products/ram/documents/user-guide/edit-the-trust-policy-of-a-ram-role.md)[角色的信任策略](products/ram/documents/user-guide/edit-the-trust-policy-of-a-ram-role.md)。

RAM角色信任策略中新增的Statement条目内容示例如下。

{ "Action": "sts:AssumeRole", "Condition": { "StringEquals": { "oidc:aud": "sts.aliyuncs.com", "oidc:iss": "<oidc_issuer_url>", "oidc:sub": "system:serviceaccount:<namespace>:<service_account>" } }, "Effect": "Allow", "Principal": { "Federated": [ "<oidc_provider_arn>" ] } }

重要

请替换Statement条目内容示例中的如下字段。

- 

<oidc_issuer_url>：替换为当前集群的OIDC提供商URL。该URL获取请参见[获取集群中](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)[OIDC](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)[提供商的](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)[URL](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)[和](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)[ARN](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)[信息](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)。

- 

<oidc_provider_arn>：替换为当前集群的OIDC提供商ARN。该ARN获取请参见[获取集群中](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)[OIDC](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)[提供商的](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)[URL](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)[和](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)[ARN](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)[信息](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)。

- 

<namespace>：替换为应用所在的命名空间。

- 

<service_account>：替换为应用使用的服务账户。

您也可以使用命令行工具ack-ram-tool通过自动化的方式配置该策略。对应的命令行示例如下。

ack-ram-tool rrsa associate-role --cluster-id <cluster_id> \ --namespace <namespace> --service-account <service_account> \ --role-name <role_name> --create-role-if-not-exist

## 阿里云官方SDK使用RRSA OIDC Token的参考代码

### SDK参考代码

目前，[阿里云](https://help.aliyun.com/zh/sdk/product-overview/differences-between-v1-and-v2-sdks)[V2.0 SDK](https://help.aliyun.com/zh/sdk/product-overview/differences-between-v1-and-v2-sdks)已经内置了支持使用RRSA OIDC Token进行OpenAPI认证的功能，所有基于V2.0 SDK生成并且支持STS Token认证的云产品SDK都将默认支持RRSA OIDC Token认证。支持此功能的SDK版本信息和参考代码如下。

| 编程语言 | 支持认证的 SDK 版本 | 使用示例 |
| --- | --- | --- |
| Go | [Alibaba Cloud Credentials for Go](https://github.com/aliyun/credentials-go) 1.2.6 及以上版本。更多信息，请参考 [方式六：使用](https://help.aliyun.com/zh/sdk/developer-reference/v2-manage-go-access-credentials#ec8021b053aqe) [OIDCRoleArn](https://help.aliyun.com/zh/sdk/developer-reference/v2-manage-go-access-credentials#ec8021b053aqe) 。 | [Go SDK](https://github.com/AliyunContainerService/ack-ram-tool/tree/main/examples/rrsa/go-sdk) [使用示例](https://github.com/AliyunContainerService/ack-ram-tool/tree/main/examples/rrsa/go-sdk) |
| Java | [Alibaba Cloud Credentials for Java](https://github.com/aliyun/credentials-java) 0.2.10 及以上版本。更多信息，请参考 [方式六：OIDCRoleArn](https://help.aliyun.com/zh/sdk/developer-reference/v2-manage-access-credentials#ec8021b053aqe) 。 | [Java SDK](https://github.com/AliyunContainerService/ack-ram-tool/tree/main/examples/rrsa/java-sdk) [使用示例](https://github.com/AliyunContainerService/ack-ram-tool/tree/main/examples/rrsa/java-sdk) |
| Python 3 | [Alibaba Cloud Credentials for Python](https://github.com/aliyun/credentials-python) 0.3.1 及以上版本。更多信息，请参考 [方式六：OIDCRoleArn](https://help.aliyun.com/zh/sdk/developer-reference/v2-manage-python-access-credentials#ec8021b053aqe) 。 | [Python 3 SDK](https://github.com/AliyunContainerService/ack-ram-tool/tree/main/examples/rrsa/python3-sdk) [使用示例](https://github.com/AliyunContainerService/ack-ram-tool/tree/main/examples/rrsa/python3-sdk) |
| Node.js 和 TypeScript | [Alibaba Cloud Credentials for TypeScript/Node.js](https://github.com/aliyun/credentials-nodejs) 2.2.6 及以上版本。更多信息，请参考 [方式六：使用](https://help.aliyun.com/zh/sdk/developer-reference/v2-manage-node-js-access-credentials#ec8021b053aqe) [OIDCRoleArn](https://help.aliyun.com/zh/sdk/developer-reference/v2-manage-node-js-access-credentials#ec8021b053aqe) 。 | [Node.js](https://github.com/AliyunContainerService/ack-ram-tool/tree/main/examples/rrsa/nodejs-sdk) [和](https://github.com/AliyunContainerService/ack-ram-tool/tree/main/examples/rrsa/nodejs-sdk) [TypeScript](https://github.com/AliyunContainerService/ack-ram-tool/tree/main/examples/rrsa/nodejs-sdk) [使用示例](https://github.com/AliyunContainerService/ack-ram-tool/tree/main/examples/rrsa/nodejs-sdk) |


部分云产品自研的SDK也可以参考上面的方法实现使用RRSA OIDC Token进行OpenAPI认证的功能。具体实现方式的参考代码如下。

| 云产品 | SDK | 使用示例 |
| --- | --- | --- |
| 对象存储 | [OSS GO SDK](products/oss/documents/developer-reference/go.md) 更多信息，请参考 [方式五：使用](products/oss/documents/go-configure-access-credentials.md) [OIDCRoleARN](products/oss/documents/go-configure-access-credentials.md) 。 | [Go SDK](https://github.com/AliyunContainerService/ack-ram-tool/tree/main/examples/rrsa/oss-go-sdk) [使用示例](https://github.com/AliyunContainerService/ack-ram-tool/tree/main/examples/rrsa/oss-go-sdk) |
| [OSS Java SDK](products/oss/documents/developer-reference/java.md) 更多信息，请参考 [使用](products/oss/documents/developer-reference/oss-java-sdk.md) [OIDCRoleARN](products/oss/documents/developer-reference/oss-java-sdk.md) 。 | [Java SDK](https://github.com/AliyunContainerService/ack-ram-tool/tree/main/examples/rrsa/oss-java-sdk) [使用示例](https://github.com/AliyunContainerService/ack-ram-tool/tree/main/examples/rrsa/oss-java-sdk) |  |
| [OSS Python SDK](products/oss/documents/developer-reference/python.md) 更多信息，请参考 [使用](products/oss/documents/python-configuration-access-credentials.md) [OIDCRoleARN](products/oss/documents/python-configuration-access-credentials.md) 。 | [Python SDK](https://github.com/AliyunContainerService/ack-ram-tool/tree/main/examples/rrsa/oss-python3-sdk) [使用示例](https://github.com/AliyunContainerService/ack-ram-tool/tree/main/examples/rrsa/oss-python3-sdk) |  |
| 日志服务 | [日志服务](products/sls/documents/developer-reference/sdk-for-java.md) [Java SDK](products/sls/documents/developer-reference/sdk-for-java.md) 更多信息，请参考 [Java SDK](products/sls/documents/developer-reference/get-started-with-log-service-sdk-for-java.md) [快速入门](products/sls/documents/developer-reference/get-started-with-log-service-sdk-for-java.md) 。 | [Java SDK](https://github.com/AliyunContainerService/ack-ram-tool/tree/main/examples/rrsa/log-java-sdk) [使用示例](https://github.com/AliyunContainerService/ack-ram-tool/tree/main/examples/rrsa/log-java-sdk) |


### SDK报错信息解决方法

不同报错信息的解决方法如下表所示。

| 报错信息 | 原因 | 解决方法 |
| --- | --- | --- |
| { "Code": "AuthenticationFail.OIDCToken.Expired", "Message": "This JsonWebToken is expired." } | 您的应用使用的 OIDC Token 已过期。 | 您需要每次都从环境变量 ALIBABA_CLOUD_OIDC_TOKEN_FILE 指向的文件中读取最新的 OIDC Token。建议您使用阿里云官方 SDK 而不是自行实现获取临时凭证的逻辑。更多信息，请参见 [阿里云官方](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md) [SDK](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md) [使用](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md) [RRSA OIDC Token](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md) [的参考代码](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md) 。 |
| { "Code": "Throttling.User", "Message": "Request was denied due to user flow control." } | 您的应用获取临时凭证的操作太频繁，导致操作被限流。 | 请勿过于频繁调用获取临时凭证的接口，在临时凭证过期前您无需频繁获取新的凭证。建议您使用阿里云官方 SDK 而不是自行实现获取临时凭证的逻辑。更多信息，请参见 [阿里云官方](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md) [SDK](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md) [使用](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md) [RRSA OIDC Token](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md) [的参考代码](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md) 。 |
| { "Code": "AuthenticationFail.OIDCToken.AudienceNotMatch", "Message": "Invalid audience." } | 您的应用模板中 audience 配置项的值不是 sts.aliyuncs.com 。 | 您需要修改应用模板，确保配置项 audience 的值是预期的 sts.aliyuncs.com 。 |
| { "Code": "AuthenticationFail.OIDCToken.IssuerConfigurationBroken", "Message": "Get public keys from OIDC Provider failed, the issuer is https://kubernetes.default.svc." } { "Code": "AuthenticationFail.OIDCToken.IssuerNotMatch", "Message": "The issuer in the OIDC Token doesn't match the OIDC Provider registered." } { "Code": "AuthenticationFail.NoPermission", "Message": "No such OIDC Provider registered." } | 您的集群未启用 RRSA 功能。 | 您需要为应用所在集群启用 RRSA 功能。操作方法，请参见 [启用](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md) [RRSA](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md) [功能](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md) 。完成启用 RRSA 功能操作后，您还需要重建使用 RRSA 功能的应用 Pod。 |
| { "Code": "EntityNotExist.Role", "Message": "The role not exists: acs:ram::19981***:role/***. " } | 您的应用所使用的 RAM 角色不存在。 | 您需要创建对应的 RAM 角色。操作方法，请参见 [创建](products/ram/documents/user-guide/create-a-ram-role-for-a-trusted-idp.md) [OIDC](products/ram/documents/user-guide/create-a-ram-role-for-a-trusted-idp.md) [身份提供商的](products/ram/documents/user-guide/create-a-ram-role-for-a-trusted-idp.md) [RAM](products/ram/documents/user-guide/create-a-ram-role-for-a-trusted-idp.md) [角色](products/ram/documents/user-guide/create-a-ram-role-for-a-trusted-idp.md) 以及 [使用示例](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md) 。 |
| { "Code": "AuthenticationFail.NoPermission", "Message": "There is no permission" } | 您的应用所使用的 RAM 角色未完成所需的信任策略配置。 | 您需要修改 RAM 角色的信任策略，允许您的应用扮演该角色。操作方法，请参见 [使用已存在的](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md) [RAM](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md) [角色并授权](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md) 。 |


## 常用命令行工具使用RRSA OIDC Token

借助[ack-ram-tool](https://github.com/AliyunContainerService/ack-ram-tool/releases)，可以赋予部分常用命令行工具（阿里云CLI、对象存储ossutil 2.0、Terraform等）在容器内使用RRSA OIDC Token的能力。具体配置和使用示例详见下表。

展开查看配置和使用示例

- 

- 

- 

- 

- 

- 

| 命令行工具 | 配置方法 | 使用示例 |
| --- | --- | --- |
| [阿里云](https://help.aliyun.com/zh/cli/what-is-alibaba-cloud-cli) [CLI](https://help.aliyun.com/zh/cli/what-is-alibaba-cloud-cli) | 您可以在配置文件 ~/.aliyun/config.json 中将 mode 配置项的值设置为 OIDC 的方式使用 RRSA OIDC Token。更多信息，请参考 [身份凭证类型](https://help.aliyun.com/zh/cli/configure-credentials/#41e7063556zzq) 。 说明 仅 v3.0.206 及以上版本的阿里云 CLI 支持该特性。 需要将配置文件中 region_id 的值替换为您期望的地域。 { "current": "rrsa", "profiles": [ { "name": "rrsa", "mode": "OIDC", "region_id": "cn-hangzhou", "ram_session_name": "test-rrsa" } ], "meta_path": "" } | $ aliyun sts GetCallerIdentity { "AccountId": "11380***", "Arn": "acs:ram::1138***:assumed-role/test-rrsa-***/test-rrsa", "IdentityType": "AssumedRoleUser", "PrincipalId": "33300***:test-rrsa", "RequestId": "20F78881-F47E-5771-90D6-***", "RoleId": "33300***" } |
| 您也可以不创建配置文件，直接执行阿里云 CLI 相关命令。 说明 仅 v3.0.206 及以上版本的阿里云 CLI 支持该特性。 | $ aliyun sts GetCallerIdentity --region cn-hangzhou --role-session-name=test-rrsa { "AccountId": "11380***", "Arn": "acs:ram::1138***:assumed-role/test-rrsa-***/test-rrsa", "IdentityType": "AssumedRoleUser", "PrincipalId": "33300***:test-rrsa", "RequestId": "20F78881-F47E-5771-90D6-***", "RoleId": "33300***" } |  |
| [对象存储](products/oss/documents/developer-reference/ossutil-overview.md) [ossutil 2.0](products/oss/documents/developer-reference/ossutil-overview.md) | 您可以在配置文件 ~/.ossutilconfig 中将 mode 配置项的值设置为 oidcRoleArn 的方式使用 RRSA OIDC Token。更多信息，请参考 [配置示例](products/oss/documents/configure-ossutil2.md) 。 说明 仅 V2.1.0 及以上版本的 ossutil 2.0 支持该特性。 需要将配置文件中 region 的值替换为您期望的地域。 cat <<EOF > ~/.ossutilconfig [default] mode = oidcRoleArn OIDCProviderArn = "${ALIBABA_CLOUD_OIDC_PROVIDER_ARN}" OIDCTokenFilePath = "${ALIBABA_CLOUD_OIDC_TOKEN_FILE}" roleArn = "${ALIBABA_CLOUD_ROLE_ARN}" roleSessionName = test-rrsa region = cn-hangzhou EOF | $ ossutil api describe-regions <RegionInfoList> <RegionInfo> <Region>oss-us-west-1</Region> <InternetEndpoint>oss-us-west-1.aliyuncs.com</InternetEndpoint> <InternalEndpoint>oss-us-west-1-internal.aliyuncs.com</InternalEndpoint> <AccelerateEndpoint>oss-accelerate.aliyuncs.com</AccelerateEndpoint> </RegionInfo> ... </RegionInfoList> |
| [日志服务](products/sls/documents/developer-reference/overview-of-log-service-cli.md) [CLI](products/sls/documents/developer-reference/overview-of-log-service-cli.md) | 暂不支持在日志服务 CLI 的配置文件中指定使用 RRSA OIDC Token，您需要使用命令 ack-ram-tool export-credentials -f environment-variables -- aliyunlog 执行日志服务 CLI 相关命令。 | $ ack-ram-tool export-credentials -f environment-variables -- aliyunlog log list_project --region-endpoint=cn-hangzhou.log.aliyuncs.com {"count": 1, "projects": [ {"createTime": "1676282996", "description": "k8s log project, ***", "lastModifyTime": "1676282996", "owner": "", "projectName": "k8s-log-c0edc***", "region": "cn-hangzhou", "resourceGroupId": "rg-***", "status": "Normal"}], "total": 24} |
| [Terraform](products/ack/documents/ack-managed-and-ack-dedicated/developer-reference/terraform-overview.md) | 您可以在配置文件中通过配置 assume_role_with_oidc 配置项的方式使用 RRSA OIDC Token。 说明 仅 v1.222.0 及以上版本的 [阿里云](https://www.terraform.io/docs/providers/alicloud/index.html) [Provider](https://www.terraform.io/docs/providers/alicloud/index.html) 支持该配置项。 需要将配置文件中 region 的值替换为您期望的地域。 provider "alicloud" { assume_role_with_oidc { role_session_name = "terraform-with-rrsa-auth-example" } region = "cn-hangzhou" } | [Terraform](https://github.com/AliyunContainerService/ack-ram-tool/tree/main/examples/rrsa/terraform-demo/rrsa-auth) [使用示例](https://github.com/AliyunContainerService/ack-ram-tool/tree/main/examples/rrsa/terraform-demo/rrsa-auth) |


## 相关文档

- 

[ack-pod-identity-webhook](products/ack/documents/product-overview/ack-pod-identity-webhook.md)

- 

[ServiceAccount token volume projection](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/?spm=a2c4g.11186623.0.0.58545bcbDaGKEm#serviceaccount-token-volume-projection)

- 

[OIDC(OpenID Connect) 介绍](https://openid.net/connect/)

- 

[OIDC](products/ram/documents/overview-of-oidc-based-sso.md)[角色](products/ram/documents/overview-of-oidc-based-sso.md)[SSO](products/ram/documents/overview-of-oidc-based-sso.md)[概览](products/ram/documents/overview-of-oidc-based-sso.md)

- 

[AssumeRoleWithOIDC - OIDC](products/ram/documents/developer-reference/api-sts-2015-04-01-assumerolewithoidc.md)[角色](products/ram/documents/developer-reference/api-sts-2015-04-01-assumerolewithoidc.md)[SSO](products/ram/documents/developer-reference/api-sts-2015-04-01-assumerolewithoidc.md)[时获取扮演角色的临时身份凭证](products/ram/documents/developer-reference/api-sts-2015-04-01-assumerolewithoidc.md)

- 

[ack-ram-tool](https://github.com/AliyunContainerService/ack-ram-tool?spm=a2c4g.11186623.0.0.58545bcbDaGKEm)

[上一篇：使用自定义Worker RAM角色](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-custom-worker-ram-roles.md)[下一篇：手动收敛ACK托管版集群的Worker RAM角色权限](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/manually-converges-the-worker-ram-role-permissions-of-the-ack-managed-version-cluster.md)

该文章对您有帮助吗？

反馈

### 为什么选择阿里云

[什么是云计算](https://www.aliyun.com/about/what-is-cloud-computing)[全球基础设施](https://infrastructure.aliyun.com/)[技术领先](https://www.aliyun.com/why-us/leading-technology)[稳定可靠](https://www.aliyun.com/why-us/reliability)[安全合规](https://www.aliyun.com/why-us/security-compliance)[分析师报告](https://www.aliyun.com/analyst-reports)

### 大模型

[千问大模型](https://www.aliyun.com/product/tongyi)[大模型服务](https://bailian.console.aliyun.com/?tab=model#/model-market)[AI应用构建](https://bailian.console.aliyun.com/app-center?tab=app#/app-center)

### 产品和定价

[全部产品](https://www.aliyun.com/product/list)[免费试用](https://free.aliyun.com/)[产品动态](https://www.aliyun.com/product/news/)[产品定价](https://www.aliyun.com/price/detail)[配置报价器](https://www.aliyun.com/price/cpq/list)[云上成本管理](https://www.aliyun.com/price/cost-management)

### 技术内容

[技术解决方案](https://www.aliyun.com/solution/tech-solution)[帮助文档](https://help.aliyun.com/)[开发者社区](https://developer.aliyun.com/)[天池大赛](https://tianchi.aliyun.com/)[阿里云认证](https://edu.aliyun.com/)

### 权益

[免费试用](https://free.aliyun.com/)[解决方案免费试用](https://www.aliyun.com/solution/free)[高校计划](https://university.aliyun.com/)[5亿算力补贴](https://www.aliyun.com/benefit/form/index)[推荐返现计划](https://dashi.aliyun.com/?ambRef=shouYeDaoHang2&pageCode=yunparterIndex)

### 服务

[基础服务](https://www.aliyun.com/service)[企业增值服务](https://www.aliyun.com/service/supportplans)[迁云服务](https://www.aliyun.com/service/devopsimpl/devopsimpl_cloudmigration_public_cn)[官网公告](https://www.aliyun.com/notice/)[健康看板](https://status.aliyun.com/)[信任中心](https://security.aliyun.com/trust-center)

### 关注阿里云

关注阿里云公众号或下载阿里云APP，关注云资讯，随时随地运维管控云服务

联系我们：4008013260

[法律声明](https://help.aliyun.com/product/67275.html)[Cookies 政策](https://terms.alicdn.com/legal-agreement/terms/platform_service/20220906101446934/20220906101446934.html)[廉正举报](https://aliyun.jubao.alibaba.com/)[安全举报](https://report.aliyun.com/)[联系我们](https://www.aliyun.com/contact)[加入我们](https://careers.aliyun.com/)

### 友情链接

[阿里巴巴集团](https://www.alibabagroup.com/cn/global/home)[淘宝网](https://www.taobao.com/)[天猫](https://www.tmall.com/)[全球速卖通](https://www.aliexpress.com/)[阿里巴巴国际交易市场](https://www.alibaba.com/)[1688](https://www.1688.com/)[阿里妈妈](https://www.alimama.com/index.htm)[飞猪](https://www.fliggy.com/)[阿里云计算](https://www.aliyun.com/)[万网](https://wanwang.aliyun.com/)[高德](https://mobile.amap.com/)[UC](https://www.uc.cn/)[友盟](https://www.umeng.com/)[优酷](https://www.youku.com/)[钉钉](https://www.dingtalk.com/)[支付宝](https://www.alipay.com/)[达摩院](https://damo.alibaba.com/)[淘宝海外](https://world.taobao.com/)[阿里云盘](https://www.aliyundrive.com/)[淘宝闪购](https://www.ele.me/)

© 2009-现在 Aliyun.com 版权所有 增值电信业务经营许可证：[浙B2-20080101](http://beian.miit.gov.cn/)域名注册服务机构许可：[浙D3-20210002](https://domain.miit.gov.cn/域名注册服务机构/互联网域名/阿里云计算有限公司 )

[浙公网安备 33010602009975号](http://www.beian.gov.cn/portal/registerSystemInfo)[浙B2-20080101-4](https://beian.miit.gov.cn/)
