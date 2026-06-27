### ACKPSPFSGroup
规则说明：限制在集群指定范围内部署的Pod的fsGroup配置。
重要等级：medium。
参数说明：

| 参数名称 | 参数类型 | 参数说明 |
| --- | --- | --- |
| rule | string | 关于该参数的具体说明，请参见原 PSP 规则中对 fsGroup 的配置，支持 MustRunAs 、 MayRunAs 、 RunAsAny 。更多信息，请参见 [Volumes and file systems](https://kubernetes.io/docs/concepts/policy/pod-security-policy/?spm=a2c4g.11186623.0.0.38671d80Jvlhsj#volumes-and-file-systems) 。 |
| ranges | object | 包含以下取值。 min：fsGroup id 的最小值。 max：fsGroup id 的最大值。 |

示例：
Constraint：
apiVersion: constraints.gatekeeper.sh/v1beta1 kind: ACKPSPFSGroup metadata: name: psp-fsgroup spec: match: kinds: - apiGroups: [""] kinds: ["Pod"] namespaces: - "test-gatekeeper" parameters: rule: "MayRunAs" #"MustRunAs" #"MayRunAs", "RunAsAny" ranges: - min: 1 max: 1000
Allowed：
apiVersion: v1 kind: Pod metadata: creationTimestamp: null labels: run: test name: good namespace: test-gatekeeper spec: securityContext: fsGroup: 100 containers: - image: test name: test
Disallowed：
apiVersion: v1 kind: Pod metadata: creationTimestamp: null labels: run: test name: bad-1 namespace: non-test-gatekeeper spec: securityContext: fsGroup: 0 shareProcessNamespace: true containers: - image: test name: test
