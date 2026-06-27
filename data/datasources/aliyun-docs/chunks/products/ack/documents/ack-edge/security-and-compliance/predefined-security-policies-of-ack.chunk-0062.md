### ACKPSPSeccomp
规则说明：限制在集群指定范围内部署的Pod使用指定的Seccomp配置文件。
重要等级：low。
参数说明：

| 参数名称 | 参数类型 | 参数说明 |
| --- | --- | --- |
| allowedProfileTypes | array | 允许的 Seccomp profile 类型白名单。 |
| allowedProfiles | array | 允许的 Seccomp profile。 |

示例：
Constraint：
apiVersion: constraints.gatekeeper.sh/v1beta1 kind: ACKPSPSeccomp metadata: name: psp-seccomp spec: match: kinds: - apiGroups: [""] kinds: ["Pod"] namespaces: - "test-gatekeeper" parameters: allowedProfileTypes: # - Unconfined - RuntimeDefault - Localhost allowedProfiles: - runtime/default - docker/default - localhost/profiles/audit.json
Allowed：
apiVersion: v1 kind: Pod metadata: creationTimestamp: null labels: run: test name: good namespace: test-gatekeeper spec: containers: - image: test name: test securityContext: seccompProfile: type: Localhost localhostProfile: profiles/audit.json initContainers: - image: test name: test2 securityContext: seccompProfile: type: Localhost localhostProfile: profiles/audit.json
Disallowed：
apiVersion: v1 kind: Pod metadata: creationTimestamp: null labels: run: test echo-k8s-webhook-enabled: 'true' name: bad namespace: test-gatekeeper spec: containers: - image: test name: test
