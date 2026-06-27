roviderClass。
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
