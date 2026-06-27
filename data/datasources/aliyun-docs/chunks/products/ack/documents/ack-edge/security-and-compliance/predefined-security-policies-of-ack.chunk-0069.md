equests | object | 包含以下取值。 min ：容器内存 requests 的最小值。 max ：容器内存 requests 的最大值。 |
| memoryLimits | object | 包含以下取值。 min ：容器内存 limits 的最小值。 max ：容器内存 limits 的最大值。 |

示例：
Constraint：
apiVersion: constraints.gatekeeper.sh/v1beta1 kind: ACKContainerResourcesRange metadata: name: container-resources-range spec: enforcementAction: deny match: kinds: - apiGroups: [ "" ] kinds: [ "Pod" ] namespaces: - "test-gatekeeper" parameters: cpuRequests: min: "100m" max: "1" cpuLimits: min: "500m" max: "2" memoryRequests: min: "256Mi" max: "512Mi" memoryLimits: min: "1Gi" max: "2048Mi"
Allowed：
apiVersion: v1 kind: Pod metadata: name: pod-0 namespace: test-gatekeeper spec: containers: - image: anolis-registry.cn-zhangjiakou.cr.aliyuncs.com/openanolis/nginx:1.14.1-8.6 name: test-container resources: requests: cpu: 100m memory: 512Mi limits: cpu: "2" memory: 2Gi
Disallowed：
apiVersion: v1 kind: Pod metadata: name: pod-0 namespace: test-gatekeeper spec: containers: - image: anolis-registry.cn-zhangjiakou.cr.aliyuncs.com/openanolis/nginx:1.14.1-8.6 name: test-container resources: requests: cpu: 10m memory: 5Mi limits: cpu: "3" memory: 128Mi
