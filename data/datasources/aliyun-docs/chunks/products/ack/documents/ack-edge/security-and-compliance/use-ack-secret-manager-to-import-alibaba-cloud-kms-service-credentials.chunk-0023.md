tore-ramrole.yaml文件。
{ACK-accountID}：替换为集群所在的阿里云账号B的账号ID。
{clusterID}：替换为集群ID。
{ACK-roleName}：替换为集群所在的阿里云账号B下创建的RAM角色的名称。
{KMS-accountID}：替换为KMS实例所在的阿里云账号A的账号ID。
{KMS-roleName}：替换为KMS实例所在的阿里云账号A下创建的RAM角色的名称。
{roleSessionName}：替换为角色会话名称（自定义字符串）。
apiVersion: 'alibabacloud.com/v1alpha1' kind: SecretStore metadata: name: scdemo-cross-account spec: KMS: KMSAuth: oidcProviderARN: "acs:ram::{ACK-accountID}:oidc-provider/ack-rrsa-{clusterID}" ramRoleARN: "acs:ram::{ACK-accountID}:role/{ACK-roleName}" remoteRamRoleARN: "acs:ram::{KMS-accountID}:role/{KMS-roleName}" remoteRamRoleSessionName: {roleSessionName}
配置数据同步信息。具体操作，请参见[步骤三：配置数据同步信息](use-ack-secret-manager-to-import-alibaba-cloud-kms-service-credentials.md)。
