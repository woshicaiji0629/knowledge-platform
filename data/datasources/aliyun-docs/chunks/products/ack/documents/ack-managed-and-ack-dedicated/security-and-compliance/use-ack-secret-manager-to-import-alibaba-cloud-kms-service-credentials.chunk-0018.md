ind: Secret metadata: name: ramuser namespace: kube-system type: Opaque
执行以下命令，创建名为ramuser的Secret。
kubectl apply -f ramuser.yaml
创建自定义资源SecretStore关联对应的认证方式并部署。
使用以下内容，替换相关字段后，创建secretstore-ramrole.yaml文件。
<ACCOUNT_ID>：替换为同步KMS凭据的阿里云账号ID。
<ROLE_NAME>：替换为[步骤](use-ack-secret-manager-to-import-alibaba-cloud-kms-service-credentials.md)[1](use-ack-secret-manager-to-import-alibaba-cloud-kms-service-credentials.md)中创建的RAM角色名称。
<SECRET_NAME>：替换为存储AK、SK的Secret名称。
<SECRET_NAMESPACE>：替换为存储AK、SK的Secret的命名空间。
<SECRET_KEY_AK>和<SECRET_KEY_SK>：替换为存储AK、SK的Secret中data字段下的键名（key）。
<ROLE_SESSION_NAME>：替换为角色会话名称（自定义字符串）。
apiVersion: alibabacloud.com/v1alpha1 kind: SecretStore metadata: name: scdemo-ramrole spec: KMS: KMSAuth: accessKey: name: <SECRET_NAME> namespace: <SECRET_NAMESPACE> key: <SECRET_KEY_AK> accessKeySecret: name: <SECRET_NAME> namespace: <SECRET_NAMESPACE> key: <SECRET_KEY_SK> ramRoleARN: "acs:ram::<ACCOUNT_ID>:role/<ROLE_NAME>" ramRoleSessionName: <ROLE_SESSION_NAME>
执行以下命令，部署SecretStore。
kubectl apply -f secretstore-ramrole.yaml
