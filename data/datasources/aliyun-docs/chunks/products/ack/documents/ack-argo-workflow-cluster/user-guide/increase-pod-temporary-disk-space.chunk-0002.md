### 设置Pod resource
apiVersion: argoproj.io/v1alpha1 kind: Workflow metadata: generateName: helloworld-- spec: entrypoint: helloworld templates: - name: helloworld container: image: mirrors-ssl.aliyuncs.com/busybox:latest resources: requests: ephemeral-storage: 50Gi # 声明临时存储空间大小 command: - sh - -c args: - echo "Hello, world!"; sleep 60;
该文章对您有帮助吗？
反馈
