### ACKContainerRequests
规则说明：要求集群中某些应用 Pod 必须声明资源requests。
重要等级：low。
参数说明：

| 参数名称 | 参数类型 | 参数说明 |
| --- | --- | --- |
| cpu | string | 容器 CPU requests 的最大值。 |
| memory | string | 容器内存 requests 的最大值。 |

示例：
Constraint：
apiVersion: constraints.gatekeeper.sh/v1beta1 kind: ACKContainerRequests metadata: name: container-must-have-requests spec: enforcementAction: deny match: kinds: - apiGroups: [""] kinds: ["Pod"] namespaces: - "test-gatekeeper" parameters: cpu: "1000m" memory: "1Gi"
Allowed：
apiVersion: v1 kind: Pod metadata: name: pod-1 namespace: test-gatekeeper spec: containers: - image: openpolicyagent/test-webserver name: test-container resources: requests: memory: "100Mi" cpu: "500m"
Disallowed：
apiVersion: v1 kind: Pod metadata: name: pod-0 namespace: test-gatekeeper spec: containers: - image: openpolicyagent/test-webserver name: test-container
