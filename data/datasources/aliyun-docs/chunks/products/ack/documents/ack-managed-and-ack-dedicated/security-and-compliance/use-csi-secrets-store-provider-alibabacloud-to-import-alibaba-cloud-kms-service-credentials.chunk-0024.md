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
参见以下内容创建 pod-sync-secret.yaml 文件。此 Pod 会挂载上述SecretProviderClass，并尝试通过secretKeyRef引用将要生成的名为test-sy
