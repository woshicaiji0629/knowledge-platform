# 使用csi-secrets-store-provider-alibabacloud导入阿里云KMS服务凭据-容器服务 Kubernetes 版 ACK(ACK)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/security-and-compliance/use-csi-secrets-store-provider-alibabacloud-to-import-alibaba-cloud-kms-service-credentials

# 使用csi-secrets-store-provider-alibabacloud导入阿里云KMS服务凭据
csi-secrets-store-provider-alibabacloud支持以Kubernetes Secret实例的形式向集群导入或同步KMS凭据信息，确保集群内的应用能够安全地访问敏感信息；还支持通过CSI Inline的形式将凭据密钥作为文件系统直接挂载到应用程序中，适用于通过文件系统接口（例如读取文件）来获取敏感信息的应用。通过该组件，可实现密钥数据的自动更新，从而降低凭据密文在Secrets实例中暴露的可能，同时解决工作负载和阿里云凭据管家交互的兼容性问题。
## 安全说明
默认情况下，直接从文件系统读取密钥和阿里云KMS凭据管家之间的直接交互可能存在兼容性问题，csi-secrets-store-provider-alibabacloud可以用于解决此类兼容性问题，同时支持将密钥同步创建为集群中的Kubernetes原生Secrets实例，以供环境变量挂载使用。使用前请评估如下的安全风险。
当密钥在文件系统中可以被访问时，如果应用中存在某些有缺陷的软件，该软件的漏洞可能会造成目录遍历的风险，导致敏感信息泄露。
一些Debug端点或Logs权限的误配置可能导致密钥泄露，所以通过环境变量挂载引用的方式消费密钥是一个不安全且不推荐的做法。
当开启Secret实例同步特性时，需要基于权限最小化原则严格控制访问权限。
鉴于上述原因，如果应用中并不需要密文的持久化存储，推荐[通过](../user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)[RRSA](../user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)[配置](../user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)[ServiceAccount](../user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)[的](../user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)[RAM](../user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)[权限实现](../user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)[Pod](../user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)[权限隔离](../user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)为应用配置Pod维度的最小化权限，并通过[GetSecretValue](../../../../kms/documents/key-management-service/developer-reference/api-getsecretvalue.md)直接在应用中获取密钥凭据，以减少密钥内容在Pod文件系统或Kubernetes集群Secrets中的暴露风险。
## 前提条件
已创建符合如下要求的ACK集群。具体操作，请参见[创建](../user-guide/create-an-ack-managed-cluster-2.md)[ACK](../user-guide/create-an-ack-managed-cluster-2.md)[托管集群](../user-guide/create-an-ack-managed-cluster-2.md)、[创建](../../distributed-cloud-container-platform-for-kubernetes/user-guide/create-ack-one-registered-clusters.md)[ACK One](../../distributed-cloud-container-platform-for-kubernetes/user-guide/create-ack-one-registered-clusters.md)[注册集群](../../distributed-cloud-container-platform-for-kubernetes/user-guide/create-ack-one-registered-clusters.md)。
集群为1.20及以上版本。支持ACK托管集群、ACK专有集群、ACK Edge集群和ACK One注册集群，暂不支持ACK Serverless集群。
[已通过](../user-guide/obtain-the-kubeconfig-file-of-a-cluster-and-use-kubectl-to-connect-to-the-cluster.md)[kubectl](../user-guide/obtain-the-kubeconfig-file-of-a-cluster-and-use-kubectl-to-connect-to-the-cluster.md)[工具连接集群](../user-guide/obtain-the-kubeconfig-file-of-a-cluster-and-use-kubectl-to-connect-to-the-cluster.md)。
## 步骤一：配置组件认证信息
需配置csi-secrets-store-provider-alibabacloud的认证信息，以确保该组件有权限获取KMS服务中的凭据信息，否则csi-secrets-store-provider-alibabacloud将无法向集群中导入或同步凭据信息。可根据集群类型选择如下三种授权方式进行配置。
[通过](use-csi-secrets-store-provider-alibabacloud-to-import-alibaba-cloud-kms-service-credentials.md)[RRSA](use-csi-secrets-store-provider-alibabacloud-to-import-alibaba-cloud-kms-service-credentials.md)[授权](use-csi-secrets-store-provider-alibabacloud-to-import-alibaba-cloud-kms-service-credentials.md)：适用于1.22及以上版本的ACK托管集群。
[为集群对应的](use-csi-secrets-store-provider-alibabacloud-to-import-alibaba-cloud-kms-service-credentials.md)[Worker RAM](use-csi-secrets-store-provider-alibabacloud-to-import-alibaba-cloud-kms-service-credentials.md)[角色添加权限](use-csi-secrets-store-provider-alibabacloud-to-import-alibaba-cloud-kms-service-credentials.md)：适用于ACK托管集群、ACK专有集群和ACK One注册集群。
[通过设置](use-csi-secrets-store-provider-alibabacloud-to-import-alibaba-cloud-kms-service-credentials.md)[AK](use-csi-secrets-store-provider-alibabacloud-to-import-alibaba-cloud-kms-service-credentials.md)[扮演指定](use-csi-secrets-store-provider-alibabacloud-to-import-alibaba-cloud-kms-service-credentials.md)[RAM](use-csi-secrets-store-provider-alibabacloud-to-import-alibaba-cloud-kms-service-credentials.md)[角色](use-csi-secrets-store-provider-alibabacloud-to-import-alibaba-cloud-kms-service-credentials.md)：适用于所有容器服务Kubernetes集群。
### 通过RRSA授权
相比其他授权方式，RRSA授权方式可以实现Pod维度的权限隔离，还可以避免直接使用AK、SK引起的凭据泄露风险。
在[容器服务管理控制台](https://cs.console.aliyun.com)开启集群的RRSA功能，用于创建集群的身份提供商信息。具体操作，请参见[启用](../user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)[RRSA](../user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)[功能](../user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)。
创建可信实体为身份提供商的RAM角色，以供csi-secrets-store-provider-alibabacloud使用。主要参数设置如下，具体操作，请参见[创建](../../../../ram/documents/user-guide/create-a-ram-role-for-a-trusted-idp.md)[OIDC](../../../../ram/documents/user-guide/create-a-ram-role-for-a-trusted-idp.md)[身份提供商的](../../../../ram/documents/user-guide/create-a-ram-role-for-a-trusted-idp.md)[RAM](../../../../ram/documents/user-guide/create-a-ram-role-for-a-trusted-idp.md)[角色](../../../../ram/documents/user-guide/create-a-ram-role-for-a-trusted-idp.md)。
| 配置项 | 描述 |
| --- | --- |
| 身份提供商类型 | OIDC 。 |
| 身份提供商 | 选择 ack-rrsa-<cluster_id>。其中，<cluster_id>为集群 ID。 |
| 条件 | oidc:iss：保持默认。 oidc:aud：保持默认。 oidc:sub：需手动添加该条件。 条件键：选择 oidc:sub 。 运算符：选择 StringEquals 。 条件值：填入 system:serviceaccount:<namespace>:<serviceAccountName> ，其中， <namespace> 为应用所在的命名空间。 <serviceAccountName> 为服务账户名称。根据本文测试应用的信息，此处需填入 system:serviceaccount:kube-system:csi-secrets-store-provider-alibabacloud 。 说明 建议将组件安装在默认的 kube-system 命名空间下。如将 csi-secrets-store-provider-alibabacloud 安装在其他的命名空间，请将 kube-system 替换为对应命名空间的名称。 |
创建自定义授权策略并为上一步创建的RAM角色授权。
创建csi-secrets-store-provider-alibabacloud导入KMS凭据时所需的权限策略。策略内容如下。具体操作，请参见[创建自定义权限策略](../../../../ram/documents/create-a-custom-policy.md)。
{ "Action": [ "kms:GetSecretValue", "kms:Decrypt" ], "Resource": [ "*" ], "Effect": "Allow" }
为上一步创建的RAM角色授权。具体操作，请参见[管理](../../../../ram/documents/user-guide/grant-permissions-to-a-ram-role.md)[RAM](../../../../ram/documents/user-guide/grant-permissions-to-a-ram-role.md)[角色的权限](../../../../ram/documents/user-guide/grant-permissions-to-a-ram-role.md)。
在集群中创建名为alibaba-credentials的Secret，配置模板如下，需要替换部分字段。
使用以下内容，替换相关字段后，创建secretstore-rrsa.yaml文件。
{rolearn}：替换为[步骤](use-csi-secrets-store-provider-alibabacloud-to-import-alibaba-cloud-kms-service-credentials.md)[2](use-csi-secrets-store-provider-alibabacloud-to-import-alibaba-cloud-kms-service-credentials.md)创建的RAM角色的ARN（需要Base64编码）。
{oidcproviderarn}：替换为集群开启RRSA后生成的提供商ARN（需要Base64编码）。
apiVersion: v1 data: rolearn: {rolearn} oidcproviderarn: {oidcproviderarn} kind: Secret metadata: name: alibaba-credentials namespace: kube-system type: Opaque
执行以下命令，部署Secret。
kubectl apply -f secretstore-rrsa.yaml
### 为集群对应的Worker RAM角色添加权限
适用于ACK托管集群、ACK专有集群和ACK One注册集群
创建如下自定义权限策略。具体操作，请参见[创建自定义权限策略](../../../../ram/documents/create-a-custom-policy.md)。
{ "Action": [ "kms:GetSecretValue", "kms:Decrypt" ], "Resource": [ "*" ], "Effect": "Allow" }
为集群的WorkerRole添加上一步创建的自定义权限。具体操作，请参见[为集群的](../../product-overview/product-changes-permissions-of-the-worker-ram-role-of-ack-managed-clusters-are-revoked.md)[Worker RAM](../../product-overview/product-changes-permissions-of-the-worker-ram-role-of-ack-managed-clusters-are-revoked.md)[角色授权](../../product-overview/product-changes-permissions-of-the-worker-ram-role-of-ack-managed-clusters-are-revoked.md)。
### 通过设置AK扮演指定RAM角色
适用于所有容器服务Kubernetes集群。
创建可信实体为阿里云账号的RAM角色，以供csi-secrets-store-provider-alibabacloud组件使用。具体操作，请参见[创建可信实体为阿里云账号的](../../../../ram/documents/user-guide/create-a-ram-role-for-a-trusted-alibaba-cloud-account.md)[RAM](../../../../ram/documents/user-guide/create-a-ram-role-for-a-trusted-alibaba-cloud-account.md)[角色](../../../../ram/documents/user-guide/create-a-ram-role-for-a-trusted-alibaba-cloud-account.md)。
说明
在选择信任主体名称时，请选择当前云账号。
创建自定义授权策略并为上一步已创建的RAM角色授权。
创建访问KMS服务凭据所需的权限策略。策略内容如下。具体操作，请参见[创建自定义权限策略](../../../../ram/documents/create-a-custom-policy.md)。
{ "Action": [ "kms:GetSecretValue", "kms:Decrypt" ], "Resource": [ "*" ], "Effect": "Allow" }
为上一步已创建的RAM角色授权。具体操作，请参见[管理](../../../../ram/documents/user-guide/grant-permissions-to-a-ram-role.md)[RAM](../../../../ram/documents/user-guide/grant-permissions-to-a-ram-role.md)[角色的权限](../../../../ram/documents/user-guide/grant-permissions-to-a-ram-role.md)。
创建扮演上述角色的自定义授权策略，并为指定的RAM用户授权。
创建扮演上述角色的自定义授权策略。策略内容如下。具体操作，请参见[创建自定义权限策略](../../../../ram/documents/create-a-custom-policy.md)。
{ "Statement": [ { "Action": "sts:AssumeRole", "Effect": "Allow", "Resource": "acs:ram:*:<account-id>:role/<role-name>" } ], "Version": "1" }
上述自定义策略中的Resource为角色ARN，其中，<ACCOUNT_ID>为阿里云账号ID，<ROLE_NAME>为RAM角色名称。关于如何查看角色ARN，请参见[如何查看](../../../../ram/documents/support/faq-about-ram-roles-and-sts-tokens.md)[RAM](../../../../ram/documents/support/faq-about-ram-roles-and-sts-tokens.md)[角色的](../../../../ram/documents/support/faq-about-ram-roles-and-sts-tokens.md)[ARN？](../../../../ram/documents/support/faq-about-ram-roles-and-sts-tokens.md)。
将上述自定义策略授权给RAM用户，便可以指定具体可以扮演的RAM角色。关于如何为RAM用户授权，请参见[管理](../../../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)[RAM](../../../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)[用户的权限](../../../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)。
在集群中创建名为alibaba-credentials的Secret，配置模板如下，需要替换部分字段。
使用以下内容，替换相关字段后，创建alibaba-credentials.yaml文件。
{rolearn}：替换为[步骤](use-csi-secrets-store-provider-alibabacloud-to-import-alibaba-cloud-kms-service-credentials.md)[1](use-csi-secrets-store-provider-alibabacloud-to-import-alibaba-cloud-kms-service-credentials.md)已创建的RAM角色的ARN（需要Base64编码）。
{ak}：替换为RAM用户的AK（需要Base64编码）。
{sk}：替换为RAM用户的SK（需要Base64编码）。
apiVersion: v1 data: id: {ak} secret: {sk} rolearn: {rolearn} kind: Secret metadata: name: alibaba-credentials namespace: kube-system type: Opaque
执行以下命令，部署Secret。
kubectl apply -f alibaba-credentials.yaml
## 步骤二：安装csi-secrets-store-provider-alibabacloud组件
登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。
在集群列表页面，单击目标集群名称，然后在左侧导航栏，选择应用>Helm。
在Helm页面，单击创建，在Chart区域搜索并选中csi-secrets-store-provider-alibabacloud，其他设置保持默认，然后单击下一步。
根据弹出的页面提示确认，组件将被安装在默认的kube-system命名空间中，并以组件名称发布应用。如需自定义应用名和命名空间，请根据页面提示设置。
选择Chart 版本为最新版本，在参数区域根据[步骤一](use-csi-secrets-store-provider-alibabacloud-to-import-alibaba-cloud-kms-service-credentials.md)选择的认证方式，设置相关参数，然后单击确定。
如果选择[通过](use-csi-secrets-store-provider-alibabacloud-to-import-alibaba-cloud-kms-service-credentials.md)[RRSA](use-csi-secrets-store-provider-alibabacloud-to-import-alibaba-cloud-kms-service-credentials.md)[授权](use-csi-secrets-store-provider-alibabacloud-to-import-alibaba-cloud-kms-service-credentials.md)，需将参数rrsa.enable设置为true，以开启RRSA认证功能。
rrsa: # Specifies whether using rrsa and enalbe sa token volume projection, default is false enable: true
其他相关参数配置如下。
envVarsFromSecret: # ACCESS_KEY_ID: # secretKeyRef: alibaba-credentials # key: id # SECRET_ACCESS_KEY: # secretKeyRef: alibaba-credentials # key: secret ALICLOUD_ROLE_ARN: secretKeyRef: alibaba-credentials key: rolearn # ALICLOUD_ROLE_SESSION_NAME: # secretKeyRef: alibaba-credentials # key: rolesessionname # ALICLOUD_ROLE_SESSION_EXPIRATION: # secretKeyRef: alibaba-credentials # key: rolesessionexpiration ALICLOUD_OIDC_PROVIDER_ARN: secretKeyRef: alibaba-credentials key: oidcproviderarn
如果选择[为集群对应的](use-csi-secrets-store-provider-alibabacloud-to-import-alibaba-cloud-kms-service-credentials.md)[Worker RAM](use-csi-secrets-store-provider-alibabacloud-to-import-alibaba-cloud-kms-service-credentials.md)[角色添加权限](use-csi-secrets-store-provider-alibabacloud-to-import-alibaba-cloud-kms-service-credentials.md)，可采用默认参数配置直接安装。
如果选择[通过设置](use-csi-secrets-store-provider-alibabacloud-to-import-alibaba-cloud-kms-service-credentials.md)[AK](use-csi-secrets-store-provider-alibabacloud-to-import-alibaba-cloud-kms-service-credentials.md)[扮演指定](use-csi-secrets-store-provider-alibabacloud-to-import-alibaba-cloud-kms-service-credentials.md)[RAM](use-csi-secrets-store-provider-alibabacloud-to-import-alibaba-cloud-kms-service-credentials.md)[角色](use-csi-secrets-store-provider-alibabacloud-to-import-alibaba-cloud-kms-service-credentials.md)，需配置如下相关参数。
envVarsFromSecret: ACCESS_KEY_ID: secretKeyRef: alibaba-credentials key: id SECRET_ACCESS_KEY: secretKeyRef: alibaba-credentials key: secret ALICLOUD_ROLE_ARN: secretKeyRef: alibaba-credentials key: rolearn # ALICLOUD_ROLE_SESSION_NAME: # secretKeyRef: alibaba-credentials # key: rolesessionname # ALICLOUD_ROLE_SESSION_EXPIRATION: # secretKeyRef: alibaba-credentials # key: rolesessionexpiration # ALICLOUD_OIDC_PROVIDER_ARN: # secretKeyRef: alibaba-credentials # key: oidcproviderarn
如需同步生成 Kubernetes Secret，需要配置如下相关参数。
syncSecret: enabled: true
secrets-store-csi-driver.syncSecret.enabled：是否启用同步为 Kubernetes Secret的功能。设置为true时，将部署必要的 RBAC Role和RoleBinding。
如需开启定时同步凭据的功能，需要配置如下相关参数。
secrets-store-csi-driver.enableSecretRotation：是否开启凭据的自动轮询功能，设置为true表示开启。
secrets-store-csi-driver.rotationPollInterval：凭据同步的频率，设置为120s，此处以两分钟同步一次凭据为例，可根据实际需求调整。
创建成功后，会自动跳转到目标集群的csi-secrets-store-provider-alibabacloud页面，检查安装结果。若所有资源创建成功，则表明组件安装成功。安装完成后，在控制台资源页面可查看组件创建的Kubernetes资源，包括：secrets-store-csi-driver和csi-secrets-store-provider-alibabacloud（ServiceAccount）、secretproviderclasses-admin-role、secretproviderclasses-viewer-role和secretproviderclasses-role（ClusterRole）、secretproviderclasses-rolebinding（ClusterRoleBinding）、secrets-store-csi-driver和csi-secrets-store-provider-alibabacloud（DaemonSet）、secrets-store.csi.k8s.io（CSIDriver）。
## 步骤三：配置数据同步信息
认证信息配置完成后，需通过SecretProviderClass来进行KMS凭据信息的配置。
### 配置模板说明
SecretProviderClass模板格式定义如下所示。
apiVersion: secrets-store.csi.x-k8s.io/v1 kind: SecretProviderClass metadata: name: <NAME> spec: provider: alibabacloud # 此处配置固定为'alibabacloud'。 parameters: objects: | - objectName: <KMS Encryption Parameter Name> # KMS 凭据名称 objectType: kms # 同步 KMS 凭据时固定为 kms
其中parameters通常包含挂载请求的三个字段：
| 参数 | 类型 | 说明 |
| --- | --- | --- |
| objects | 必选 | 挂载 Secrets 凭据的 YAML 配置声明。例如： parameters: objects: | - objectName: "MySecret" objectType: "kms" objects 可包含以下子字段： objectName ：必选，对应为指定 KMS 凭据管家中的密钥名称。更多信息，请参见 [SecretName](../../../../kms/documents/key-management-service/developer-reference/api-getsecretvalue.md) 。 objectType ：可选，可用于指定需要同步的阿里云服务类型，当前支持 kms 和 oos，默认为 kms，因此导入 KMS 服务凭据时可省略该字段。 objectAlias ：可选，可用于指定凭据在 Pod 中挂载的文件名称，如果不指定将默认使用 objectName 的值。 objectVersion ：可选，对应凭据管家中的参数 [VersionId](../../../../kms/documents/key-management-service/developer-reference/api-getsecretvalue.md) 。RDS 凭据、PolarDB 凭据、Redis/Tair 凭据、RAM 凭据和 ECS 凭据不支持指定 VersionId。 objectVersionLabel ：可选，对应凭据管家中的参数 [VersionStage](../../../../kms/documents/key-management-service/developer-reference/api-getsecretvalue.md) 。RDS 凭据、PolarDB 凭据、Redis/Tair 凭据、RAM 凭据和 ECS 凭据只能获取 ACSPrevious 和 ACSCurrent 对应版本的凭据值。 jmesPath ：可选，用于解析 JSON 格式的凭据中的指定键值对字段，例如，以下 test 凭据示例包含了一段 JSON： { "username": "testuser", "password": "testpassword" } 如需将 username 和 password 分别挂载为一个独立的密钥文件，可以使用如下的 JMESPath 字段配置。使用 JMESPath 字段时，必须指定以下两个子字段： path ：必选项，基于 [JMESPath](https://jmespath.org/specification.html) 定义路径检索指定配置项。 objectAlias ：必选项，指定的键值对将会以此参数配置作为文件路径挂载。 kmsEndpoint ：可选，用来配置 KMS 服务请求的 Endpoint 地址，未配置时使用默认 Endpoint。支持配置为 KMS 服务的共享网关或专属网关，且配置是凭据级的，即每个凭据都可以指定不同的 Endpoint 地址。字段配置说明请参见 [kmsEndpoint](use-csi-secrets-store-provider-alibabacloud-to-import-alibaba-cloud-kms-service-credentials.md) [配置说明](use-csi-secrets-store-provider-alibabacloud-to-import-alibaba-cloud-kms-service-credentials.md) 。 |
| region | 可选 | 用于请求指定 Region 下的阿里云凭据管家后端。如果不指定该参数，则默认使用节点对应的阿里云 Region。但在大规模应用 Pod 部署时，可能会带来额外的性能开销，所以推荐配置该参数指定 Region。 |
| pathTranslation | 可选 | 如果在凭据管家的密钥凭据包含文件分隔符，挂载到 Pod 中的密钥文件会使用该配置指定的字符作为路径之间的分隔符。例如，凭据管家中的 My/Path/Secret 会被挂载为名称是 My_Path_Secret 的密钥文件。 如果不指定该参数，则默认使用下划线作为分隔符。 如果该参数指定为 “False” ，则路径分隔符在挂载时对应的文件名将不会使用任何字符。 |
### 配置使用示例
本示例以ACK托管集群同一地域下的KMS服务凭据test为例，介绍如何通过SecretProviderClass将其导入到集群应用中。
使用以下简单的SecretProviderClass示例，创建secretstore.yaml文件。
apiVersion: secrets-store.csi.x-k8s.io/v1 kind: SecretProviderClass metadata: name: test-secrets spec: provider: alibabacloud # 此处固定配置为alibabacloud。 parameters: objects: | # objectType 支持oos和kms, 默认为kms - objectName: "test-hangzhou" objectType: "kms" objectAlias: "hangzhou-public" kmsEndpoint: "kms.{region}.aliyuncs.com"
执行以下命令，部署SecretProviderClass。
kubectl apply -f secretstore.yaml
使用以下内容，创建deploy.yaml。
包含一个Nginx Deployment实例，通过CSI Inline文件系统的形式声明使用了上面示例中已经创建的SecretProviderClass，并在Pod中的/mnt/secrets-store目录下挂载凭据密钥。关于Deployment实例更多信息，请参见[Deployment](https://github.com/AliyunContainerService/secrets-store-csi-driver-provider-alibaba-cloud/tree/main/examples)[示例](https://github.com/AliyunContainerService/secrets-store-csi-driver-provider-alibaba-cloud/tree/main/examples)。
apiVersion: apps/v1 # 1.8.0之前版本请使用apps/v1beta1。 kind: Deployment metadata: name: nginx-deployment-basic labels: app: nginx spec: replicas: 2 selector: matchLabels: app: nginx template: metadata: labels: app: nginx spec: volumes: - name: secrets-store-inline csi: driver: secrets-store.csi.k8s.io readOnly: true volumeAttributes: secretProviderClass: "test-secrets" containers: - name: nginx image: anolis-registry.cn-zhangjiakou.cr.aliyuncs.com/openanolis/nginx:1.14.1-8.6 # 替换为您的实际镜像。 ports: - containerPort: 80 resources: limits: cpu: "500m" volumeMounts: - name: secrets-store-inline mountPath: "/mnt/secrets-store" readOnly: true
执行以下命令，部署Deploy应用。
kubectl apply -f deploy.yaml
验证密钥是否被正常挂载。
登录Pod查看Secret的目标挂载路径/mnt/secrets-store下是否已经创建了SecretProviderClass实例中指定密钥名称为文件名的密钥文件，同时查看文件内容是否为KMS凭据中指定的密文。
### 将 KMS 凭据同步为 Kubernetes Secret
Secrets Store CSI Driver 支持将从外部密钥管理服务（如阿里云KMS、OOS）中获取的密钥，自动同步并创建为集群内原生的 Kubernetes Secret。应用无需修改代码，就能以标准方式使用这些外部密钥。
配置方法：SecretProviderClass
您可以在SecretProviderClass资源的spec中添加secretObjects可选字段来启用此功能。
apiVersion: secrets-store.csi.x-k8s.io/v1 kind: SecretProviderClass metadata: name: <NAME> spec: provider: alibabacloud # 此处配置固定为alibabacloud，请勿修改。 parameters: objects: | - objectName: <KMS Encryption Parameter Name> # KMS 凭据名称 objectType: kms # 同步 KMS 凭据时固定为 kms secretObjects: - secretName: <Kubernetes Secret Name> # Kubernetes Secret 名称 type: <Kubernetes Secret Type> # Kubernetes Secret 类型 data: - objectName: <parameters.objects.objectName> # parameters.objects.objectName 名称，当指定别名时，使用别名 key: <Kubernetes Secret Data Key> # Kubernetes Secret Data Key 字段名称
secretObjects通常包含以下三个参数：
| 参数 | 类型 | 说明 |
| --- | --- | --- |
| secretName | 必选 | 指定将在集群中创建的 Kubernetes Secret 的名称。 |
| type | 必选 | 定义所创建的 Secret 的类型。可取值： Opaque 、 kubernetes.io/basic-auth 、 bootstrap.kubernetes.io/token 、 kubernetes.io/dockerconfigjson 、 kubernetes.io/dockercfg 、 kubernetes.io/ssh-auth 、 kubernetes.io/service-account-token 、 kubernetes.io/tls |
| data | 必选 | 定义如何将从外部获取的密钥映射到 Secret 的 data 字段中。其子字段包括： objectName : 必选，引用 parameters.objects 中定义的密钥名称（ objectName ）。如果设置了别名，则引用其别名 objectAlias 。 key : 必选，指定该密钥内容在 Secret 的 data 字段中所使用的键（Key）。 |
同步生命周期
Secret对象的同步和清理是由挂载了对应SecretProviderClass的 Pod 动态触发的：
创建：当第一个使用该SecretProviderClass的 Pod 启动并成功挂载卷时，Secrets Store CSI Driver 才会执行同步操作，创建对应的 Kubernetes Secret。
更新：当安装 csi-secrets-store-provider-alibabacloud 组件，设置secrets-store-csi-driver.enableSecretRotation参数为true时，会根据参数secrets-store-csi-driver.rotationPollInterval来定时同步更新对应的 Kubernetes Secret，否则不会更新。
删除：当最后一个使用该SecretProviderClass的 Pod 被删除后，由 Secrets Store CSI Driver 自动创建的 Kubernetes Secret 也会被随之删除。
操作示例：同步KMS凭据并注入Pod环境变量
以下步骤将演示如何将KMS凭据同步为 Kubernetes Secret，并最终通过环境变量注入到 Nginx Pod 中。
创建 SecretProviderClass。
参见以下内容创建 syncSecret.yaml 文件，定义如何获取外部密钥以及如何将其同步。
apiVersion: secrets-store.csi.x-k8s.io/v1 kind: SecretProviderClass metadata: name: alibabacloud-sync-secret spec: provider: alibabacloud parameters: objects: | - objectName: test-kms objectAlias: secretalias objectType: kms secretObjects: - secretName: test-sync-secret # 生成的 Kubernetes Secret 名称 type: Opaque data: - objectName: secretalias # 对应 objectName 或 objectAlias key: test # 填充生成的 Kubernetes Secret data
部署 SecretProviderClass。
kubectl apply -f syncSecret.yaml
创建应用 Pod 以触发同步。
参见以下内容创建 pod-sync-secret.yaml 文件。此 Pod 会挂载上述SecretProviderClass，并尝试通过secretKeyRef引用将要生成的名为test-sync-secret的Secret。
kind: Pod apiVersion: v1 metadata: name: pod-sync-secret spec: containers: - name: nginx image: nginx:latest volumeMounts: - name: secrets-store-inline mountPath: "/mnt/secrets-store" readOnly: true env: - name: SECRET_TEST valueFrom: secretKeyRef: name: test-sync-secret key: test volumes: - name: secrets-store-inline csi: driver: secrets-store.csi.k8s.io readOnly: true volumeAttributes: secretProviderClass: "alibabacloud-sync-secret"
部署 Pod，同时触发 Secret 的同步。
kubectl apply -f pod-sync-secret.yaml
验证结果：
检查 Kubernetes Secret 是否已生成。
kubectl get secret test-sync-secret
执行后，您将看到名为 test-sync-secret 的 Secret。
检查 Pod 环境变量是否成功注入：
kubectl exec -it $(kubectl get pods | awk '/pod-sync-secret/{print $1}' | head -1) -- env
您将看到环境变量SECRET_TEST及其从KMS加密参数中获取到的值。
### kmsEndpoint配置说明
可通过专属网关访问或共享网关访问两种方式访问KMS服务获取凭据，请参考以下要求进行Endpoint配置。关于专属网关访问和共享网关访问的更多差异，请参见[共享网关和专属网关的差异](../../../../kms/documents/key-management-service/developer-reference/classic-kms-sdkclassic-kms-sdk.md)。
KMS Endpoint地址说明
| 网关类型 | 域名类型 | Endpoint 地址 | 使用说明 |
| --- | --- | --- | --- |
| 专属网关 | KMS 私网域名 | {kms-instance-id}.cryptoservice.kms.aliyuncs.com | 要求 KMS 凭据所属实例和集群在同一 Region 及同一 VPC 中。 替换 {kms-instance-id} 为 KMS 凭据所属实例 ID。 KMS 凭据所属实例版本为 3.0 以上。 |
| 共享网关 | VPC 域名 | kms-vpc.{region}.aliyuncs.com | 要求 KMS 凭据和集群在同一 Region。 替换 {region} 为 KMS 凭据所在的 Region。 应用默认配置，使用此地址时无需配置。 |
| 共享网关 | 公网 | kms.{region}.aliyuncs.com | 替换 {region} 为 KMS 凭据所在的 Region。 集群具有公网访问能力。 |
KMS Endpoint配置示例
apiVersion: secrets-store.csi.x-k8s.io/v1 kind: SecretProviderClass metadata: name: test spec: provider: alibabacloud # 固定值为 'alibabacloud' parameters: # 示例使用网关说明： # hangzhou-public 使用共享网关公网域名，需要将{region}替换为KMS凭据所在的Region，此方式可获取和集群不在同一Region的KMS凭据 # hangzhou-vpc 未指定kmsEndpoint字段，使用默认的共享网关VPC域名 # hangzhou-cryptoservice 使用专属网关，需要替换{kms-instance-id}为KMS凭据所属实例ID # london-public 使用共享网关公网域名，需要将{region}替换为KMS凭据所在的Region，此方式可获取和集群不在同一Region的KMS凭据 objects: | - objectName: "test-hangzhou" objectType: "kms" objectAlias: "hangzhou-public" kmsEndpoint: "kms.{region}.aliyuncs.com" - objectName: "test-hangzhou" objectType: "kms" objectAlias: "hangzhou-vpc" - objectName: "test-hangzhou" objectType: "kms" objectAlias: "hangzhou-cryptoservice" kmsEndpoint: "{kms-instance-id}.cryptoservice.kms.aliyuncs.com" - objectName: "test-london" objectAlias: "london-public" kmsEndpoint: "kms.{region}.aliyuncs.com"
## 相关文档
如需为ACK Serverless集群中的应用导入阿里云KMS凭据，请参见[使用](use-ack-secret-manager-to-import-alibaba-cloud-kms-service-credentials.md)[ack-secret-manager](use-ack-secret-manager-to-import-alibaba-cloud-kms-service-credentials.md)[导入阿里云](use-ack-secret-manager-to-import-alibaba-cloud-kms-service-credentials.md)[KMS](use-ack-secret-manager-to-import-alibaba-cloud-kms-service-credentials.md)[服务凭据](use-ack-secret-manager-to-import-alibaba-cloud-kms-service-credentials.md)。
为了保护从KMS读取后缓存在ACK集群中的Secret，可对ACK集群Secret进行一键加密。具体操作，请参见[使用阿里云](use-kms-to-encrypt-kubernetes-secrets-2.md)[KMS](use-kms-to-encrypt-kubernetes-secrets-2.md)[进行](use-kms-to-encrypt-kubernetes-secrets-2.md)[Secret](use-kms-to-encrypt-kubernetes-secrets-2.md)[的落盘加密](use-kms-to-encrypt-kubernetes-secrets-2.md)。
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
