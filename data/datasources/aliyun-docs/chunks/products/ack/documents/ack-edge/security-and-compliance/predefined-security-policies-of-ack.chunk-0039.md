### ACKContainerLimits
规则说明：要求集群指定范围的应用Pod配置资源limits。
重要等级：low。
参数说明：无。
示例：
Constraint：
apiVersion: constraints.gatekeeper.sh/v1beta1 kind: ACKContainerLimits metadata: name: container-must-have-limits spec: match: kinds: - apiGroups: [""] kinds: ["Pod"] namespaces: - "test-gatekeeper" parameters: cpu: "1000m" memory: "1Gi"
Allowed：
apiVersion: v1 kind: Pod metadata: name: pod-1 namespace: test-gatekeeper spec: containers: - image: openpolicyagent/test-webserver name: test-container resources: limits: memory: "100Mi" cpu: "500m"
Disallowed：
apiVersion: v1 kind: Pod metadata: name: pod-2 namespace: non-test-gatekeeper spec: containers: - image: openpolicyagent/test-webserver name: test-container resources: limits: memory: "100Gi" cpu: "2000m"
