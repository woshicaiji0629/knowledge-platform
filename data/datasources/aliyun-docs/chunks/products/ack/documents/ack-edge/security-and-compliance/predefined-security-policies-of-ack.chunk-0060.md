### ACKPSPProcMount
规则说明：限制在集群指定范围内部署的Pod允许挂载的proc类型。
重要等级：high。
参数说明：

| 参数名称 | 参数类型 | 参数说明 |
| --- | --- | --- |
| procMount | string | proc 挂载类型，允许配置如下类型： Default：默认屏蔽挂载 /proc 目录。 Unmasked：不屏蔽挂载 /proc 。 关于参数配置的具体说明，请参见 [AllowedProcMountTypes](https://kubernetes.io/docs/concepts/policy/pod-security-policy/?spm=a2c4g.11186623.0.0.38671d80Jvlhsj#allowedprocmounttypes) 。 |

示例：
Constraint：
apiVersion: constraints.gatekeeper.sh/v1beta1 kind: ACKPSPProcMount metadata: name: psp-proc-mount spec: match: kinds: - apiGroups: [""] kinds: ["Pod"] namespaces: - "test-gatekeeper" parameters: procMount: Default # Default or Unmasked
Allowed：
apiVersion: v1 kind: Pod metadata: creationTimestamp: null labels: run: test name: good1 namespace: test-gatekeeper spec: containers: - image: test name: test securityContext: procMount: "Default"
Disallowed：
apiVersion: v1 kind: Pod metadata: creationTimestamp: null labels: run: test name: bad3 namespace: test-gatekeeper spec: hostUsers: false containers: - image: test name: test securityContext: procMount: "Unmasked" initContainers: - image: test name: test2
