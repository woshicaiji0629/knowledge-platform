列表。设置为空数组 [] ，表示允许所有值。 |
| memoryRequests | array | 容器内存 requests 的白名单列表。设置为空数组 [] ，表示允许所有值。 |
| memoryLimits | array | 容器内存 limits 的白名单列表。设置为空数组 [] ，表示允许所有值。 |

示例：
Constraint：
apiVersion: constraints.gatekeeper.sh/v1beta1 kind: ACKContainerResourcesWhitelist metadata: name: container-resources-whitelist spec: enforcementAction: deny match: kinds: - apiGroups: [ "" ] kinds: [ "Pod" ] namespaces: - "test-gatekeeper" parameters: cpuRequests: - "100m" - "500m" - "1" cpuLimits: - "2" - "4000m" memoryRequests: - "256Mi" - "512Mi" memoryLimits: - "1Gi" - "2048Mi"
Allowed：
apiVersion: v1 kind: Pod metadata: name: pod-0 namespace: test-gatekeeper spec: containers: - image: anolis-registry.cn-zhangjiakou.cr.aliyuncs.com/openanolis/nginx:1.14.1-8.6 name: test-container resources: requests: cpu: 100m memory: 512Mi limits: cpu: "2" memory: 1Gi
Disallowed：
apiVersion: v1 kind: Pod metadata: name: pod-0 namespace: test-gatekeeper spec: containers: - image: anolis-registry.cn-zhangjiakou.cr.aliyuncs.com/openanolis/nginx:1.14.1-8.6 name: test-container resources: requests: cpu: 10m memory: 512Mi limits: cpu: "1" memory: 1Gi
