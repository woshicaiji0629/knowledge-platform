## 自动绑核策略
配置方法：
添加两个Annotation：cpuset-scheduler: "true"和cpu-policy: "static-burst"
Pod中：在metadata.annotations字段中添加
工作负载（例如Deployment）中：在spec.template.metadata.annotations字段中添加
在Containers字段中配置resources.limits.cpu的取值（需为整数），限定CPU绑核范围。
配置示例：
apiVersion: apps/v1 kind: Deployment metadata: name: nginx-deployment namespace: default labels: app: nginx spec: replicas: 1 selector: matchLabels: app: nginx template: metadata: annotations: # 设置为true，启用CPU拓扑感知调度 cpuset-scheduler: "true" # 设置为static-burst，启用自动绑核与NUMA亲和策略 cpu-policy: "static-burst" labels: app: nginx spec: containers: - name: nginx image: alibaba-cloud-linux-3-registry.cn-hangzhou.cr.aliyuncs.com/alinux3/nginx_optimized:20240221-1.20.1-2.3.0 ports: - containerPort: 80 command: - "sleep" - "infinity" resources: requests: cpu: 4 memory: 8Gi limits: # 设置cpu值，需为整数 cpu: 4 memory: 8Gi
结果验证：
自动绑核策略会实时分析节点的CPU拓扑和资源使用情况，绑核数量可能会大于Pod的显式请求。绑核情况可通过以下两种方式查看。
