## kubectl
创建oss-workload.yaml。
apiVersion: apps/v1 kind: Deployment metadata: name: oss-workload labels: app: nginx spec: replicas: 2 selector: matchLabels: app: nginx template: metadata: labels: app: nginx spec: containers: - name: nginx image: anolis-registry.cn-zhangjiakou.cr.aliyuncs.com/openanolis/nginx:1.14.1-8.6 ports: - containerPort: 80 volumeMounts: # 容器内的挂载路径 - name: pvc-oss mountPath: "/data" # 配置健康检查 livenessProbe: exec: command: - ls - /data initialDelaySeconds: 30 periodSeconds: 30 volumes: - name: pvc-oss persistentVolumeClaim: # 引用此前创建的PVC claimName: pvc-oss
创建应用。
kubectl create -f oss-workload.yaml
验证挂载结果。
确认Pod处于Running状态。
kubectl get pod -l app=nginx
进入Pod，查看挂载点。
kubectl exec -it <pod-name> -- ls /data
输出中，可查看OSS挂载路径下的数据。
