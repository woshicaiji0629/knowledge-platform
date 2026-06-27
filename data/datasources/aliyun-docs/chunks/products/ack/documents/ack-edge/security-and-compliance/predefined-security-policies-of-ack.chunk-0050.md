### ACKPSPAllowPrivilegeEscalationContainer
规则说明：限制在集群指定范围内部署的Pod配置allowPrivilegeEscalation参数。
重要等级：medium。
参数说明：无。
示例：
Constraint：
apiVersion: constraints.gatekeeper.sh/v1beta1 kind: ACKPSPAllowPrivilegeEscalationContainer metadata: name: psp-allow-privilege-escalation-container spec: match: kinds: - apiGroups: [""] kinds: ["Pod"] namespaces: - "test-gatekeeper"
Allowed：
apiVersion: v1 kind: Pod metadata: creationTimestamp: null labels: run: test name: good namespace: test-gatekeeper spec: containers: - image: test name: test securityContext: allowPrivilegeEscalation: false initContainers: - image: test name: test2 securityContext: allowPrivilegeEscalation: false
Disallowed：
apiVersion: v1 kind: Pod metadata: creationTimestamp: null labels: run: test name: bad namespace: test-gatekeeper spec: containers: - image: test name: test
