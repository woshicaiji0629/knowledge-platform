示例：
Constraint:
apiVersion: constraints.gatekeeper.sh/v1beta1 kind: ACKResourceDeletionProtection metadata: name: resource-deletion-protection annotations: description: "Protect resources from being accidentally deleted." spec: enforcementAction: deny match: kinds: - apiGroups: - "" kinds: - Service - Namespace - apiGroups: - extensions - networking.k8s.io kinds: - Ingress - apiGroups: - apps kinds: - Deployment - StatefulSet - DaemonSet - apiGroups: - batch kinds: - Job - CronJob parameters: labels: - labelName: policy.alibabacloud.com/delete-protection labelValue: "true"
Allowed：
apiVersion: apps/v1 kind: Deployment metadata: name: test-deployment namespace: test-gatekeeper spec: replicas: 2 selector: matchLabels: app: test-app template: metadata: labels: app: test-app spec: containers: - name: nginx image: nginx:latest ports: - containerPort: 80
Disallowed：
apiVersion: apps/v1 kind: Deployment metadata: name: test-deployment namespace: test-gatekeeper labels: policy.alibabacloud.com/delete-protection: "true" spec: replicas: 2 selector: matchLabels: app: test-app template: metadata: labels: app: test-app spec: containers: - name: nginx image: nginx:latest ports: - containerPort:
