## 步骤二：安装csi-secrets-store-provider-alibabacloud组件
登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。
在集群列表页面，单击目标集群名称，然后在左侧导航栏，选择应用>Helm。
在Helm页面，单击创建，在Chart区域搜索并选中csi-secrets-store-provider-alibabacloud，其他设置保持默认，然后单击下一步。
根据弹出的页面提示确认，组件将被安装在默认的kube-system命名空间中，并以组件名称发布应用。如需自定义应用名和命名空间，请根据页面提示设置。
选择Chart 版本为最新版本，在参数区域根据[步骤一](use-csi-secrets-store-provider-alibabacloud-to-import-alibaba-cloud-kms-service-credentials.md)选择的认证方式，设置相关参数，然后单击确定。
如果选择[通过](use-csi-secrets-store-provider-alibabacloud-to-import-alibaba-cloud-kms-service-credentials.md)[RRSA](use-csi-secrets-store-provider-alibabacloud-to-import-alibaba-cloud-kms-service-credentials.md)[授权](use-csi-secrets-store-provider-alibabacloud-to-import-alibaba-cloud-kms-service-credentials.md)，需将参数rrsa.enable设置为true，以开启RRSA认证功能。
rrsa: # Specifies whether using rrsa and enalbe sa token volume projection, default is false enable: true
其他相关参数配置如下。
envVarsFromSecret: # ACCESS_KEY_ID: # secretKeyRef: alibaba-credentials # key: id # SECRET_ACCESS_KEY: # secretKeyRef: alibaba-credentials # key: secret ALICLOUD_ROLE_ARN: secretKeyRef: alibaba-credentials key: rolearn # ALICLOUD_ROLE_SESSION_NAME: # secretKeyRef: alibaba-credentials #
