replicas: 2 selector: matchLabels: app: nginx template: metadata: labels: app: nginx spec: volumes: - name: secrets-store-inline csi: driver: secrets-store.csi.k8s.io readOnly: true volumeAttributes: secretProviderClass: "test-secrets" containers: - name: nginx image: anolis-registry.cn-zhangjiakou.cr.aliyuncs.com/openanolis/nginx:1.14.1-8.6 # 替换为您的实际镜像。 ports: - containerPort: 80 resources: limits: cpu: "500m" volumeMounts: - name: secrets-store-inline mountPath: "/mnt/secrets-store" readOnly: true
执行以下命令，部署Deploy应用。
kubectl apply -f deploy.yaml
验证密钥是否被正常挂载。
登录Pod查看Secret的目标挂载路径/mnt/secrets-store下是否已经创建了SecretProviderClass实例中指定密钥名称为文件名的密钥文件，同时查看文件内容是否为KMS凭据中指定的密文。
