ype: Opaque
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
