### ACKPSPCapabilities
规则说明：限制在集群指定范围内部署的Pod配置Linux Capabilities能力。
重要等级：high。
参数说明：

| 参数名称 | 参数类型 | 参数说明 |
| --- | --- | --- |
| allowedCapabilities | array | 允许的 capabilities 白名单。 |
| requiredDropCapabilities | array | 需要强制 Drop 的 capabilities 。 |

示例：
Constraint：
apiVersion: constraints.gatekeeper.sh/v1beta1 kind: ACKPSPCapabilities metadata: name: psp-capabilities spec: match: kinds: - apiGroups: [""] kinds: ["Pod"] namespaces: - "test-gatekeeper" parameters: allowedCapabilities: ["CHOWN"] requiredDropCapabilities: ["NET_ADMIN", "SYS_ADMIN", "NET_RAW"]
Allowed：
apiVersion: v1 kind: Pod metadata: creationTimestamp: null labels: run: test name: good-4 namespace: test-gatekeeper spec: containers: - image: test name: test securityContext: capabilities: add: - CHOWN drop: - "NET_ADMIN" - "SYS_ADMIN" - "NET_RAW"
Disallowed：
apiVersion: v1 kind: Pod metadata: creationTimestamp: null labels: run: test name: bad-1 namespace: test-gatekeeper spec: containers: - image: test name: test
