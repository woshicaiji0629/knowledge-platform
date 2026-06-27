# 使用ack-secret-manager将KMS服务凭据同步为Kubernetes Secret-容器服务 Kubernetes 版 ACK-阿里云

Source: https://help.aliyun.com/zh/ack/ack-edge/security-and-compliance/use-ack-secret-manager-to-import-alibaba-cloud-kms-service-credentials

# 使用ack-secret-manager导入阿里云KMS服务凭据
ack-secret-manager支持以Kubernetes Secret实例的形式向集群导入或同步KMS凭据信息，确保集群内的应用能够安全地访问敏感信息。通过该组件，可以实现密钥数据的自动更新，使应用负载通过文件系统挂载指定Secret实例来使用凭据信息，同时帮助解决负载应用和阿里云凭据管家交互的兼容性问题。
## 安全说明
通常情况下，用户的密钥会保存在文件中供应用程序读取，这种情况和通过阿里云KMS凭据管家直接读取密钥存在兼容性问题。ack-secret-manager可以解决此类兼容性问题，同时支持将密钥同步创建为集群中的Kubernetes原生Secrets实例，以供环境变量挂载使用。使用前请评估如下的安全风险。
当密钥在文件系统中可以被访问时，如果应用中存在某些有缺陷的软件，该软件的漏洞可能会造成目录遍历的风险，导致敏感信息泄露。
一些Debug端点或Logs权限的误配置可能导致密钥泄露，所以通过环境变量挂载引用的方式消费密钥是一个不安全且不推荐的做法。
当开启Secret实例同步特性时，需要基于权限最小化原则严格控制访问权限。
鉴于上述原因，如果应用中并不需要密文的持久化存储，推荐[通过](../../ack-managed-and-ack-dedicated/user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)[RRSA](../../ack-managed-and-ack-dedicated/user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)[配置](../../ack-managed-and-ack-dedicated/user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)[ServiceAccount](../../ack-managed-and-ack-dedicated/user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)[的](../../ack-managed-and-ack-dedicated/user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)[RAM](../../ack-managed-and-ack-dedicated/user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)[权限实现](../../ack-managed-and-ack-dedicated/user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)[Pod](../../ack-managed-and-ack-dedicated/user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)[权限隔离](../../ack-managed-and-ack-dedicated/user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)为应用配置Pod维度的最小化权限，并通过[GetSecretValue](../../../../kms/documents/key-management-service/developer-reference/api-getsecretvalue.md)直接在应用中获取密钥凭据，以减少密钥内容在Pod文件系统或Kubernetes集群Secrets中的暴露风险。
## 前提条件
已创建ACK集群。请参见[创建](../../ack-managed-and-ack-dedicated/user-guide/create-an-ack-managed-cluster-2.md)[ACK](../../ack-managed-and-ack-dedicated/user-guide/create-an-ack-managed-cluster-2.md)[托管集群](../../ack-managed-and-ack-dedicated/user-guide/create-an-ack-managed-cluster-2.md)、[创建](../../distributed-cloud-container-platform-for-kubernetes/user-guide/create-ack-one-registered-clusters.md)[ACK One](../../distributed-cloud-container-platform-for-kubernetes/user-guide/create-ack-one-registered-clusters.md)[注册集群](../../distributed-cloud-container-platform-for-kubernetes/user-guide/create-ack-one-registered-clusters.md)、[创建](../../serverless-kubernetes/user-guide/create-an-ask-cluster-2.md)[ACK Serverless](../../serverless-kubernetes/user-guide/create-an-ask-cluster-2.md)[集群](../../serverless-kubernetes/user-guide/create-an-ask-cluster-2.md)。
支持ACK托管集群、ACK专有集群、ACK Serverless集群、ACK Edge集群、和ACK One注册集群。
[已通过](../../ack-managed-and-ack-dedicated/user-guide/obtain-the-kubeconfig-file-of-a-cluster-and-use-kubectl-to-connect-to-the-cluster.md)[kubectl](../../ack-managed-and-ack-dedicated/user-guide/obtain-the-kubeconfig-file-of-a-cluster-and-use-kubectl-to-connect-to-the-cluster.md)[工具连接集群](../../ack-managed-and-ack-dedicated/user-guide/obtain-the-kubeconfig-file-of-a-cluster-and-use-kubectl-to-connect-to-the-cluster.md)。
## 步骤一：安装ack-secret-manager组件
登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。
在集群列表页面，单击目标集群名称，然后在左侧导航栏，选择应用>Helm。
在Helm页面，单击创建，在Chart区域搜索并选中ack-secret-manager，其他设置保持默认，然后单击下一步。
根据弹出的页面提示确认，组件将被安装在默认的kube-system命名空间中，并以组件名称发布应用。如果需要自定义应用名和命名空间，请根据页面提示设置。
在参数配置页面，选择Chart版本为最新版本，并设置相应参数，然后单击确定。
如需开启RRSA认证功能，需要将参数rrsa.enable设置为true。
如需开启定时同步凭据功能，需要配置如下参数。
command.disablePolling：是否关闭凭据的自动轮询功能，设置为false，开启凭据自动轮询功能。
command.pollingInterval：凭据同步的频率，设置为120s，此处以两分钟同步一次凭据为例，可以根据实际需求调整。
配置限流参数：如果集群中具有较多的ExternalSecret（待同步的 KMS 凭据），配置不当可能会引发KMS或RAM侧的限流，因此，需要配置以下限流参数避免发生限流。command.maxConcurrentKmsSecretPulls：每秒可以同步的最大KMS凭据数量，默认为10。
如需指定KMS服务Endpoint地址，需要配置kmsEndpoint参数。
command.kmsEndpoint：参数支持KMS服务的共享网关和专属网关，可按需配置，该参数是全局配置，当前也支持凭据级的配置，具体的配置说明请参见下文[配置](use-ack-secret-manager-to-import-alibaba-cloud-kms-service-credentials.md)[KMS](use-ack-secret-manager-to-import-alibaba-cloud-kms-service-credentials.md)[服务](use-ack-secret-manager-to-import-alibaba-cloud-kms-service-credentials.md)[Endpoint](use-ack-secret-manager-to-import-alibaba-cloud-kms-service-credentials.md)[地址](use-ack-secret-manager-to-import-alibaba-cloud-kms-service-credentials.md)。
创建成功后，会自动跳转到目标集群的ack-secret-manager页面，检查安装结果。若下图中所有资源创建成功，则表明组件安装成功。
## 步骤二：配置组件认证信息
需要通过自定义资源SecretStore来配置ack-secret-manager的认证信息，以确保该组件有权限获取KMS服务中的凭据信息，否则ack-secret-manager将无法向集群中导入或同步凭据信息。可以根据集群类型选择如下三种授权方式进行配置。
[通过](use-ack-secret-manager-to-import-alibaba-cloud-kms-service-credentials.md)[RRSA](use-ack-secret-manager-to-import-alibaba-cloud-kms-service-credentials.md)[授权](use-ack-secret-manager-to-import-alibaba-cloud-kms-service-credentials.md)：适用于1.22及以上版本的ACK托管集群和ACK Serverless集群。
[为集群对应的](use-ack-secret-manager-to-import-alibaba-cloud-kms-service-credentials.md)[Worker RAM](use-ack-secret-manager-to-import-alibaba-cloud-kms-service-credentials.md)[角色添加权限](use-ack-secret-manager-to-import-alibaba-cloud-kms-service-credentials.md)：适用于ACK托管集群、ACK专有集群和ACK One注册集群。
[通过设置](use-ack-secret-manager-to-import-alibaba-cloud-kms-service-credentials.md)[AK](use-ack-secret-manager-to-import-alibaba-cloud-kms-service-credentials.md)[扮演指定](use-ack-secret-manager-to-import-alibaba-cloud-kms-service-credentials.md)[RAM](use-ack-secret-manager-to-import-alibaba-cloud-kms-service-credentials.md)[角色](use-ack-secret-manager-to-import-alibaba-cloud-kms-service-credentials.md)：适用于所有容器服务Kubernetes集群。
### 通过RRSA授权
RRSA适用于1.22及以上版本的ACK托管集群和ACK Serverless集群。相比其他授权方式，RRSA授权方式可以实现Pod维度的权限隔离，还可以避免直接使用AK、SK引起的凭据泄露风险。
在[容器服务管理控制台](https://cs.console.aliyun.com)开启集群的RRSA功能，用于创建集群的身份提供商信息。具体操作，请参见[启用](../../ack-managed-and-ack-dedicated/user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)[RRSA](../../ack-managed-and-ack-dedicated/user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)[功能](../../ack-managed-and-ack-dedicated/user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)。
说明
安装ack-secret-manager时，需要将参数rrsa.enable设置为true，以启用RRSA功能。
创建可信实体为身份提供商的RAM角色，以供ack-secret-manager使用。
选择信任主体类型为身份提供商，添加主体时主要参数设置如下，具体操作，请参见[创建](../../../../ram/documents/user-guide/create-a-ram-role-for-a-trusted-idp.md)[OIDC](../../../../ram/documents/user-guide/create-a-ram-role-for-a-trusted-idp.md)[身份提供商的](../../../../ram/documents/user-guide/create-a-ram-role-for-a-trusted-idp.md)[RAM](../../../../ram/documents/user-guide/create-a-ram-role-for-a-trusted-idp.md)[角色](../../../../ram/documents/user-guide/create-a-ram-role-for-a-trusted-idp.md)。
| 配置项 | 描述 |
| --- | --- |
| 身份提供商类型 | OIDC 。 |
| 身份提供商 | 选择 ack-rrsa-<cluster_id>。其中，<cluster_id>为集群 ID。 |
| 条件 | oidc:iss：保持默认。 oidc:aud：保持默认。 oidc:sub：需手动添加该条件。 条件键：选择 oidc:sub 。 运算符：选择 StringEquals 。 条件值：输入 system:serviceaccount:<namespace>:<serviceAccountName> 。其中， <namespace> 为应用所在的命名空间。 <serviceAccountName> 为服务账户名称。根据本文测试应用的信息，此处需填入 system:serviceaccount:kube-system:ack-secret-manager 。 说明 如果将 ack-secret-manager 安装在其他的命名空间，请将 kube-system 替换为对应命名空间的名称。 |
创建自定义权限策略并为上一步创建的RAM角色授权。
创建ack-secret-manager导入KMS凭据时所需的权限策略。策略内容如下。具体操作，请参见[创建自定义权限策略](../../../../ram/documents/create-a-custom-policy.md)。
{ "Action": [ "kms:GetSecretValue", "kms:Decrypt" ], "Resource": [ "*" ], "Effect": "Allow" }
为上一步创建的RAM角色授权。具体操作，请参见[为](../../../../ram/documents/user-guide/grant-permissions-to-a-ram-role.md)[RAM](../../../../ram/documents/user-guide/grant-permissions-to-a-ram-role.md)[角色授权](../../../../ram/documents/user-guide/grant-permissions-to-a-ram-role.md)。
创建自定义资源SecretStore关联对应的认证方式并部署。
使用以下内容，替换相关字段后，创建secretstore-rrsa.yaml文件。
{accountID}：替换为同步KMS凭据的阿里云账号ID。
{clusterID}：替换为集群ID。
{roleName}：替换为[步骤](use-ack-secret-manager-to-import-alibaba-cloud-kms-service-credentials.md)[2](use-ack-secret-manager-to-import-alibaba-cloud-kms-service-credentials.md)中创建的RAM角色名称。
apiVersion: 'alibabacloud.com/v1alpha1' kind: SecretStore metadata: name: scdemo-rrsa spec: KMS: KMSAuth: oidcProviderARN: "acs:ram::{accountID}:oidc-provider/ack-rrsa-{clusterID}" ramRoleARN: "acs:ram::{accountID}:role/{roleName}"
执行以下命令，部署SecretStore。
kubectl apply -f secretstore-rrsa.yaml
### 为集群对应的Worker RAM角色添加权限
由于ACK Serverless集群没有绑定Worker RAM角色，该方式只适用于ACK托管集群、ACK专有集群和ACK One注册集群。
创建如下自定义权限策略。具体操作，请参见[创建自定义权限策略](../../../../ram/documents/create-a-custom-policy.md)。
{ "Action": [ "kms:GetSecretValue", "kms:Decrypt" ], "Resource": [ "*" ], "Effect": "Allow" }
为集群的Worker RAM角色添加上一步创建的自定义权限。具体操作，请参见[为集群的](../../product-overview/product-changes-permissions-of-the-worker-ram-role-of-ack-managed-clusters-are-revoked.md)[Worker RAM](../../product-overview/product-changes-permissions-of-the-worker-ram-role-of-ack-managed-clusters-are-revoked.md)[角色授权](../../product-overview/product-changes-permissions-of-the-worker-ram-role-of-ack-managed-clusters-are-revoked.md)。
### 通过设置AK扮演指定RAM角色
适用于所有容器服务Kubernetes集群。
创建可信实体为阿里云账号的RAM角色，以供ack-secret-manager组件使用。具体操作，请参见[创建可信实体为阿里云账号的](../../../../ram/documents/user-guide/create-a-ram-role-for-a-trusted-alibaba-cloud-account.md)[RAM](../../../../ram/documents/user-guide/create-a-ram-role-for-a-trusted-alibaba-cloud-account.md)[角色](../../../../ram/documents/user-guide/create-a-ram-role-for-a-trusted-alibaba-cloud-account.md)。
说明
在选择信任主体类型时，请选择当前云账号。
创建自定义权限策略并为上一步已创建的RAM角色授权。
创建访问KMS服务凭据所需的权限策略。策略内容如下。具体操作，请参见[创建自定义权限策略](../../../../ram/documents/create-a-custom-policy.md)。
{ "Action": [ "kms:GetSecretValue", "kms:Decrypt" ], "Resource": [ "*" ], "Effect": "Allow" }
为上一步已创建的RAM角色授权。具体操作，请参见[为](../../../../ram/documents/user-guide/grant-permissions-to-a-ram-role.md)[RAM](../../../../ram/documents/user-guide/grant-permissions-to-a-ram-role.md)[角色授权](../../../../ram/documents/user-guide/grant-permissions-to-a-ram-role.md)。
创建自定义权限策略，并为指定的RAM用户授权。
创建扮演上述角色的自定义权限策略。策略内容如下。具体操作，请参见[创建自定义权限策略](../../../../ram/documents/create-a-custom-policy.md)。
{ "Statement": [ { "Action": "sts:AssumeRole", "Effect": "Allow", "Resource": "acs:ram:*:<account-id>:role/<role-name>" } ], "Version": "1" }
上述自定义策略中的Resource为角色ARN，其中，<account-id>为阿里云账号ID，<role-name>为RAM角色名称。关于如何查看角色ARN，请参见[如何查看](../../../../ram/documents/support/faq-about-ram-roles-and-sts-tokens.md)[RAM](../../../../ram/documents/support/faq-about-ram-roles-and-sts-tokens.md)[角色的](../../../../ram/documents/support/faq-about-ram-roles-and-sts-tokens.md)[ARN？](../../../../ram/documents/support/faq-about-ram-roles-and-sts-tokens.md)。
将上述自定义策略授权给RAM用户，便可以指定具体可以扮演的RAM角色。关于如何为RAM用户授权，请参见[为](../../../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)[RAM](../../../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)[用户授权](../../../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)。
创建Secret用于存放指定RAM用户的AK、SK信息。
使用以下内容，替换您的AK、SK的Base64编码信息后，创建ramuser.yaml文件。
apiVersion: v1 data: accessKey: {AK base64编码} accessKeySecret: {SK base64 编码} kind: Secret metadata: name: ramuser namespace: kube-system type: Opaque
执行以下命令，创建名为ramuser的Secret。
kubectl apply -f ramuser.yaml
创建自定义资源SecretStore关联对应的认证方式并部署。
使用以下内容，替换相关字段后，创建secretstore-ramrole.yaml文件。
{accountID}：替换为同步KMS凭据的阿里云账号ID。
{roleName}：替换为[步骤](use-ack-secret-manager-to-import-alibaba-cloud-kms-service-credentials.md)[1](use-ack-secret-manager-to-import-alibaba-cloud-kms-service-credentials.md)中创建的RAM角色名称。
{secretName}：替换为存储AK、SK的Secret名称。
{secretNamespace}：替换为存储AK、SK的Secret的Namespace。
{secretKey}：替换为存储AK、SK的Secret Key。
{roleSessionName}：替换为角色会话名称（自定义字符串）。
apiVersion: 'alibabacloud.com/v1alpha1' kind: SecretStore metadata: name: scdemo-ramrole spec: KMS: KMSAuth: accessKey: name: {secretName} namespace: {secretNamespace} key: {secretKey} accessKeySecret: name: {secretName} namespace: {secretNamespace} key: {secretKey} ramRoleARN: "acs:ram::{accountID}:role/{roleName}" ramRoleSessionName: {roleSessionName}
执行以下命令，部署SecretStore。
kubectl apply -f secretstore-ramrole.yaml
## 步骤三：配置数据同步信息
认证信息配置完成后，需要通过自定义资源ExternalSecret来配置待访问的KMS凭据信息，从而将KMS凭据导入到Kubernetes Secret。
说明
KMS凭据导入的Kubernetes Secret的命名空间、名称均与ExternalSecret的命名空间、名称一致。
创建自定义资源ExternalSecret并部署。
使用以下内容，替换相关字段后，创建external.yaml文件。
| 参数 | 替换说明 |
| --- | --- |
| {KMS secret name} | 必填，替换为目标 KMS 凭据名称。 |
| {Kubernetes secret key} | 必填，为一系列键值对的集合。KMS 的单条凭据会存放在 Kubernetes Secret Data 的某一条键值对中，需将 {Kubernetes secret key} 替换为目标键值对的键。 |
| {KMS secret version stage} | 选填，替换为 KMS 凭据的版本状态（并非凭据的版本号），例如 ACSCurrent。 RDS 凭据、PolarDB 凭据、Redis/Tair 凭据、RAM 凭据和 ECS 凭据只能获取 ACSPrevious 和 ACSCurrent 对应版本的凭据值。 如需指定 KMS 凭据版本号进行同步，请将以下模板中的 versionStage 字段替换为 versionId ，并填入 KMS 凭据版本号。 RDS 凭据、PolarDB 凭据、Redis/Tair 凭据、RAM 凭据和 ECS 凭据不支持指定 VersionId，设置该参数将被忽略。 关于凭据版本号和版本状态请参考 [凭据的组成](../../../../kms/documents/key-management-service/user-guide/secret-management-overview.md) 中凭据版本的说明 |
| {KMS Service endpoint address} | 选填，如需指定 KMS 服务请求 Endpoint，需将其替换为对应的 Endpoint 的地址。 参数支持 KMS 服务的共享网关和专属网关，可按需配置。 参数是凭据级配置，可以为 KMS 凭据单独配置 Endpoint 地址，同时也支持全局配置，具体的配置说明请参考 [配置](use-ack-secret-manager-to-import-alibaba-cloud-kms-service-credentials.md) [KMS](use-ack-secret-manager-to-import-alibaba-cloud-kms-service-credentials.md) [服务](use-ack-secret-manager-to-import-alibaba-cloud-kms-service-credentials.md) [Endpoint](use-ack-secret-manager-to-import-alibaba-cloud-kms-service-credentials.md) [地址](use-ack-secret-manager-to-import-alibaba-cloud-kms-service-credentials.md) 。 参数设置后，会覆盖全局配置和默认配置，该凭据请求的 Endpoint 地址为该参数值。 |
| {secret store name} | 选填，替换为对应 SecretStore 的名称，表示使用某个认证配置来导入目标 KMS 凭据。 说明 组件通过 Worker RAM 角色授权时，无需配置该参数。 |
| {secret store namespace} | 选填，替换为对应 SecretStore 的 Namespace。 说明 组件通过 Worker RAM 角色授权时，无需配置该参数。 |
apiVersion: 'alibabacloud.com/v1alpha1' kind: ExternalSecret metadata: name: esdemo spec: provider: kms # 需要同步的阿里云服务类型，默认是kms，当同步KMS凭据时，可以不填写该字段或者指定字段值为 kms data: # 无需特殊处理的数据源。 - key: {KMS secret name} name: {Kubernetes secret key} versionStage: {KMS secret version stage} secretStoreRef: # 组件通过Worker RAM授权时，无需配置该参数。 name: {secret store name} namespace: {secret store namespace} - key: {KMS secret name} name: {Kubernetes secret key} versionStage: {KMS secret version stage} kmsEndpoint: {KMS Service endpoint address}
执行以下命令，部署ExternalSecret。
kubectl apply -f external.yaml
执行以下命令，查看集群中是否存在对应的Kubernetes Secret。
kubectl get secret esdemo
查询存在Secret，表明Secret同步成功。
## ack-secret-manager组件更多高级用法
### 跨账号同步凭据
如果KMS实例（账号A中）与集群（账号B中）不在同一个阿里云账号中，可以通过ack-secret-manager组件将KMS凭据跨账号同步到集群中。下文通过RRSA认证机制，使ack-secret-manager组件能够获取跨账号访问KMS实例的权限。集群中的组件通过其OIDC提供商扮演账号A中的角色，从而获得对账号A中KMS实例的访问权限，并将该KMS实例导入到账号B的集群中。
账号A（KMS实例所在阿里云账号）权限配置
创建信任集群所在账号的RAM角色。具体操作，请参见[创建可信实体为阿里云账号的](../../../../ram/documents/user-guide/create-a-ram-role-for-a-trusted-alibaba-cloud-account.md)[RAM](../../../../ram/documents/user-guide/create-a-ram-role-for-a-trusted-alibaba-cloud-account.md)[角色](../../../../ram/documents/user-guide/create-a-ram-role-for-a-trusted-alibaba-cloud-account.md)。
重要
在选择信任主体名称时，选择其他云账号，填入账号B（集群所在的阿里云账号）的账号ID。
创建访问KMS服务凭据所需的权限策略。策略内容如下。具体操作，请参见[创建自定义权限策略](../../../../ram/documents/create-a-custom-policy.md)。
{ "Action": [ "kms:GetSecretValue", "kms:Decrypt" ], "Resource": [ "*" ], "Effect": "Allow" }
为上一步创建的RAM角色授权。具体操作，请参见[为](../../../../ram/documents/user-guide/grant-permissions-to-a-ram-role.md)[RAM](../../../../ram/documents/user-guide/grant-permissions-to-a-ram-role.md)[角色授权](../../../../ram/documents/user-guide/grant-permissions-to-a-ram-role.md)。
账号B（集群所在的阿里云账号）权限配置
在[容器服务管理控制台](https://cs.console.aliyun.com)开启集群的RRSA功能，用于创建集群的身份提供商信息。具体操作，请参见[启用](../../ack-managed-and-ack-dedicated/user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)[RRSA](../../ack-managed-and-ack-dedicated/user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)[功能](../../ack-managed-and-ack-dedicated/user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)。
说明
安装ack-secret-manager时，需要将参数rrsa.enable设置为true，以启用RRSA功能。
创建可信实体为身份提供商的RAM角色，以供ack-secret-manager使用。
选择信任主体类型为身份提供商，添加主体时主要参数设置如下，具体操作，请参见[创建](../../../../ram/documents/user-guide/create-a-ram-role-for-a-trusted-idp.md)[OIDC](../../../../ram/documents/user-guide/create-a-ram-role-for-a-trusted-idp.md)[身份提供商的](../../../../ram/documents/user-guide/create-a-ram-role-for-a-trusted-idp.md)[RAM](../../../../ram/documents/user-guide/create-a-ram-role-for-a-trusted-idp.md)[角色](../../../../ram/documents/user-guide/create-a-ram-role-for-a-trusted-idp.md)。
| 配置项 | 描述 |
| --- | --- |
| 身份提供商类型 | OIDC 。 |
| 身份提供商 | 选择 ack-rrsa-<cluster_id>。其中，<cluster_id>为集群 ID。 |
| 条件 | oidc:iss：保持默认。 oidc:aud：保持默认。 oidc:sub：需手动添加该条件。 条件键：选择 oidc:sub 。 运算符：选择 StringEquals 。 条件值：输入 system:serviceaccount:<namespace>:<serviceAccountName> 。其中， <namespace> 为应用所在的命名空间。 <serviceAccountName> 为服务账户名称。根据本文测试应用的信息，此处需填入 system:serviceaccount:kube-system:ack-secret-manager 。 说明 如果将 ack-secret-manager 安装在其他的命名空间，请将 kube-system 替换为对应命名空间的名称。 |
创建自定义权限策略并为上一步账号B下创建的RAM角色授权。
创建ack-secret-manager导入KMS凭据时所需的权限策略。策略内容如下，具体操作，请参见[创建自定义权限策略](../../../../ram/documents/create-a-custom-policy.md)。
{ "Statement": [ { "Action": "sts:AssumeRole", "Effect": "Allow", "Resource": "acs:ram:*:<account-id>:role/<role-name>" # KMS所在账号A下的RAM角色的ARN。 } ], "Version": "1" }
上述自定义策略中的Resource为角色ARN，其中，<account-id>为KMS实例所在的阿里云账号A的账号ID，<role-name>为账号A中创建的RAM角色名称。关于如何查看角色ARN，请参见[如何查看](../../../../ram/documents/support/faq-about-ram-roles-and-sts-tokens.md)[RAM](../../../../ram/documents/support/faq-about-ram-roles-and-sts-tokens.md)[角色的](../../../../ram/documents/support/faq-about-ram-roles-and-sts-tokens.md)[ARN？](../../../../ram/documents/support/faq-about-ram-roles-and-sts-tokens.md)。
为上一步在账号B下创建的RAM角色授权。具体操作，请参见[为](../../../../ram/documents/user-guide/grant-permissions-to-a-ram-role.md)[RAM](../../../../ram/documents/user-guide/grant-permissions-to-a-ram-role.md)[角色授权](../../../../ram/documents/user-guide/grant-permissions-to-a-ram-role.md)。
创建自定义资源SecretStore并部署。
使用以下内容，替换相关字段后，创建secretstore-ramrole.yaml文件。
{ACK-accountID}：替换为集群所在的阿里云账号B的账号ID。
{clusterID}：替换为集群ID。
{ACK-roleName}：替换为集群所在的阿里云账号B下创建的RAM角色的名称。
{KMS-accountID}：替换为KMS实例所在的阿里云账号A的账号ID。
{KMS-roleName}：替换为KMS实例所在的阿里云账号A下创建的RAM角色的名称。
{roleSessionName}：替换为角色会话名称（自定义字符串）。
apiVersion: 'alibabacloud.com/v1alpha1' kind: SecretStore metadata: name: scdemo-cross-account spec: KMS: KMSAuth: oidcProviderARN: "acs:ram::{ACK-accountID}:oidc-provider/ack-rrsa-{clusterID}" ramRoleARN: "acs:ram::{ACK-accountID}:role/{ACK-roleName}" remoteRamRoleARN: "acs:ram::{KMS-accountID}:role/{KMS-roleName}" remoteRamRoleSessionName: {roleSessionName}
配置数据同步信息。具体操作，请参见[步骤三：配置数据同步信息](use-ack-secret-manager-to-import-alibaba-cloud-kms-service-credentials.md)。
### 凭据解析与Key替换
可以参考以下方式对JSON格式和YAML格式的凭据进行解析。
## JSON格式的凭据解析
JSON中指定的Key解析
如果需要解析一个JSON格式的KMS Secret，并将其中指定的key-value键值对同步到Kubernetes Secret中，可以使用JMESPath字段。以下是一个使用JMESPath字段的样例，例如，如果在KMS凭据管家中有如下JSON格式的Secret。
{"name":"tom","friends":[{"name":"lily"},{"name":"mark"}]}
对应的ExternalSecret样例如下。当使用JMESPath字段时，必须指定以下两个子字段：
path：必选项，基于[JMESPath](https://jmespath.org/specification.html)规范解析JSON中的指定字段。
objectAlias：必选项，用于指定解析出的字段同步Kubernetes Secret中的Key名称。
apiVersion: 'alibabacloud.com/v1alpha1' kind: ExternalSecret metadata: name: es-json-demo spec: provider: kms data: - key: {KMS secret name} versionStage: {KMS secret version stage} secretStoreRef: name: {secret store name} namespace: {secret store namespace} jmesPath: # Parse some fields in json string - path: "name" objectAlias: "myname" - path: "friends[0].name" objectAlias: "friendname"
JSON自解析
如果不知道凭据的具体结构，但还需要将JSON凭据解析后再存储在Secret中，可以定义dataProcess.extract字段采用JSON自解析功能，同时还可以定义dataProcess.replaceRule字段，针对解析后的字段键进行规则替换，以防止不规则的Secret data key导致无法创建Secret。
例如，如果在KMS凭据管家中有如下JSON格式的Secret。
{"/name-invalid":"lily","name-invalid/":[{"name":"mark"}]}
对应的ExternalSecret样例如下。
apiVersion: 'alibabacloud.com/v1alpha1' kind: ExternalSecret metadata: name: extract-secret spec: provider: kms dataProcess: - extract: key: {KMS secret name} versionStage: ACSCurrent # KMS凭据版本。 secretStoreRef: name: {secret store name} namespace: {secret store namespace} replaceRule: # 替换规则。 - source: "^/.*d$" # 替换以“/“开头以”d“结尾的key为tom。 target: "tom" - source: "^n.*/$" # 替换以”n“开头以”/“结尾的key为mark。 target: "mark"
## YAML格式的凭据解析
YAML中指定的Key解析
如果需要解析一个YAML格式的KMS Secret，并将其中指定的key-value键值对同步到Kubernetes Secret中，可以使用JMESPath字段。以下是一个使用JMESPath字段的样例，例如，如果在KMS凭据管家中有如下YAML格式的Secret。
name: tom friends: - name: lily - name: mark
对应的ExternalSecret样例如下。当使用JMESPath字段时，必须指定以下两个子字段：
path：必选项，基于[JMESPath](https://jmespath.org/specification.html)规范解析YAML中的指定字段。
objectAlias：必选项，用于指定解析出的字段同步Kubernetes Secret中的Key名称。
apiVersion: 'alibabacloud.com/v1alpha1' kind: ExternalSecret metadata: name: es-json-demo spec: provider: kms data: - key: {KMS secret name} versionStage: {KMS secret version stage} secretStoreRef: name: {secret store name} namespace: {secret store namespace} jmesPath: # Parse some fields in yaml string - path: "name" objectAlias: "myname" - path: "friends[0].name" objectAlias: "friendname"
YAML自解析
如果不知道凭据的具体结构，但还需要将YAML凭据解析后再存储在Secret中，可以定义dataProcess.extract字段采用YAML自解析功能，同时还可以定义dataProcess.replaceRule字段，针对解析后的字段键进行规则替换，以防止不规则的Secret data key导致无法创建Secret。
例如，如果在KMS凭据管家中有如下YAML格式的Secret。
/name-invalid: lily name-invalid/: - name: mark
对应的ExternalSecret样例如下。
apiVersion: 'alibabacloud.com/v1alpha1' kind: ExternalSecret metadata: name: extract-secret spec: provider: kms dataProcess: - extract: key: {KMS secret name} versionStage: ACSCurrent # KMS凭据版本。 secretStoreRef: name: {secret store name} namespace: {secret store namespace} replaceRule: # 替换规则。 - source: "^/.*d$" # 替换以“/“开头以”d“结尾的key为tom。 target: "tom" - source: "^n.*/$" # 替换以”n“开头以”/“结尾的key为mark。 target: "mark"
### 配置KMS服务Endpoint地址
可以通过专属网关访问或共享网关访问两种方式访问KMS服务获取凭据，请参考以下要求进行Endpoint配置。关于专属网关访问和共享网关访问的更多差异，请参见[共享网关和专属网关的差异](../../../../kms/documents/key-management-service/developer-reference/classic-kms-sdkclassic-kms-sdk.md)。
KMS Endpoint优先级规则
| 类型 | 配置字段 | 用途 | 优先级 | 说明 |
| --- | --- | --- | --- | --- |
| 凭据级配置 | ExternalSecret.spec.data.kmsEndpoint | 为需要导入的每个 KMS 凭据单独指定 Endpoint 地址。 | 最高 | 针对单个凭据优先使用该配置，会覆盖全局配置和默认配置。 |
| 全局配置 | command.kmsEndpoint （启动参数） | 用于所有 KMS 请求。 | 中 | 提供了凭据级配置以外的其他 KMS 凭据使用的 Endpoint 地址 |
| 默认配置 | 无 | 当未明确配置 Endpoint 地址时使用。 | 最低 | 默认使用的 KMS Endpoint 地址 kms-vpc.{region}.aliyuncs.com , 替换 {region} 为 KMS 凭据所在的 Region。 |
apiVersion: "alibabacloud.com/v1alpha1" kind: ExternalSecret metadata: name: esdemo spec: provider: kms data: - key: test-hangzhou # 实际Endpoint 地址：全局配置存在时使用全局配置，否则为默认配置地址：kms-vpc.{region}.aliyuncs.com name: hangzhou-vpc versionId: v1 - key: test-hangzhou # 实际Endpoint 地址：字段 kmsEndpoint 指定的 kms.cn-hangzhou.aliyuncs.com name: hangzhou-public versionId: v1 kmsEndpoint: kms.cn-hangzhou.aliyuncs.com
KMS Endpoint配置地址说明
| 网关类型 | 域名类型 | Endpoint 地址 | 使用说明 |
| --- | --- | --- | --- |
| 专属网关 | KMS 私网域名 | {kms-instance-id}.cryptoservice.kms.aliyuncs.com | 要求 KMS 凭据所属实例和集群在同一 Region 及同一 VPC 中。 替换 {kms-instance-id} 为 KMS 凭据所属实例 ID。 KMS 凭据所属实例版本为 3.0 以上。 |
| 共享网关 | VPC 域名 | kms-vpc.{region}.aliyuncs.com | 要求 KMS 凭据和集群在同一 Region。 替换 {region} 为 KMS 凭据所在的 Region。 应用默认配置，使用此地址时无需配置。 |
| 共享网关 | 公网 | kms.{region}.aliyuncs.com | 替换 {region} 为 KMS 凭据所在的 Region。 集群具有公网访问能力。 |
## 相关文档
为了保护从KMS读取后缓存在ACK集群中的Secret，可以对ACK集群Secret进行一键加密。具体操作，请参见[使用阿里云](../../ack-managed-and-ack-dedicated/security-and-compliance/use-kms-to-encrypt-kubernetes-secrets-2.md)[KMS](../../ack-managed-and-ack-dedicated/security-and-compliance/use-kms-to-encrypt-kubernetes-secrets-2.md)[进行](../../ack-managed-and-ack-dedicated/security-and-compliance/use-kms-to-encrypt-kubernetes-secrets-2.md)[Secret](../../ack-managed-and-ack-dedicated/security-and-compliance/use-kms-to-encrypt-kubernetes-secrets-2.md)[的落盘加密](../../ack-managed-and-ack-dedicated/security-and-compliance/use-kms-to-encrypt-kubernetes-secrets-2.md)。
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
