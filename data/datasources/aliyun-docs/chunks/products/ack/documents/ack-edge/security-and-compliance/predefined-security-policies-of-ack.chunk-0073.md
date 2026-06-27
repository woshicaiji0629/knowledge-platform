示例：
Constraint：
apiVersion: constraints.gatekeeper.sh/v1beta1 kind: ACKWorkloadReplicasRange metadata: name: replica-limiter spec: enforcementAction: deny match: kinds: - apiGroups: ["*"] kinds: ["Deployment", "StatefulSet", "ReplicaSet", "Scale"] namespaces: - "test-gatekeeper" parameters: minReplicas: 2 maxReplicas: 3
Allowed：
apiVersion: apps/v1 kind: Deployment metadata: name: nginx-deployment-basic namespace: test-gatekeeper labels: app: nginx spec: replicas: 2 selector: matchLabels: app: nginx template: metadata: labels: app: nginx spec: containers: - name: nginx image: anolis-registry.cn-zhangjiakou.cr.aliyuncs.com/openanolis/nginx:1.14.1-8.6 ports: - containerPort: 80 resources: limits: cpu: "500m"
Disallowed：
apiVersion: apps/v1 kind: Deployment metadata: name: nginx-deployment-basic-0 namespace: test-gatekeeper labels: app: nginx spec: replicas: 1 selector: matchLabels: app: nginx template: metadata: labels: app: nginx spec: containers: - name: nginx image: anolis-registry.cn-zhangjiakou.cr.aliyuncs.com/openanolis/nginx:1.14.1-8.6 ports: - containerPort: 80 resources: limits: cpu: "500m" --- apiVersion: apps/v1 kind: Deployment metadata: name: nginx-deployment-basic-1 nam
