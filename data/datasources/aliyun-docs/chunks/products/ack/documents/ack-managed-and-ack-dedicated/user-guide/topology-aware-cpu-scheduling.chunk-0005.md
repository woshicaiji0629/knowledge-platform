## 步骤一：部署示例应用
本文以一个Nginx应用为例，介绍如何启用CPU拓扑感知调度，实现CPU绑核。
创建nginx-app.yaml。
展开查看YAML
apiVersion: apps/v1 kind: Deployment metadata: name: nginx-deployment namespace: default labels: app: nginx spec: replicas: 1 selector: matchLabels: app: nginx template: metadata: labels: app: nginx spec: containers: - name: nginx image: alibaba-cloud-linux-3-registry.cn-hangzhou.cr.aliyuncs.com/alinux3/nginx_optimized:20240221-1.20.1-2.3.0 ports: - containerPort: 80 command: - "sleep" - "infinity" resources: requests: cpu: 4 memory: 8Gi limits: # 设置cpu值，需为整数。 cpu: 4 memory: 8Gi
部署应用。
kubectl apply -f nginx-app.yaml
[登录](overview-of-node-management.md)[Pod](overview-of-node-management.md)[所在节点](overview-of-node-management.md)，获取Pod的UID和Container ID。
获取Pod名称。
执行kubectl get pods -n <your-namespace>查看Pod名称，如nginx-deployment-6f5899*****。
获取Pod UID。
