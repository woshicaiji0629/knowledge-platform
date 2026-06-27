ovider-alibabacloud-to-import-alibaba-cloud-kms-service-credentials.md)[角色](use-csi-secrets-store-provider-alibabacloud-to-import-alibaba-cloud-kms-service-credentials.md)，需配置如下相关参数。
envVarsFromSecret: ACCESS_KEY_ID: secretKeyRef: alibaba-credentials key: id SECRET_ACCESS_KEY: secretKeyRef: alibaba-credentials key: secret ALICLOUD_ROLE_ARN: secretKeyRef: alibaba-credentials key: rolearn # ALICLOUD_ROLE_SESSION_NAME: # secretKeyRef: alibaba-credentials # key: rolesessionname # ALICLOUD_ROLE_SESSION_EXPIRATION: # secretKeyRef: alibaba-credentials # key: rolesessionexpiration # ALICLOUD_OIDC_PROVIDER_ARN: # secretKeyRef: alibaba-credentials # key: oidcproviderarn
如需同步生成 Kubernetes Secret，需要配置如下相关参数。
syncSecret: enabled: true
secrets-store-csi-driver.syncSecret.enabled：是否启用同步为 Kubernetes Secret的功能。设置为true时，将部署必要的 RBAC Role和RoleBinding。
如需开启定时同步凭据的功能，需要配置如下相关参数。
secrets-store-csi-driver.enableSecretRotation：是否开启凭据的自动轮询功能，设置为true表示开启。
secrets-store-csi-driver.rotationPollInterval：凭据同步的频率，设置为120s，此处以两分钟同步一次凭据为例，可根据实际需求调整。
创建成功后，会自动跳转到目标集群的csi-secrets-store-provider-alibabacloud页面，检查安装结果。若所有资源创建成功，则表明组件安装成功。安装完成后，在控制台资源页面可查看组件创建的Kubernetes资源，包括：secrets-store-csi-driver和csi-secrets-store-pr
